# OBS Data Files

This directory contains configuration files for OBS Studio plugins and filters.

## Files

### obs-config.json

Main configuration file for OBS Studio with plugin and filter settings.

#### Structure

```json
{
  "version": "1.0.0",
  "name": "OBS Configuration",
  "description": "OBS Studio configuration file for plugins and filters",
  "plugins": [...],
  "settings": {...}
}
```

#### Plugins Section

Lists all available plugins with their configuration:

- `id`: Unique identifier for the plugin
- `name`: Display name
- `version`: Plugin version
- `enabled`: Whether the plugin is active
- `type`: Plugin type (filter, source, etc.)
- `path`: Relative path to the plugin directory

#### Settings Section

Global settings for OBS:

**Video Settings:**
- `base_width`: Base canvas width (default: 1920)
- `base_height`: Base canvas height (default: 1080)
- `output_width`: Output video width (default: 1920)
- `output_height`: Output video height (default: 1080)
- `fps_num`: FPS numerator (default: 30)
- `fps_den`: FPS denominator (default: 1)

**Filter Settings:**

Each filter can have specific settings:

- `face-tracking`:
  - `enabled`: Enable/disable face tracking
  - `detection_confidence`: Minimum confidence for detection (0.0-1.0)
  - `tracking_smoothness`: Smoothing factor for tracking (0.0-1.0)
  - `update_rate_ms`: Update interval in milliseconds

## Usage

This configuration file can be used to:

1. Define global OBS settings
2. Register available plugins
3. Configure filter parameters
4. Set up default values for new installations

## Modifying Configuration

To add a new plugin:

```json
{
  "id": "new-plugin-id",
  "name": "New Plugin Name",
  "version": "1.0.0",
  "enabled": true,
  "type": "filter",
  "path": "../obs-plugins/new-plugin"
}
```

To modify filter settings:

```json
"filters": {
  "new-filter": {
    "enabled": true,
    "custom_setting": "value"
  }
}
```

## Integration

To use this configuration in OBS Studio:

1. Place the file in the OBS data directory
2. Update OBS to read configuration on startup
3. Plugins will be loaded according to the configuration

## Notes

- All paths are relative to the OBS data directory
- Configuration is loaded on OBS Studio startup
- Changes require OBS restart to take effect
