# OBS Zoom and Follow Script

A Python script for OBS Studio that provides automatic zoom and follow functionality. This script allows you to smoothly zoom in on and track a specific source within your OBS scenes, perfect for presentations, live streams, or recordings where you want to focus on specific content.

## Features

- 🔍 **Automatic Zoom**: Smoothly zoom in on selected sources
- 🎯 **Smart Follow**: Track and follow target sources automatically  
- ⚙️ **Customizable Settings**: Adjust zoom level, follow speed, and update rate
- 🎬 **Smooth Transitions**: Interpolated animations for professional-looking effects
- 🔄 **Easy Reset**: One-click reset to default view
- 💪 **Lightweight**: Minimal performance impact on your streams

## Requirements

- OBS Studio (version 27.0 or later recommended)
- Python 3.6 or higher

## Installation

1. Download or clone this repository
2. Open OBS Studio
3. Navigate to **Tools** > **Scripts**
4. Click the **"+"** button (Add Scripts)
5. Browse to and select `obs_zoom_follow.py`
6. The script will now appear in your Scripts panel

## Usage

### Basic Setup

1. In the Scripts panel, find "Zoom and Follow Script"
2. Configure the following settings:
   - **Source to Zoom**: Select the source you want to apply zoom effects to (usually your main camera or scene)
   - **Target Source to Follow**: Select the source you want to track (e.g., a window, image, or specific element)
   - **Enable Zoom and Follow**: Check this box to activate the script
   - **Zoom Level**: Adjust how much to zoom (1.0 = no zoom, 3.0 = maximum zoom)
   - **Follow Speed**: Control how quickly the camera follows the target (0.01 = slow, 1.0 = instant)
   - **Update Interval**: Set how often the script updates in milliseconds (16ms ≈ 60 FPS)

3. Click **"Reset Zoom"** button at any time to return to the default view

### Tips for Best Results

- Start with moderate zoom levels (1.5-2.0) and adjust based on your needs
- Lower follow speeds (0.1-0.3) create smoother, more natural movements
- For gaming or fast-action content, increase the follow speed
- For presentations or calm content, use slower follow speeds
- The update interval of 16ms provides smooth 60 FPS tracking

## Configuration Examples

### Presentation Mode
- Zoom Level: 1.5
- Follow Speed: 0.15
- Update Interval: 16ms

### Gaming/Fast Action
- Zoom Level: 1.8
- Follow Speed: 0.5
- Update Interval: 16ms

### Smooth Cinematic
- Zoom Level: 2.0
- Follow Speed: 0.08
- Update Interval: 16ms

## How It Works

The script uses OBS's Python API to:
1. Monitor the position of your target source in real-time
2. Calculate the center point of the target
3. Apply smooth interpolated zoom and position transforms
4. Update the source transform to keep the target centered and zoomed

The interpolation ensures that movements are smooth and professional-looking rather than jarring or sudden.

## Troubleshooting

**Script doesn't appear in OBS:**
- Ensure you have Python 3.6+ installed
- Check that OBS is configured to use Python (Tools > Scripts > Python Settings)

**Zoom not working:**
- Verify that both "Source to Zoom" and "Target Source to Follow" are selected
- Make sure "Enable Zoom and Follow" is checked
- Check that both sources exist in your current scene

**Jerky movement:**
- Increase the follow speed slightly
- Ensure your update interval is set to 16ms for smooth 60 FPS updates
- Check your computer's performance - the script needs CPU cycles to run

**Source moves off-screen:**
- Click "Reset Zoom" to return to default position
- Adjust zoom level to a lower value
- Ensure the target source is visible in your scene

## License

This project is open source and available for free use.

## Contributing

Contributions, issues, and feature requests are welcome! Feel free to check the issues page or submit a pull request.

## Author

Created for the OBS community to enhance streaming and recording capabilities.