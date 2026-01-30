#!/usr/bin/env python3
"""
Face swapper utility for swapping faces between two images or videos.
"""

import cv2
import dlib
import numpy as np
import argparse
from imutils import face_utils
import sys


class FaceSwapper:
    """Class for swapping faces between images."""
    
    def __init__(self):
        """Initialize face detector and predictor."""
        self.detector = dlib.get_frontal_face_detector()
        try:
            self.predictor = dlib.shape_predictor("shape_predictor_68_face_landmarks.dat")
        except RuntimeError:
            print("Error: Could not load shape_predictor_68_face_landmarks.dat")
            print("Download from: http://dlib.net/files/shape_predictor_68_face_landmarks.dat.bz2")
            sys.exit(1)
    
    def get_face_landmarks(self, image):
        """Extract facial landmarks from an image."""
        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        faces = self.detector(gray, 1)
        
        if len(faces) == 0:
            return None, None
        
        # Use the first detected face
        face = faces[0]
        shape = self.predictor(gray, face)
        landmarks = face_utils.shape_to_np(shape)
        
        return landmarks, face
    
    def extract_face_region(self, image, landmarks):
        """Extract the triangular mesh of the face."""
        # Get convex hull
        hull = cv2.convexHull(landmarks)
        
        # Get bounding rectangle
        rect = cv2.boundingRect(hull)
        x, y, w, h = rect
        
        # Create mask
        mask = np.zeros(image.shape[:2], dtype=np.uint8)
        cv2.fillConvexPoly(mask, hull, 255)
        
        return mask, rect
    
    def seamless_clone(self, src_img, dst_img, src_landmarks, dst_landmarks):
        """
        Perform seamless face swap using Poisson blending.
        
        Args:
            src_img: Source image (face to transfer)
            dst_img: Destination image (target)
            src_landmarks: Source face landmarks
            dst_landmarks: Destination face landmarks
            
        Returns:
            Result image with swapped face
        """
        # Get face masks and rectangles
        src_mask, src_rect = self.extract_face_region(src_img, src_landmarks)
        dst_mask, dst_rect = self.extract_face_region(dst_img, dst_landmarks)
        
        # Get center of destination face
        dst_center = (dst_rect[0] + dst_rect[2]//2, dst_rect[1] + dst_rect[3]//2)
        
        # Extract source face
        src_face = cv2.bitwise_and(src_img, src_img, mask=src_mask)
        
        # Use seamless cloning
        try:
            result = cv2.seamlessClone(src_face, dst_img, src_mask, dst_center, cv2.NORMAL_CLONE)
            return result
        except Exception as e:
            print(f"Seamless clone failed: {e}")
            return dst_img
    
    def swap_faces_affine(self, src_img, dst_img, src_landmarks, dst_landmarks):
        """
        Swap faces using affine transformation.
        
        Args:
            src_img: Source image
            dst_img: Destination image
            src_landmarks: Source landmarks
            dst_landmarks: Destination landmarks
            
        Returns:
            Image with swapped faces
        """
        # Get convex hulls
        src_hull = cv2.convexHull(src_landmarks)
        dst_hull = cv2.convexHull(dst_landmarks)
        
        # Calculate Delaunay triangulation on destination
        dst_rect = cv2.boundingRect(dst_hull)
        subdiv = cv2.Subdiv2D(dst_rect)
        
        for point in dst_landmarks:
            subdiv.insert((int(point[0]), int(point[1])))
        
        triangles = subdiv.getTriangleList()
        triangles = np.array(triangles, dtype=np.int32)
        
        # Create output image
        output = dst_img.copy()
        
        # For each triangle
        for t in triangles:
            pt1 = (t[0], t[1])
            pt2 = (t[2], t[3])
            pt3 = (t[4], t[5])
            
            # Check if triangle is within destination hull
            if (cv2.pointPolygonTest(dst_hull, pt1, False) >= 0 and
                cv2.pointPolygonTest(dst_hull, pt2, False) >= 0 and
                cv2.pointPolygonTest(dst_hull, pt3, False) >= 0):
                
                # Get corresponding triangle in source
                tri_dst = np.array([pt1, pt2, pt3], dtype=np.float32)
                
                # Find bounding rectangle
                rect = cv2.boundingRect(tri_dst)
                x, y, w, h = rect
                
                # Crop triangle from source and destination
                if x >= 0 and y >= 0 and x+w <= src_img.shape[1] and y+h <= src_img.shape[0]:
                    src_crop = src_img[y:y+h, x:x+w]
                    dst_crop = output[y:y+h, x:x+w]
                    
                    # Create mask for triangle
                    mask = np.zeros((h, w), dtype=np.uint8)
                    tri_crop = tri_dst - np.array([x, y])
                    cv2.fillConvexPoly(mask, tri_crop.astype(np.int32), 255)
                    
                    # Apply mask
                    if src_crop.size > 0 and dst_crop.size > 0:
                        src_crop = cv2.bitwise_and(src_crop, src_crop, mask=mask)
                        dst_crop = cv2.bitwise_and(dst_crop, dst_crop, mask=cv2.bitwise_not(mask))
                        output[y:y+h, x:x+w] = cv2.add(src_crop, dst_crop)
        
        return output


def swap_images(src_path, dst_path, output_path, method='seamless'):
    """
    Swap faces between two images.
    
    Args:
        src_path: Path to source image
        dst_path: Path to destination image
        output_path: Path to save result
        method: Swapping method ('seamless' or 'affine')
    """
    # Load images
    src_img = cv2.imread(src_path)
    dst_img = cv2.imread(dst_path)
    
    if src_img is None or dst_img is None:
        print("Error: Could not load images")
        return
    
    # Initialize face swapper
    swapper = FaceSwapper()
    
    # Get landmarks
    print("Detecting faces...")
    src_landmarks, src_face = swapper.get_face_landmarks(src_img)
    dst_landmarks, dst_face = swapper.get_face_landmarks(dst_img)
    
    if src_landmarks is None or dst_landmarks is None:
        print("Error: Could not detect faces in one or both images")
        return
    
    print("Swapping faces...")
    if method == 'seamless':
        result = swapper.seamless_clone(src_img, dst_img, src_landmarks, dst_landmarks)
    else:
        result = swapper.swap_faces_affine(src_img, dst_img, src_landmarks, dst_landmarks)
    
    # Save result
    cv2.imwrite(output_path, result)
    print(f"Result saved to {output_path}")
    
    # Display result
    cv2.imshow("Source", src_img)
    cv2.imshow("Destination", dst_img)
    cv2.imshow("Result", result)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


def main():
    """Main function."""
    parser = argparse.ArgumentParser(description='Face Swapper Tool')
    parser.add_argument('--source', required=True, help='Source image path')
    parser.add_argument('--target', required=True, help='Target image path')
    parser.add_argument('--output', required=True, help='Output image path')
    parser.add_argument('--method', default='seamless', choices=['seamless', 'affine'],
                        help='Swapping method')
    
    args = parser.parse_args()
    
    swap_images(args.source, args.target, args.output, args.method)


if __name__ == "__main__":
    main()
