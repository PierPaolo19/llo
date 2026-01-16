# Example Configurations for OBS Zoom and Follow Script

This directory contains example configuration scenarios for different use cases.

## How to Use These Examples

Each example below shows recommended settings for specific scenarios. To use them:

1. Open OBS Studio
2. Load the zoom and follow script (Tools > Scripts)
3. Apply the settings from the example that matches your use case
4. Fine-tune based on your specific needs

## Examples

### 1. Presentation Mode
**Scenario**: You're giving a presentation and want to smoothly follow your slides

```
Source to Zoom: PowerPoint Window Capture
Target Source to Follow: Slide Focus Point (invisible marker)
Enable Zoom and Follow: ✓
Zoom Level: 1.5
Follow Speed: 0.15
Update Interval: 16
```

**Description**: Gentle zoom with moderate follow speed creates a professional presentation look without being distracting.

---

### 2. Software Tutorial
**Scenario**: Recording a software tutorial where you want viewers to focus on specific UI elements

```
Source to Zoom: Display Capture
Target Source to Follow: Application Window
Enable Zoom and Follow: ✓
Zoom Level: 1.6
Follow Speed: 0.2
Update Interval: 16
```

**Description**: Slightly faster follow speed keeps up with cursor movements and window switches.

---

### 3. Gaming Stream - Face Cam
**Scenario**: Gaming stream with webcam reaction overlay

```
Source to Zoom: Webcam
Target Source to Follow: Webcam Center Point
Enable Zoom and Follow: ✓
Zoom Level: 1.4
Follow Speed: 0.3
Update Interval: 16
```

**Description**: Quick reactions with moderate zoom to capture facial expressions during gameplay.

---

### 4. Product Review/Unboxing
**Scenario**: Showcasing products with cinematic zoom effects

```
Source to Zoom: Main Camera
Target Source to Follow: Product Marker
Enable Zoom and Follow: ✓
Zoom Level: 2.2
Follow Speed: 0.08
Update Interval: 16
```

**Description**: Slow, cinematic movement with strong zoom for detailed product views.

---

### 5. Music Performance
**Scenario**: Live music performance with camera following the performer

```
Source to Zoom: Camera 1
Target Source to Follow: Stage Position Marker
Enable Zoom and Follow: ✓
Zoom Level: 1.7
Follow Speed: 0.12
Update Interval: 16
```

**Description**: Natural movement that follows the performer without being jarring.

---

### 6. Cooking Show
**Scenario**: Cooking demonstration focusing on ingredients and preparation

```
Source to Zoom: Overhead Camera
Target Source to Follow: Prep Area Marker
Enable Zoom and Follow: ✓
Zoom Level: 2.0
Follow Speed: 0.1
Update Interval: 16
```

**Description**: Smooth zoom to show details while maintaining stability for viewers.

---

### 7. Art/Drawing Stream
**Scenario**: Digital art creation with focus on canvas area

```
Source to Zoom: Screen Capture
Target Source to Follow: Canvas Center
Enable Zoom and Follow: ✓
Zoom Level: 1.8
Follow Speed: 0.15
Update Interval: 16
```

**Description**: Balanced settings to follow artistic work without rapid movements.

---

### 8. Interview Setup
**Scenario**: Two-person interview where camera focuses on the speaker

```
Source to Zoom: Wide Camera
Target Source to Follow: Speaker Marker (switch between guests)
Enable Zoom and Follow: ✓
Zoom Level: 1.6
Follow Speed: 0.18
Update Interval: 16
```

**Description**: Moderate zoom and speed for natural conversation flow.

---

### 9. Fitness/Workout Stream
**Scenario**: Exercise demonstration with full-body visibility

```
Source to Zoom: Main Camera
Target Source to Follow: Exercise Zone
Enable Zoom and Follow: ✓
Zoom Level: 1.3
Follow Speed: 0.25
Update Interval: 16
```

**Description**: Minimal zoom to keep full body visible, faster follow for movement.

---

### 10. Podcast Recording
**Scenario**: Podcast with minimal movement, emphasis on speakers

```
Source to Zoom: Studio Camera
Target Source to Follow: Active Speaker Marker
Enable Zoom and Follow: ✓
Zoom Level: 1.5
Follow Speed: 0.06
Update Interval: 33
```

**Description**: Slow, subtle movements with lower update rate for relaxed atmosphere.

---

## Creating Custom Configurations

### Step 1: Identify Your Use Case
- What are you streaming/recording?
- How much movement will there be?
- Do you want subtle or dramatic effects?

### Step 2: Start with a Base Example
- Choose the example above that's closest to your needs
- Apply those settings as a starting point

### Step 3: Fine-Tune
- **Too fast?** Lower Follow Speed by 0.05
- **Too slow?** Increase Follow Speed by 0.05
- **Want more detail?** Increase Zoom Level by 0.2
- **Too zoomed?** Decrease Zoom Level by 0.2
- **Performance issues?** Increase Update Interval

### Step 4: Test and Adjust
- Record a test clip
- Watch it back
- Make small adjustments
- Repeat until satisfied

## Pro Tips

1. **Layer Your Zooms**: Use different zoom levels for different scenes to add variety
2. **Match Your Content**: Fast-paced content needs faster follow speeds
3. **Consider Your Audience**: Subtle effects are less tiring to watch over long periods
4. **Save Your Settings**: Document your favorite configurations for different scenarios
5. **Update Interval Sweet Spot**: 16ms for smooth motion, 33ms for performance balance

## Troubleshooting Common Issues

**Problem**: Zoom is too aggressive
- **Solution**: Reduce Zoom Level by 0.3-0.5

**Problem**: Movement is jerky
- **Solution**: Decrease Follow Speed or ensure Update Interval is at 16ms

**Problem**: Can't keep up with fast action
- **Solution**: Increase Follow Speed to 0.3-0.5

**Problem**: Too much CPU usage
- **Solution**: Increase Update Interval to 33ms or 50ms

**Problem**: Source drifts off screen
- **Solution**: Click Reset Zoom button, check that target source is properly positioned

## Advanced: Scene-Specific Settings

For advanced users wanting different settings per scene:

1. Make copies of the script file: `zoom_preset_1.py`, `zoom_preset_2.py`, etc.
2. Load multiple script instances in OBS
3. Configure each with different settings
4. Enable/disable the appropriate script for each scene

This allows you to have:
- Close-up preset (Zoom: 2.5)
- Medium preset (Zoom: 1.7)
- Wide preset (Zoom: 1.2)

---

**Have a configuration that works great?** Share it with the community!
