#!/usr/bin/env python3
"""
Demo script showing various face changer capabilities.
"""

import cv2
import sys
import os


def check_dependencies():
    """Check if all required dependencies are installed."""
    print("Checking dependencies...")
    
    try:
        import cv2
        print("✓ OpenCV installed")
    except ImportError:
        print("✗ OpenCV not found. Install: pip install opencv-python")
        return False
    
    try:
        import dlib
        print("✓ dlib installed")
    except ImportError:
        print("✗ dlib not found. Install: pip install dlib")
        return False
    
    try:
        import numpy
        print("✓ NumPy installed")
    except ImportError:
        print("✗ NumPy not found. Install: pip install numpy")
        return False
    
    try:
        import imutils
        print("✓ imutils installed")
    except ImportError:
        print("✗ imutils not found. Install: pip install imutils")
        return False
    
    # Check for model file
    if not os.path.exists("shape_predictor_68_face_landmarks.dat"):
        print("✗ shape_predictor_68_face_landmarks.dat not found")
        print("  Run: python download_model.py")
        return False
    else:
        print("✓ Facial landmark model found")
    
    return True


def test_webcam():
    """Test if webcam is accessible."""
    print("\nTesting webcam...")
    cap = cv2.VideoCapture(0)
    
    if not cap.isOpened():
        print("✗ Cannot access webcam")
        print("  Possible issues:")
        print("  - Webcam is being used by another application")
        print("  - No webcam connected")
        print("  - Permission denied")
        return False
    
    ret, frame = cap.read()
    cap.release()
    
    if not ret:
        print("✗ Cannot read from webcam")
        return False
    
    print("✓ Webcam is working")
    print(f"  Resolution: {frame.shape[1]}x{frame.shape[0]}")
    return True


def print_usage_examples():
    """Print usage examples."""
    print("\n" + "="*60)
    print("REAL-TIME FACE CHANGER - USAGE EXAMPLES")
    print("="*60)
    
    print("\n1. Real-time face detection with landmarks:")
    print("   python face_changer.py --filter landmarks")
    
    print("\n2. Apply blur filter to faces:")
    print("   python face_changer.py --filter blur")
    
    print("\n3. Pixelate faces for privacy:")
    print("   python face_changer.py --filter pixelate")
    
    print("\n4. Process a video file:")
    print("   python face_changer.py --source input.mp4 --save output.avi")
    
    print("\n5. Swap faces between two images:")
    print("   python face_swapper.py --source face1.jpg --target face2.jpg --output result.jpg")
    
    print("\n" + "="*60)
    print("KEYBOARD CONTROLS (during real-time processing):")
    print("="*60)
    print("  1 - Switch to landmarks filter")
    print("  2 - Switch to blur filter")
    print("  3 - Switch to pixelate filter")
    print("  q - Quit")
    
    print("\n" + "="*60)
    print("TIPS:")
    print("="*60)
    print("  - Ensure good lighting for better face detection")
    print("  - Face the camera directly for optimal results")
    print("  - Keep your face within the camera frame")
    print("  - Close other apps using the webcam")
    print("="*60)


def main():
    """Main demo function."""
    print("="*60)
    print("REAL-TIME FACE CHANGER TOOLS - SETUP CHECK")
    print("="*60)
    
    # Check dependencies
    if not check_dependencies():
        print("\n✗ Setup incomplete. Please install missing dependencies.")
        sys.exit(1)
    
    # Test webcam
    webcam_ok = test_webcam()
    
    if not webcam_ok:
        print("\n⚠ Webcam test failed, but you can still use face swapping with images.")
    
    # Print usage examples
    print_usage_examples()
    
    print("\n✓ Setup check complete!")
    print("\nReady to use face changer tools!")
    print("\nRun 'python face_changer.py' to start real-time face detection")


if __name__ == "__main__":
    main()
