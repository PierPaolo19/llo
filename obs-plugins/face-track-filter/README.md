# Face Track Filter Plugin

A filter plugin for OBS Studio that tracks faces in video streams and provides various tracking and follow modes.

## Features

- **Face Detection**: Multiple detection methods supported
  - Haar Cascade (Fast, CPU-friendly)
  - DNN (Deep Neural Network, more accurate)
  - MediaPipe (Modern, efficient)

- **Face Tracking**: Smooth tracking of detected faces across frames

- **Visual Feedback**: Optional bounding box overlay with customizable color

- **Follow Modes**:
  - **None**: Only detect and display
  - **Center**: Keep the face centered in the frame
  - **Zoom**: Zoom in on the detected face

## Settings

### Detection Method
Choose the algorithm used for face detection:
- `haar_cascade`: Fast, lightweight method suitable for most cases
- `dnn`: More accurate deep learning-based detection
- `mediapipe`: Modern ML-based detection with good performance

### Confidence Threshold
Minimum confidence level (0.0 - 1.0) required to consider a detection valid. Higher values reduce false positives but may miss some faces.

### Enable Tracking
When enabled, the filter will track faces across frames rather than detecting them independently in each frame.

### Smoothing Factor
Controls how smoothly the camera follows faces (0.0 - 1.0). Higher values result in smoother but slower movement.

### Draw Bounding Box
When enabled, draws a rectangle around detected faces.

### Box Color
Color of the bounding box (when enabled).

### Follow Mode
- `none`: Only detect faces without adjusting the frame
- `center`: Keep the primary face centered in the frame
- `zoom`: Zoom in to keep the face prominent in the frame

## Installation

1. Copy the `face-track-filter` folder to your OBS plugins directory:
   - Windows: `%APPDATA%\obs-studio\plugins\`
   - macOS: `~/Library/Application Support/obs-studio/plugins/`
   - Linux: `~/.config/obs-studio/plugins/`

2. Restart OBS Studio

3. Add the filter to any video source:
   - Right-click on a video source
   - Select "Filters"
   - Click "+" under "Effect Filters"
   - Select "Face Track Filter"

## Requirements

- OBS Studio 27.0.0 or later
- For optimal performance, a dedicated GPU is recommended

## Usage Example

1. Add a video source (e.g., Video Capture Device for webcam)
2. Right-click the source and select "Filters"
3. Add "Face Track Filter" from the Effect Filters
4. Adjust settings based on your needs:
   - For general use: Haar Cascade, 0.5 confidence
   - For accuracy: DNN, 0.7 confidence
   - For performance: MediaPipe, 0.5 confidence

## Technical Notes

The plugin uses Lua scripting capabilities of OBS Studio. The actual face detection would require integration with computer vision libraries (OpenCV, MediaPipe, etc.) through OBS's native plugin interface for optimal performance.

## License

This plugin is part of the llo project.
