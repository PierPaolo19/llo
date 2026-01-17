-- Face Track Filter Plugin for OBS Studio
-- This filter tracks faces in the video stream and can follow them

obs = obslua

-- Plugin information
source_info = {}
source_info.id = "face_track_filter"
source_info.type = obs.OBS_SOURCE_TYPE_FILTER
source_info.output_flags = bit.bor(obs.OBS_SOURCE_VIDEO)

-- Plugin properties
source_info.get_name = function()
    return "Face Track Filter"
end

-- Default settings
source_info.get_defaults = function(settings)
    obs.obs_data_set_default_string(settings, "detection_method", "haar_cascade")
    obs.obs_data_set_default_double(settings, "confidence_threshold", 0.5)
    obs.obs_data_set_default_bool(settings, "tracking_enabled", true)
    obs.obs_data_set_default_double(settings, "smoothing_factor", 0.7)
    obs.obs_data_set_default_bool(settings, "draw_bounding_box", true)
    obs.obs_data_set_default_int(settings, "box_color", 0x00FF00)
    obs.obs_data_set_default_string(settings, "follow_mode", "center")
end

-- Properties UI
source_info.get_properties = function(data)
    local props = obs.obs_properties_create()
    
    -- Detection method dropdown
    local detection_list = obs.obs_properties_add_list(
        props, "detection_method", "Detection Method",
        obs.OBS_COMBO_TYPE_LIST, obs.OBS_COMBO_FORMAT_STRING
    )
    obs.obs_property_list_add_string(detection_list, "Haar Cascade", "haar_cascade")
    obs.obs_property_list_add_string(detection_list, "DNN", "dnn")
    obs.obs_property_list_add_string(detection_list, "MediaPipe", "mediapipe")
    
    -- Confidence threshold slider
    obs.obs_properties_add_float_slider(
        props, "confidence_threshold", "Confidence Threshold",
        0.0, 1.0, 0.05
    )
    
    -- Tracking enabled checkbox
    obs.obs_properties_add_bool(props, "tracking_enabled", "Enable Tracking")
    
    -- Smoothing factor slider
    obs.obs_properties_add_float_slider(
        props, "smoothing_factor", "Smoothing Factor",
        0.0, 1.0, 0.05
    )
    
    -- Draw bounding box checkbox
    obs.obs_properties_add_bool(props, "draw_bounding_box", "Draw Bounding Box")
    
    -- Box color
    obs.obs_properties_add_color(props, "box_color", "Box Color")
    
    -- Follow mode dropdown
    local follow_list = obs.obs_properties_add_list(
        props, "follow_mode", "Follow Mode",
        obs.OBS_COMBO_TYPE_LIST, obs.OBS_COMBO_FORMAT_STRING
    )
    obs.obs_property_list_add_string(follow_list, "None", "none")
    obs.obs_property_list_add_string(follow_list, "Center", "center")
    obs.obs_property_list_add_string(follow_list, "Zoom", "zoom")
    
    return props
end

-- Update filter settings
source_info.update = function(data, settings)
    data.detection_method = obs.obs_data_get_string(settings, "detection_method")
    data.confidence_threshold = obs.obs_data_get_double(settings, "confidence_threshold")
    data.tracking_enabled = obs.obs_data_get_bool(settings, "tracking_enabled")
    data.smoothing_factor = obs.obs_data_get_double(settings, "smoothing_factor")
    data.draw_bounding_box = obs.obs_data_get_bool(settings, "draw_bounding_box")
    data.box_color = obs.obs_data_get_int(settings, "box_color")
    data.follow_mode = obs.obs_data_get_string(settings, "follow_mode")
end

-- Create filter instance
source_info.create = function(settings, source)
    local data = {}
    data.source = source
    data.faces = {}
    data.last_detection_time = 0
    
    source_info.update(data, settings)
    
    return data
end

-- Destroy filter instance
source_info.destroy = function(data)
    -- Cleanup
end

-- Video render callback
source_info.video_render = function(data, effect)
    -- Pass through the video
    obs.obs_source_process_filter_begin(data.source, obs.GS_RGBA, obs.OBS_NO_DIRECT_RENDERING)
    obs.obs_source_process_filter_end(data.source, effect, 0, 0)
end

-- Video tick callback (for face detection/tracking logic)
source_info.video_tick = function(data, seconds)
    -- This is a framework implementation showing the structure
    -- In a production implementation, this would:
    -- 1. Get the current video frame from OBS
    -- 2. Run face detection algorithm (requires CV library integration)
    -- 3. Update tracked face positions with smoothing
    -- 4. Apply transformations based on follow mode
    -- 5. Render bounding boxes if enabled
    --
    -- Note: Actual face detection requires native plugin integration
    -- with computer vision libraries (OpenCV, MediaPipe, etc.)
end

-- Get video info
source_info.get_width = function(data)
    local target = obs.obs_filter_get_target(data.source)
    if target then
        return obs.obs_source_get_base_width(target)
    end
    return 0
end

source_info.get_height = function(data)
    local target = obs.obs_filter_get_target(data.source)
    if target then
        return obs.obs_source_get_base_height(target)
    end
    return 0
end

-- Register the filter
obs.obs_register_source(source_info)
