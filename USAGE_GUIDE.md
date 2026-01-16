# OBS Zoom and Follow Script - Usage Guide

## Table of Contents
1. [Quick Start](#quick-start)
2. [Understanding the Settings](#understanding-the-settings)
3. [Common Use Cases](#common-use-cases)
4. [Advanced Techniques](#advanced-techniques)
5. [Performance Optimization](#performance-optimization)
6. [Frequently Asked Questions](#frequently-asked-questions)

## Quick Start

### 5-Minute Setup

1. **Install the Script**
   - Open OBS Studio
   - Go to Tools → Scripts
   - Click "+" and select `obs_zoom_follow.py`

2. **Configure Basic Settings**
   - Source to Zoom: Select your camera or main video source
   - Target Source to Follow: Select the element you want to track
   - Enable Zoom and Follow: ✓ Check this box
   - Zoom Level: 1.5 (recommended starting point)
   - Follow Speed: 0.1 (smooth and natural)

3. **Test It Out**
   - Move your target source around the scene
   - Watch as the camera smoothly follows and zooms
   - Adjust settings to your preference

## Understanding the Settings

### Source to Zoom
This is the source that will have the zoom effect applied to it. Typically:
- Your webcam/camera source
- A scene that contains your camera
- A display capture you want to zoom into

**Important**: This source should be large enough to accommodate zooming. If it's too small, zooming may reveal black borders.

### Target Source to Follow
This is what the zoom will track and follow. Examples:
- A window capture (for software demos)
- An image or logo
- A browser source
- Another scene element
- Even text sources

**Pro Tip**: You can use an invisible/transparent source positioned where you want the camera to focus.

### Enable Zoom and Follow
Simple on/off switch. Uncheck to pause the effect without losing your settings.

**Use Case**: Toggle off during scene transitions or when you want manual control.

### Zoom Level (1.0 - 3.0)
Controls the magnification:
- **1.0**: No zoom (normal view)
- **1.5**: Subtle zoom (good for presentations)
- **2.0**: Moderate zoom (great for highlighting details)
- **2.5**: Strong zoom (for specific focus)
- **3.0**: Maximum zoom (very tight focus)

**Recommendation**: Start at 1.5 and adjust up or down based on your content.

### Follow Speed (0.01 - 1.0)
Controls how quickly the camera tracks the target:
- **0.01-0.05**: Very slow, cinematic movement
- **0.06-0.15**: Smooth, natural movement (recommended)
- **0.16-0.30**: Responsive tracking
- **0.31-0.60**: Quick reactions
- **0.61-1.0**: Nearly instant (can be jarring)

**Recommendation**: Use 0.1 for most scenarios. Increase for gaming, decrease for professional presentations.

### Update Interval (16-1000 ms)
How often the script checks and updates position:
- **16ms**: ~60 FPS updates (smoothest, recommended)
- **33ms**: ~30 FPS updates (good balance)
- **50ms**: ~20 FPS updates (lighter on CPU)
- **100ms+**: Noticeable lag but minimal CPU usage

**Recommendation**: Keep at 16ms unless you have performance issues.

## Common Use Cases

### 1. Software Tutorial/Demo
**Goal**: Follow the application window as you work

**Settings**:
- Source to Zoom: Display Capture or Game Capture
- Target: The application window
- Zoom Level: 1.3-1.5
- Follow Speed: 0.15
- Update Interval: 16ms

**Why**: Keeps viewers focused on the active application without manual adjustments.

### 2. Presentation with Slides
**Goal**: Zoom into slides as you present

**Settings**:
- Source to Zoom: PowerPoint/Slides Window
- Target: An image or marker you move around
- Zoom Level: 2.0
- Follow Speed: 0.08
- Update Interval: 16ms

**Why**: Slow, deliberate movements match the pace of presentations.

### 3. Gaming Stream with Face Cam
**Goal**: Keep face cam zoomed on your reactions

**Settings**:
- Source to Zoom: Webcam
- Target: Face detection zone (center of webcam)
- Zoom Level: 1.6
- Follow Speed: 0.3
- Update Interval: 16ms

**Why**: Quick response captures fast reactions during gameplay.

### 4. Product Showcase
**Goal**: Smooth zoom transitions on products

**Settings**:
- Source to Zoom: Camera
- Target: Product position markers
- Zoom Level: 2.5
- Follow Speed: 0.05
- Update Interval: 16ms

**Why**: Slow, controlled zooms give a professional look.

### 5. Music Performance
**Goal**: Follow instrument or performer

**Settings**:
- Source to Zoom: Main Camera
- Target: Performer's position
- Zoom Level: 1.8
- Follow Speed: 0.12
- Update Interval: 16ms

**Why**: Natural movement that doesn't distract from the performance.

## Advanced Techniques

### Creating Focus Zones
1. Add an invisible image source (fully transparent PNG) 
2. Position it where you want focus
3. Set it as the target source
4. Move it around to guide the camera

### Multiple Zoom Presets
Create multiple copies of the script with different settings:
- `zoom_follow_close.py` (Zoom: 2.5, Speed: 0.05)
- `zoom_follow_medium.py` (Zoom: 1.7, Speed: 0.1)
- `zoom_follow_wide.py` (Zoom: 1.2, Speed: 0.15)

Toggle between them based on your scene needs.

### Dynamic Target Switching
Use OBS hotkeys to switch scenes, and configure different targets in each scene. The script will automatically track the new target.

### Smooth Scene Transitions
1. Set Follow Speed to 0.05 before transitioning
2. Switch scenes
3. Gradually increase Follow Speed back to normal
4. Creates a smooth "camera move" effect

## Performance Optimization

### If You Experience Lag:

1. **Increase Update Interval**
   - Change from 16ms to 33ms or 50ms
   - Less frequent updates = less CPU usage

2. **Reduce Follow Speed**
   - Lower values mean less calculations per frame
   - Set to 0.05 or lower

3. **Simplify Your Scene**
   - Fewer sources = better performance
   - Disable the script when not needed

4. **Check OBS Settings**
   - Go to Settings → Output
   - Consider reducing stream/recording quality if OBS is struggling overall

### Best Performance Setup:
- Update Interval: 33ms
- Follow Speed: 0.08
- Close unnecessary browser sources
- Use Game Capture instead of Display Capture when possible

## Frequently Asked Questions

### Q: Can I use this with multiple cameras?
**A**: Yes! Run multiple instances of the script (save copies with different names) or switch the "Source to Zoom" setting when changing scenes.

### Q: Does this work with virtual cameras?
**A**: Yes, as long as the virtual camera appears as a source in OBS, you can zoom it.

### Q: Can I zoom on a group of sources?
**A**: Yes! Create a scene, add all sources to it, then use that scene as your "Source to Zoom."

### Q: The zoom feels too robotic. How do I make it more natural?
**A**: Lower the Follow Speed to 0.08 or less. Natural movements are slower and more gradual.

### Q: Can I animate between different zoom levels?
**A**: Currently, you need to manually change the Zoom Level setting. For complex animations, consider using OBS's built-in Move plugin in combination with this script.

### Q: Does this work with OBS Studio on Mac/Linux?
**A**: Yes! Python scripts work on all platforms where OBS Studio is supported.

### Q: Can I use hotkeys to enable/disable the zoom?
**A**: Currently, you need to toggle it in the Scripts panel. A future version could add hotkey support.

### Q: How do I zoom on a specific point without a target source?
**A**: Create a small colored square source, position it where you want to focus, then set it as the target. You can make it semi-transparent so it's not distracting.

### Q: The position seems off. What's wrong?
**A**: Click the "Reset Zoom" button to recenter everything, then re-enable the effect.

### Q: Can I record the zoom settings per scene?
**A**: Currently, settings are global. For scene-specific zooms, you can run multiple copies of the script with different filenames.

## Getting Help

If you encounter issues:
1. Check that both sources exist in your current scene
2. Verify "Enable Zoom and Follow" is checked
3. Try clicking "Reset Zoom"
4. Restart OBS Studio
5. Check the OBS log file for Python errors

For bugs or feature requests, please open an issue on the GitHub repository.

## Tips for Success

✅ **DO:**
- Start with conservative settings (Zoom: 1.5, Speed: 0.1)
- Test before going live
- Use the Reset button if things go wrong
- Adjust settings gradually

❌ **DON'T:**
- Use extreme zoom levels (3.0+) with low-resolution sources
- Set Follow Speed to 1.0 (creates jarring movements)
- Leave it enabled when switching to scenes without your sources
- Forget to test your scenes after configuring

---

**Happy Streaming!** 🎥✨
