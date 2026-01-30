#!/usr/bin/env python3
"""
Real-time Face Changer Tool
This module provides real-time face detection, landmark detection, and face swapping capabilities.
"""

import cv2
import dlib
import numpy as np
import sys
import argparse
from imutils import face_utils


class FaceChanger:
    """Main class for real-time face changing operations."""
    
    def __init__(self):
        """Initialize face detector and landmark predictor."""
        # Initialize dlib's face detector and facial landmark predictor
        self.detector = dlib.get_frontal_face_detector()
        try:
            self.predictor = dlib.shape_predictor("shape_predictor_68_face_landmarks.dat")
        except RuntimeError:
            print("Error: Could not load shape_predictor_68_face_landmarks.dat")
            print("Please download it from: https://github.com/davisking/dlib-models/raw/master/shape_predictor_68_face_landmarks.dat.bz2")
            print("Extract and place it in the same directory as this script.")
            sys.exit(1)
    
    def detect_faces(self, frame):
        """
        Detect faces in a frame.
        
        Args:
            frame: Input image frame
            
        Returns:
            List of detected face rectangles
        """
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        faces = self.detector(gray, 1)
        return faces
    
    def get_landmarks(self, frame, face):
        """
        Get facial landmarks for a detected face.
        
        Args:
            frame: Input image frame
            face: Detected face rectangle
            
        Returns:
            Numpy array of facial landmarks
        """
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        shape = self.predictor(gray, face)
        landmarks = face_utils.shape_to_np(shape)
        return landmarks
    
    def apply_face_mask(self, frame, landmarks):
        """
        Apply a simple face mask effect.
        
        Args:
            frame: Input image frame
            landmarks: Facial landmarks
            
        Returns:
            Modified frame with face mask
        """
        # Create a mask for the face region
        mask = np.zeros(frame.shape[:2], dtype=np.uint8)
        
        # Fill convex hull of face landmarks
        hull = cv2.convexHull(landmarks)
        cv2.fillConvexPoly(mask, hull, 255)
        
        # Apply blur to the face region
        blurred = cv2.GaussianBlur(frame, (99, 99), 30)
        
        # Combine original and blurred using the mask
        result = np.where(mask[..., None] == 255, blurred, frame)
        
        return result
    
    def swap_faces(self, frame1, landmarks1, frame2, landmarks2):
        """
        Swap faces between two frames.
        
        Args:
            frame1: First frame
            landmarks1: Landmarks for first face
            frame2: Second frame
            landmarks2: Landmarks for second face
            
        Returns:
            Frame with swapped faces
        """
        # Get convex hulls
        hull1 = cv2.convexHull(landmarks1)
        hull2 = cv2.convexHull(landmarks2)
        
        # Create masks
        mask1 = np.zeros(frame1.shape[:2], dtype=np.uint8)
        mask2 = np.zeros(frame2.shape[:2], dtype=np.uint8)
        cv2.fillConvexPoly(mask1, hull1, 255)
        cv2.fillConvexPoly(mask2, hull2, 255)
        
        # Extract face regions
        face1 = cv2.bitwise_and(frame1, frame1, mask=mask1)
        face2 = cv2.bitwise_and(frame2, frame2, mask=mask2)
        
        # Get bounding rectangles
        rect1 = cv2.boundingRect(hull1)
        rect2 = cv2.boundingRect(hull2)
        
        # Extract and resize face regions
        x1, y1, w1, h1 = rect1
        x2, y2, w2, h2 = rect2
        
        face1_crop = frame1[y1:y1+h1, x1:x1+w1]
        face2_crop = frame2[y2:y2+h2, x2:x2+w2]
        
        # Resize faces to match target regions
        if face1_crop.size > 0 and face2_crop.size > 0:
            face1_resized = cv2.resize(face1_crop, (w2, h2))
            face2_resized = cv2.resize(face2_crop, (w1, h1))
            
            # Create result frame
            result = frame1.copy()
            result[y1:y1+h1, x1:x1+w1] = face2_resized
            
            return result
        
        return frame1
    
    def draw_landmarks(self, frame, landmarks):
        """
        Draw facial landmarks on frame.
        
        Args:
            frame: Input image frame
            landmarks: Facial landmarks to draw
            
        Returns:
            Frame with landmarks drawn
        """
        result = frame.copy()
        for (x, y) in landmarks:
            cv2.circle(result, (x, y), 2, (0, 255, 0), -1)
        return result
    
    def apply_filter(self, frame, faces, filter_type='landmarks'):
        """
        Apply various filters to detected faces.
        
        Args:
            frame: Input image frame
            faces: List of detected faces
            filter_type: Type of filter to apply ('landmarks', 'blur', 'pixelate')
            
        Returns:
            Frame with filter applied
        """
        result = frame.copy()
        
        for face in faces:
            landmarks = self.get_landmarks(frame, face)
            
            if filter_type == 'landmarks':
                result = self.draw_landmarks(result, landmarks)
            elif filter_type == 'blur':
                result = self.apply_face_mask(result, landmarks)
            elif filter_type == 'pixelate':
                # Get face region
                x, y, w, h = face.left(), face.top(), face.width(), face.height()
                
                # Only pixelate if face is large enough
                if w >= 15 and h >= 15:
                    face_region = result[y:y+h, x:x+w]
                    
                    # Pixelate
                    if face_region.size > 0:
                        small = cv2.resize(face_region, (w//15, h//15), interpolation=cv2.INTER_LINEAR)
                        pixelated = cv2.resize(small, (w, h), interpolation=cv2.INTER_NEAREST)
                        result[y:y+h, x:x+w] = pixelated
            
            # Draw rectangle around face
            x, y, w, h = face.left(), face.top(), face.width(), face.height()
            cv2.rectangle(result, (x, y), (x+w, y+h), (0, 255, 0), 2)
        
        return result


def main():
    """Main function to run real-time face changer."""
    parser = argparse.ArgumentParser(description='Real-time Face Changer Tool')
    parser.add_argument('--source', type=str, default='0', 
                        help='Video source (0 for webcam, or video file path)')
    parser.add_argument('--filter', type=str, default='landmarks',
                        choices=['landmarks', 'blur', 'pixelate'],
                        help='Filter type to apply')
    parser.add_argument('--save', type=str, default=None,
                        help='Output video file path (optional)')
    
    args = parser.parse_args()
    
    # Initialize face changer
    print("Initializing face changer...")
    face_changer = FaceChanger()
    
    # Open video source - handle both integer (webcam) and string (file) sources
    try:
        source = int(args.source)
    except ValueError:
        source = args.source
    
    cap = cv2.VideoCapture(source)
    if not cap.isOpened():
        print("Error: Could not open video source")
        return
    
    # Get video properties
    width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
    height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
    fps = int(cap.get(cv2.CAP_PROP_FPS))
    
    # Use default FPS if not available (common with webcams)
    if fps <= 0:
        fps = 20
    
    # Initialize video writer if save path is provided
    out = None
    if args.save:
        fourcc = cv2.VideoWriter_fourcc(*'XVID')
        out = cv2.VideoWriter(args.save, fourcc, fps, (width, height))
    
    print("Starting real-time face detection...")
    print("Press 'q' to quit")
    print(f"Press '1' for landmarks, '2' for blur, '3' for pixelate")
    
    current_filter = args.filter
    
    while True:
        ret, frame = cap.read()
        if not ret:
            break
        
        # Detect faces
        faces = face_changer.detect_faces(frame)
        
        # Apply filter
        result = face_changer.apply_filter(frame, faces, current_filter)
        
        # Add text overlay
        cv2.putText(result, f"Filter: {current_filter}", (10, 30),
                    cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
        cv2.putText(result, f"Faces: {len(faces)}", (10, 70),
                    cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
        
        # Save frame if output is specified
        if out:
            out.write(result)
        
        # Display result
        cv2.imshow('Real-time Face Changer', result)
        
        # Handle key presses
        key = cv2.waitKey(1) & 0xFF
        if key == ord('q'):
            break
        elif key == ord('1'):
            current_filter = 'landmarks'
        elif key == ord('2'):
            current_filter = 'blur'
        elif key == ord('3'):
            current_filter = 'pixelate'
    
    # Cleanup
    cap.release()
    if out:
        out.release()
    cv2.destroyAllWindows()
    print("Face changer stopped.")


if __name__ == "__main__":
    main()
