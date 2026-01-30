# Project Structure

```
llo/
├── README.md                    # Main documentation
├── QUICKSTART.md               # Quick start guide
├── requirements.txt            # Python dependencies
├── .gitignore                  # Git ignore rules
│
├── face_changer.py             # Main real-time face changer tool
├── face_swapper.py             # Face swapping between images
├── download_model.py           # Model download utility
├── demo.py                     # Demo and setup verification
├── test_basic.py               # Basic tests
│
├── setup.sh                    # Linux/macOS setup script
└── setup.bat                   # Windows setup script
```

## File Descriptions

### Core Applications

- **face_changer.py**: Real-time face detection and filtering application
  - Detects faces in video streams
  - Applies various filters (landmarks, blur, pixelate)
  - Supports webcam and video file input
  - Interactive keyboard controls

- **face_swapper.py**: Static image face swapping tool
  - Swaps faces between two images
  - Supports seamless cloning and affine transformation methods
  - Produces high-quality results

### Utilities

- **download_model.py**: Downloads the dlib facial landmark model
  - Automatically downloads and extracts model file
  - Shows progress bar
  - Handles errors gracefully

- **demo.py**: Setup verification and demo script
  - Checks all dependencies
  - Tests webcam access
  - Shows usage examples

- **test_basic.py**: Basic module tests
  - Verifies Python syntax
  - Tests module imports
  - Checks class definitions

### Setup Scripts

- **setup.sh**: Automated setup for Linux/macOS
  - Creates virtual environment (optional)
  - Installs dependencies
  - Downloads model
  - Runs verification

- **setup.bat**: Automated setup for Windows
  - Same functionality as setup.sh
  - Windows-compatible batch script

## Key Features by File

### face_changer.py
- FaceChanger class with methods:
  - `detect_faces()`: Face detection
  - `get_landmarks()`: Landmark extraction
  - `apply_filter()`: Filter application
  - `apply_face_mask()`: Blur effect
  - `draw_landmarks()`: Landmark visualization

### face_swapper.py
- FaceSwapper class with methods:
  - `get_face_landmarks()`: Extract landmarks
  - `extract_face_region()`: Get face mask
  - `seamless_clone()`: Poisson blending
  - `swap_faces_affine()`: Affine transformation

## Dependencies

All dependencies are listed in requirements.txt:
- opencv-python: Core computer vision
- opencv-contrib-python: Additional CV algorithms
- dlib: Face detection and landmarks
- numpy: Numerical operations
- imutils: Image processing utilities

## Model Files

- **shape_predictor_68_face_landmarks.dat**: Facial landmark model
  - Downloaded by download_model.py
  - Required for all face detection operations
  - Size: ~65 MB
  - Source: dlib.net
