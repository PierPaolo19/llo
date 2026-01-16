"""
OBS Zoom and Follow Script

This script provides automatic zoom and follow functionality for OBS Studio.
It allows a camera or other video source to smoothly zoom in and follow
a specified source within your OBS scene.

Requirements:
- OBS Studio (version 27.0 or later recommended)
- Python 3.6+

Installation:
1. Open OBS Studio
2. Go to Tools > Scripts
3. Click the "+" button and select this script
4. Configure the settings in the script properties panel

Features:
- Smooth zoom transitions
- Configurable follow speed
- Adjustable zoom levels
- Enable/disable toggle
"""

import obspython as obs

# Global variables
settings_data = {}
source_name = ""
target_source_name = ""
zoom_enabled = False
zoom_level = 1.5
follow_speed = 0.1
update_interval = 16  # milliseconds (approximately 60 FPS)

# Animation state
current_zoom = 1.0
current_pos_x = 0.0
current_pos_y = 0.0
target_pos_x = 0.0
target_pos_y = 0.0


def script_description():
    """Returns the description of the script shown in OBS"""
    return """<center><h2>Zoom and Follow Script</h2></center>
    <p>Automatically zooms and follows a target source in your scene.</p>
    <p>Select a source to apply zoom effects to, and a target source to follow.</p>
    <p>Adjust zoom level and follow speed to customize the behavior.</p>"""


def script_properties():
    """Defines the properties shown in the Scripts dialog"""
    props = obs.obs_properties_create()
    
    # Add source selection
    source_list = obs.obs_properties_add_list(
        props,
        "source",
        "Source to Zoom:",
        obs.OBS_COMBO_TYPE_EDITABLE,
        obs.OBS_COMBO_FORMAT_STRING
    )
    
    target_list = obs.obs_properties_add_list(
        props,
        "target_source",
        "Target Source to Follow:",
        obs.OBS_COMBO_TYPE_EDITABLE,
        obs.OBS_COMBO_FORMAT_STRING
    )
    
    # Populate source lists
    sources = obs.obs_enum_sources()
    if sources:
        for source in sources:
            source_id = obs.obs_source_get_name(source)
            obs.obs_property_list_add_string(source_list, source_id, source_id)
            obs.obs_property_list_add_string(target_list, source_id, source_id)
        obs.obs_source_list_release(sources)
    
    # Add enable/disable toggle
    obs.obs_properties_add_bool(
        props,
        "zoom_enabled",
        "Enable Zoom and Follow"
    )
    
    # Add zoom level slider
    obs.obs_properties_add_float_slider(
        props,
        "zoom_level",
        "Zoom Level:",
        1.0,
        3.0,
        0.1
    )
    
    # Add follow speed slider
    obs.obs_properties_add_float_slider(
        props,
        "follow_speed",
        "Follow Speed:",
        0.01,
        1.0,
        0.01
    )
    
    # Add update interval
    obs.obs_properties_add_int(
        props,
        "update_interval",
        "Update Interval (ms):",
        16,
        1000,
        1
    )
    
    # Add reset button
    obs.obs_properties_add_button(
        props,
        "reset_button",
        "Reset Zoom",
        reset_zoom
    )
    
    return props


def script_update(settings):
    """Called when the script settings are updated"""
    global source_name, target_source_name, zoom_enabled, zoom_level, follow_speed, update_interval
    
    source_name = obs.obs_data_get_string(settings, "source")
    target_source_name = obs.obs_data_get_string(settings, "target_source")
    zoom_enabled = obs.obs_data_get_bool(settings, "zoom_enabled")
    zoom_level = obs.obs_data_get_double(settings, "zoom_level")
    follow_speed = obs.obs_data_get_double(settings, "follow_speed")
    update_interval = obs.obs_data_get_int(settings, "update_interval")
    
    # Remove existing timer
    obs.timer_remove(update_zoom_and_follow)
    
    # Add timer if enabled
    if zoom_enabled:
        obs.timer_add(update_zoom_and_follow, update_interval)


def script_defaults(settings):
    """Sets default values for the script settings"""
    obs.obs_data_set_default_bool(settings, "zoom_enabled", False)
    obs.obs_data_set_default_double(settings, "zoom_level", 1.5)
    obs.obs_data_set_default_double(settings, "follow_speed", 0.1)
    obs.obs_data_set_default_int(settings, "update_interval", 16)


def script_load(settings):
    """Called when the script is loaded"""
    pass


def script_unload():
    """Called when the script is unloaded"""
    obs.timer_remove(update_zoom_and_follow)


def reset_zoom(props, prop):
    """Reset zoom to default values"""
    global current_zoom, current_pos_x, current_pos_y
    
    current_zoom = 1.0
    current_pos_x = 0.0
    current_pos_y = 0.0
    
    # Apply reset to source
    if source_name:
        source = obs.obs_get_source_by_name(source_name)
        if source:
            scene = obs.obs_frontend_get_current_scene()
            if scene:
                scene_source = obs.obs_scene_from_source(scene)
                if scene_source:
                    scene_item = obs.obs_scene_find_source(scene_source, source_name)
                    if scene_item:
                        # Reset scale
                        scale = obs.vec2()
                        scale.x = 1.0
                        scale.y = 1.0
                        obs.obs_sceneitem_set_scale(scene_item, scale)
                        
                        # Reset position
                        pos = obs.vec2()
                        pos.x = 0.0
                        pos.y = 0.0
                        obs.obs_sceneitem_set_pos(scene_item, pos)
                
                obs.obs_source_release(scene)
            obs.obs_source_release(source)
    
    return True


def lerp(start, end, factor):
    """Linear interpolation between start and end"""
    return start + (end - start) * factor


def update_zoom_and_follow():
    """Main update function called by timer"""
    global current_zoom, current_pos_x, current_pos_y, target_pos_x, target_pos_y
    
    if not zoom_enabled or not source_name or not target_source_name:
        return
    
    # Get current scene
    scene = obs.obs_frontend_get_current_scene()
    if not scene:
        return
    
    scene_source = obs.obs_scene_from_source(scene)
    if not scene_source:
        obs.obs_source_release(scene)
        return
    
    # Get source scene item
    source_item = obs.obs_scene_find_source(scene_source, source_name)
    if not source_item:
        obs.obs_source_release(scene)
        return
    
    # Get target scene item
    target_item = obs.obs_scene_find_source(scene_source, target_source_name)
    if not target_item:
        obs.obs_source_release(scene)
        return
    
    # Get target position
    target_pos = obs.vec2()
    obs.obs_sceneitem_get_pos(target_item, target_pos)
    
    # Get target bounds
    target_bounds = obs.vec2()
    obs.obs_sceneitem_get_bounds(target_item, target_bounds)
    
    # Calculate center of target
    target_center_x = target_pos.x + target_bounds.x / 2
    target_center_y = target_pos.y + target_bounds.y / 2
    
    # Smooth interpolation to target position
    target_pos_x = target_center_x
    target_pos_y = target_center_y
    
    current_pos_x = lerp(current_pos_x, target_pos_x, follow_speed)
    current_pos_y = lerp(current_pos_y, target_pos_y, follow_speed)
    
    # Smooth zoom interpolation
    current_zoom = lerp(current_zoom, zoom_level, follow_speed)
    
    # Get video info for centering
    video_info = obs.obs_video_info()
    obs.obs_get_video_info(video_info)
    canvas_width = video_info.base_width
    canvas_height = video_info.base_height
    
    # Apply scale (zoom)
    scale = obs.vec2()
    scale.x = current_zoom
    scale.y = current_zoom
    obs.obs_sceneitem_set_scale(source_item, scale)
    
    # Calculate position to keep target centered
    # When zoomed, we need to offset to keep the target in view
    pos = obs.vec2()
    obs.obs_sceneitem_get_pos(source_item, pos)
    
    # Apply position offset to follow target
    # This is a simplified follow - adjust based on your needs
    offset_x = (canvas_width / 2 - current_pos_x) * (current_zoom - 1.0)
    offset_y = (canvas_height / 2 - current_pos_y) * (current_zoom - 1.0)
    
    pos.x = offset_x
    pos.y = offset_y
    obs.obs_sceneitem_set_pos(source_item, pos)
    
    # Release scene
    obs.obs_source_release(scene)
