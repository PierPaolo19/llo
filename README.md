# llo

OBS Studio Plugin Collection with Face Tracking Filters

## Overview

This repository contains OBS Studio plugins and configuration files, including a face tracking filter for video streams.

## Contents

### obs-data/

Configuration files for OBS Studio:
- `obs-config.json`: Main configuration file with plugin settings and global OBS settings

See [obs-data/README.md](obs-data/README.md) for detailed documentation.

### obs-plugins/

Plugin implementations:

#### face-track-filter

A video filter plugin that detects and tracks faces in video streams.

**Features:**
- Multiple face detection methods (Haar Cascade, DNN, MediaPipe)
- Smooth face tracking across frames
- Visual feedback with bounding boxes
- Camera follow modes (center, zoom)
- Adjustable confidence thresholds and smoothing

See [obs-plugins/face-track-filter/README.md](obs-plugins/face-track-filter/README.md) for detailed documentation.

## Installation

1. Clone this repository:
   ```bash
   git clone https://github.com/PierPaolo19/llo.git
   ```

2. Copy the plugins to your OBS plugins directory:
   - **Windows**: `%APPDATA%\obs-studio\plugins\`
   - **macOS**: `~/Library/Application Support/obs-studio/plugins/`
   - **Linux**: `~/.config/obs-studio/plugins/`

3. Copy configuration files to your OBS data directory (optional):
   - **Windows**: `%APPDATA%\obs-studio\`
   - **macOS**: `~/Library/Application Support/obs-studio/`
   - **Linux**: `~/.config/obs-studio/`

4. Restart OBS Studio

## Usage

### Face Track Filter

1. Add a video source to your scene (e.g., webcam)
2. Right-click the source and select "Filters"
3. Click "+" under "Effect Filters"
4. Select "Face Track Filter"
5. Configure the settings as desired:
   - Choose detection method
   - Adjust confidence threshold
   - Enable tracking and set smoothness
   - Choose follow mode
   - Customize bounding box appearance

## Requirements

- OBS Studio 27.0.0 or later
- For optimal performance, a dedicated GPU is recommended

## Project Structure

```
llo/
├── obs-data/
│   ├── obs-config.json       # Main OBS configuration
│   └── README.md             # Configuration documentation
├── obs-plugins/
│   └── face-track-filter/
│       ├── face-track-filter.lua   # Main filter implementation
│       ├── plugin.json             # Plugin metadata
│       └── README.md               # Plugin documentation
└── README.md                 # This file
```

## Contributing

Contributions are welcome! Please feel free to submit issues or pull requests.

## License

See LICENSE file for details.