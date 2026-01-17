# Setup Guide for OBS Zoom and Follow Object Tracking System

## Step-by-Step Installation

### 1. System Requirements Check

Before starting, ensure you have:
- **OBS Studio 30.0.1 or later** installed
- **Python 3.6.8 or later** installed
- Internet connection for downloading dependencies

#### Verify Python Version
```bash
python --version
# or
python3 --version
```

Expected output: `Python 3.6.8` or higher

#### Verify OBS Studio Version
1. Open OBS Studio
2. Go to Help → About
3. Check version is 30.0.1 or later

### 2. Install Python Dependencies

Navigate to the project directory and install required packages:

```bash
cd llo
pip install -r requirements.txt
```

#### Dependencies Installed
- `obs-websocket-py` - OBS WebSocket client
- `opencv-python` - Computer vision library
- `numpy` - Numerical computing

### 3. Configure OBS Studio

#### Enable WebSocket Server
1. Open OBS Studio
2. Click **Tools** in the menu bar
3. Select **WebSocket Server Settings**
4. Check the box "Enable WebSocket server"
5. Note the **Server Port** (default: 4455)
6. (Optional) Set a password for security
7. Click **Apply** then **OK**

#### Set Up Your Scene
1. Create a new scene or select existing scene
2. Add a video capture device (camera):
   - Click **+** under Sources
   - Select **Video Capture Device**
   - Name it (e.g., "Camera")
   - Select your camera
   - Click **OK**
3. Note the exact names:
   - Scene name (e.g., "Main Scene")
   - Source name (e.g., "Camera")

### 4. Configure the Tracker

Edit `config.json` with your OBS settings:

```json
{
  "obs": {
    "host": "localhost",
    "port": 4455,
    "password": "your_password_here"
  },
  "camera": {
    "source_name": "Camera",
    "scene_name": "Main Scene"
  }
}
```

**Important**: Match the `source_name` and `scene_name` exactly as they appear in OBS!

### 5. Test the Connection

Run the example script to test:

```bash
python example.py
```

Expected output:
```
OBS Tracker - Usage Examples
========================================
Example 1: Basic Tracking
----------------------------------------
Connecting to OBS at localhost:4455...
Connected to OBS successfully!
```

### 6. Run the Tracker

Start the tracking system:

```bash
python obs_tracker.py
```

Press **Ctrl+C** to stop tracking.

## Common Issues and Solutions

### Issue: "Failed to connect to OBS"

**Solution:**
1. Verify OBS Studio is running
2. Check WebSocket server is enabled
3. Verify port in config.json matches OBS settings
4. Check password is correct (if set)

### Issue: "ModuleNotFoundError"

**Solution:**
```bash
pip install -r requirements.txt --upgrade
```

### Issue: Python version too old

**Solution:**
Download and install Python 3.6.8 or later from [python.org](https://www.python.org/downloads/)

### Issue: Camera source not found

**Solution:**
1. Open OBS Studio
2. Note exact spelling of scene and source names
3. Update config.json with exact names (case-sensitive)

## Advanced Configuration

### Adjusting Tracking Speed

Edit `config.json`:

```json
"tracking": {
  "zoom_speed": 0.1,      // Lower = slower zoom (0.0-1.0)
  "follow_speed": 0.05,   // Lower = slower follow (0.0-1.0)
  "min_zoom": 1.0,        // Minimum zoom level
  "max_zoom": 5.0         // Maximum zoom level
}
```

### Multiple Camera Setup

For tracking multiple cameras, create separate config files:

```bash
cp config.json config_camera1.json
cp config.json config_camera2.json
```

Run with specific config:
```python
tracker = OBSTracker('config_camera1.json')
```

## Next Steps

1. Experiment with tracking parameters
2. Test with different objects and lighting
3. Adjust detection threshold for your use case
4. Integrate with your streaming setup

## Getting Help

If you encounter issues:
1. Check this setup guide
2. Review troubleshooting section in README.md
3. Open an issue on GitHub with details
