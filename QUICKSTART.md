# Quick Start Guide

## Getting Started in 3 Steps

### Step 1: Install Dependencies

```bash
pip install -r requirements.txt
```

This installs:
- OpenCV (computer vision)
- dlib (face detection)
- NumPy (numerical computing)
- imutils (image utilities)

### Step 2: Download Face Model

```bash
python download_model.py
```

This downloads the facial landmark detection model (~65 MB).

### Step 3: Run Demo

```bash
python demo.py
```

This verifies your setup and shows usage examples.

## Basic Usage

### Real-time Face Detection

```bash
# Start with your webcam
python face_changer.py

# Try different filters
python face_changer.py --filter blur
python face_changer.py --filter pixelate
```

### Face Swapping

You need two images with faces to swap:

```bash
python face_swapper.py --source face1.jpg --target face2.jpg --output result.jpg
```

## Common Issues

### "No module named cv2"
```bash
pip install opencv-python
```

### "No module named dlib"
```bash
pip install dlib
```

If dlib installation fails:
- **macOS**: `brew install cmake` then retry
- **Linux**: `sudo apt-get install cmake` then retry
- **Windows**: Download pre-built wheels from the official repository or use conda

### "Cannot find shape_predictor_68_face_landmarks.dat"
```bash
python download_model.py
```

### Webcam not working
- Close other apps using the webcam
- Try: `python face_changer.py --source 1`
- Check camera permissions in system settings

## Next Steps

1. **Experiment with filters**: Try all three filter types
2. **Process videos**: Use `--source video.mp4` to process video files
3. **Save output**: Use `--save output.avi` to save results
4. **Face swapping**: Try swapping faces between different images

## Tips for Best Results

- ✓ Use good lighting
- ✓ Face the camera directly
- ✓ Keep face centered in frame
- ✓ Avoid extreme angles
- ✓ Use high-quality images for face swapping

## Need Help?

Open an issue on GitHub: https://github.com/PierPaolo19/llo/issues
