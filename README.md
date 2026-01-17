# OBS Zoom and Follow Object Tracking System

An automated object tracking system for OBS Studio that dynamically adjusts camera zoom and position to follow detected objects in real-time.

## Requirements

- **OBS Studio**: Version 30.0.1 or later recommended
- **Python**: 3.6.8 or later
- **OBS WebSocket Plugin**: Built into OBS Studio 28.0+

## Features

- Real-time object detection and tracking
- Automatic camera zoom adjustment based on object size and distance
- Smooth follow motion for tracked objects
- Configurable tracking parameters
- WebSocket-based communication with OBS Studio

## Installation

1. Clone this repository:
```bash
git clone https://github.com/PierPaolo19/llo.git
cd llo
```

2. Install Python dependencies:
```bash
pip install -r requirements.txt
```

3. Ensure OBS Studio is installed (version 30.0.1 or later)

## Configuration

Edit `config.json` to customize the tracking behavior:

```json
{
  "obs": {
    "host": "localhost",
    "port": 4455,
    "password": ""
  },
  "tracking": {
    "zoom_speed": 0.1,
    "follow_speed": 0.05,
    "min_zoom": 1.0,
    "max_zoom": 5.0,
    "default_zoom": 1.5,
    "position_scale": 100,
    "detection_threshold": 0.5
  },
  "camera": {
    "source_name": "Camera",
    "scene_name": "Main Scene"
  }
}
```

### Configuration Parameters

- **obs.host**: OBS WebSocket server hostname (default: localhost)
- **obs.port**: OBS WebSocket server port (default: 4455)
- **obs.password**: OBS WebSocket server password (if set)
- **tracking.zoom_speed**: Speed of zoom transitions (0.0-1.0)
- **tracking.follow_speed**: Speed of position following (0.0-1.0)
- **tracking.min_zoom**: Minimum zoom level
- **tracking.max_zoom**: Maximum zoom level
- **tracking.default_zoom**: Default zoom for single object tracking
- **tracking.position_scale**: Position movement scaling factor
- **tracking.detection_threshold**: Object detection confidence threshold
- **camera.source_name**: Name of the camera source in OBS
- **camera.scene_name**: Name of the scene containing the camera

## OBS Studio Setup

1. Open OBS Studio (version 30.0.1 or later)
2. Enable WebSocket server:
   - Go to **Tools** → **WebSocket Server Settings**
   - Check "Enable WebSocket server"
   - Note the port number (default: 4455)
   - Set a password if desired
   - Click "Apply" and "OK"

3. Set up your scene:
   - Create or select a scene
   - Add a camera source
   - Note the exact names of your scene and source for the config file

## Usage

Run the tracking system:

```bash
python obs_tracker.py
```

The system will:
1. Connect to OBS Studio via WebSocket
2. Start detecting and tracking objects
3. Automatically adjust camera zoom and position
4. Continue until interrupted with Ctrl+C

## Troubleshooting

### Connection Issues

If you can't connect to OBS:
- Verify OBS Studio is running
- Check WebSocket server is enabled in OBS settings
- Ensure port number matches in config.json
- Verify password (if set) is correct

### Tracking Issues

If tracking isn't working:
- Verify source_name and scene_name in config.json match OBS exactly
- Check that the camera source is visible in the scene
- Adjust detection_threshold for better object detection

## System Requirements

- **Operating System**: Windows 10/11, macOS 10.15+, or Linux
- **RAM**: 4GB minimum, 8GB recommended
- **Processor**: Intel i5 or equivalent
- **Python Version**: 3.6.8 or later

## Dependencies

- `obs-websocket-py`: OBS WebSocket client library
- `opencv-python`: Computer vision and object detection
- `numpy`: Numerical computing support

## License

This project is open source and available under the MIT License.

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## Support

For issues and questions, please open an issue on the GitHub repository.