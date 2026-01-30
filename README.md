# LLO - Real-time Face Changer Tools

A comprehensive Python toolkit for real-time face detection, manipulation, and swapping using OpenCV and dlib.

## Features

- **Real-time Face Detection**: Detect multiple faces in live video streams
- **Facial Landmark Detection**: Identify 68 facial landmarks for precise face analysis
- **Multiple Face Filters**:
  - Landmarks visualization
  - Face blur effect
  - Face pixelation
- **Face Swapping**: Swap faces between images using advanced techniques
- **Video Processing**: Process both live webcam feeds and video files
- **Easy-to-use CLI**: Simple command-line interface for all tools

## Installation

### Prerequisites

- Python 3.7 or higher
- Webcam (for real-time features)

### Setup

1. Clone the repository:
```bash
git clone https://github.com/PierPaolo19/llo.git
cd llo
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Download the facial landmark model:
```bash
python download_model.py
```

This will download the dlib shape predictor model (~65 MB) required for facial landmark detection.

## Usage

### Real-time Face Changer

Run the real-time face changer with your webcam:

```bash
python face_changer.py
```

#### Options:

- `--source`: Video source (default: 0 for webcam, or path to video file)
- `--filter`: Filter type (`landmarks`, `blur`, `pixelate`)
- `--save`: Save output to video file (optional)

#### Examples:

```bash
# Use webcam with landmarks filter
python face_changer.py --filter landmarks

# Process a video file
python face_changer.py --source input_video.mp4 --save output_video.avi

# Use blur filter
python face_changer.py --filter blur
```

#### Keyboard Controls:

- `1`: Switch to landmarks filter
- `2`: Switch to blur filter
- `3`: Switch to pixelate filter
- `q`: Quit

### Face Swapper

Swap faces between two images:

```bash
python face_swapper.py --source source_image.jpg --target target_image.jpg --output result.jpg
```

#### Options:

- `--source`: Source image (face to be transferred)
- `--target`: Target image (destination)
- `--output`: Output image path
- `--method`: Swapping method (`seamless` or `affine`)

#### Examples:

```bash
# Seamless face swap (default)
python face_swapper.py --source face1.jpg --target face2.jpg --output swapped.jpg

# Affine transformation method
python face_swapper.py --source face1.jpg --target face2.jpg --output swapped.jpg --method affine
```

## Technical Details

### Face Detection

- Uses dlib's HOG-based face detector
- Detects multiple faces in real-time
- Efficient performance on modern hardware

### Facial Landmarks

- 68-point facial landmark detection
- Covers eyes, eyebrows, nose, mouth, and jaw line
- Enables precise face manipulation

### Face Swapping Techniques

1. **Seamless Cloning**: Uses Poisson blending for natural-looking results
2. **Affine Transformation**: Triangle-based warping for accurate face alignment

## Architecture

```
llo/
├── face_changer.py      # Real-time face detection and filtering
├── face_swapper.py      # Face swapping between images
├── download_model.py    # Model download utility
├── requirements.txt     # Python dependencies
└── README.md           # This file
```

## Troubleshooting

### Model Not Found Error

If you get an error about `shape_predictor_68_face_landmarks.dat`:

1. Run `python download_model.py` to download automatically
2. Or manually download from: https://github.com/davisking/dlib-models/raw/master/shape_predictor_68_face_landmarks.dat.bz2
3. Extract and place in the project directory

### Webcam Not Working

- Ensure no other application is using the webcam
- Try different source indices: `--source 1` or `--source 2`
- Check webcam permissions on your system

### Performance Issues

- Close other applications to free up resources
- Reduce video resolution
- Use a more powerful computer for real-time processing

## Dependencies

- **OpenCV**: Computer vision and image processing
- **dlib**: Face detection and landmark detection
- **NumPy**: Numerical operations
- **imutils**: Image processing utilities

## Performance

- Real-time processing at 15-30 FPS on modern hardware
- Supports HD video streams (720p/1080p)
- Efficient face detection and landmark extraction

## Contributing

Contributions are welcome! Please feel free to submit pull requests or open issues.

## License

This project is open source and available under the MIT License.

## Acknowledgments

- dlib library by Davis King
- OpenCV community
- Face landmark model from dlib

## Future Enhancements

- [ ] Multiple face swapping in single frame
- [ ] Real-time face swapping from webcam
- [ ] 3D face modeling
- [ ] Expression transfer
- [ ] Age/gender transformation filters
- [ ] GPU acceleration support
- [ ] Mobile app version

## Contact

For questions or support, please open an issue on GitHub.