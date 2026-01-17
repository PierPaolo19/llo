#!/usr/bin/env python3
"""
OBS Zoom and Follow Object Tracking System
Tracks objects in OBS scenes and automatically adjusts camera zoom and position
"""

import json
import time
import cv2
import numpy as np
from obswebsocket import obsws, requests, events
import sys


class OBSTracker:
    def __init__(self, config_path='config.json'):
        """Initialize OBS Tracker with configuration"""
        self.load_config(config_path)
        self.ws = None
        self.tracking_active = False
        self.current_zoom = 1.0
        self.current_position = {'x': 0, 'y': 0}
        
    def load_config(self, config_path):
        """Load configuration from JSON file"""
        try:
            with open(config_path, 'r') as f:
                self.config = json.load(f)
        except FileNotFoundError:
            print(f"Config file not found: {config_path}")
            print("Using default configuration")
            self.config = {
                'obs': {'host': 'localhost', 'port': 4455, 'password': ''},
                'tracking': {
                    'zoom_speed': 0.1,
                    'follow_speed': 0.05,
                    'min_zoom': 1.0,
                    'max_zoom': 5.0,
                    'detection_threshold': 0.5
                },
                'camera': {'source_name': 'Camera', 'scene_name': 'Main Scene'}
            }
    
    def connect(self):
        """Connect to OBS WebSocket"""
        try:
            host = self.config['obs']['host']
            port = self.config['obs']['port']
            password = self.config['obs']['password']
            
            print(f"Connecting to OBS at {host}:{port}...")
            self.ws = obsws(host, port, password)
            self.ws.connect()
            print("Connected to OBS successfully!")
            return True
        except Exception as e:
            print(f"Failed to connect to OBS: {e}")
            print("Make sure OBS Studio is running with WebSocket server enabled")
            return False
    
    def disconnect(self):
        """Disconnect from OBS WebSocket"""
        if self.ws:
            self.ws.disconnect()
            print("Disconnected from OBS")
    
    def get_scene_item_transform(self, scene_name, source_name):
        """Get transform properties of a scene item"""
        try:
            response = self.ws.call(requests.GetSceneItemId(
                sceneName=scene_name,
                sourceName=source_name
            ))
            item_id = response.getSceneItemId()
            
            transform = self.ws.call(requests.GetSceneItemTransform(
                sceneName=scene_name,
                sceneItemId=item_id
            ))
            return transform.getSceneItemTransform()
        except Exception as e:
            print(f"Error getting scene item transform: {e}")
            return None
    
    def set_scene_item_transform(self, scene_name, source_name, transform):
        """Set transform properties of a scene item"""
        try:
            response = self.ws.call(requests.GetSceneItemId(
                sceneName=scene_name,
                sourceName=source_name
            ))
            item_id = response.getSceneItemId()
            
            self.ws.call(requests.SetSceneItemTransform(
                sceneName=scene_name,
                sceneItemId=item_id,
                sceneItemTransform=transform
            ))
            return True
        except Exception as e:
            print(f"Error setting scene item transform: {e}")
            return False
    
    def detect_objects(self, frame):
        """
        Detect objects in frame using simple motion detection
        This is a placeholder - can be replaced with more sophisticated detection
        """
        # Convert to grayscale
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        
        # Simple blob detection
        detector = cv2.SimpleBlobDetector_create()
        keypoints = detector.detect(gray)
        
        objects = []
        for kp in keypoints:
            objects.append({
                'x': kp.pt[0],
                'y': kp.pt[1],
                'size': kp.size,
                'confidence': 1.0
            })
        
        return objects
    
    def calculate_zoom_and_position(self, objects, frame_width, frame_height):
        """Calculate optimal zoom and position based on detected objects"""
        if not objects:
            return self.current_zoom, self.current_position
        
        # Find center of all objects
        center_x = sum(obj['x'] for obj in objects) / len(objects)
        center_y = sum(obj['y'] for obj in objects) / len(objects)
        
        # Calculate target position (normalized to -1 to 1)
        target_x = (center_x / frame_width - 0.5) * 2
        target_y = (center_y / frame_height - 0.5) * 2
        
        # Calculate target zoom based on object spread
        if len(objects) > 1:
            max_distance = 0
            for obj in objects:
                distance = ((obj['x'] - center_x) ** 2 + (obj['y'] - center_y) ** 2) ** 0.5
                max_distance = max(max_distance, distance)
            
            # Adjust zoom based on spread
            target_zoom = max(
                self.config['tracking']['min_zoom'],
                min(self.config['tracking']['max_zoom'], 
                    frame_width / (max_distance * 4))
            )
        else:
            target_zoom = 1.5  # Default zoom for single object
        
        # Smooth transition
        zoom_speed = self.config['tracking']['zoom_speed']
        follow_speed = self.config['tracking']['follow_speed']
        
        new_zoom = self.current_zoom + (target_zoom - self.current_zoom) * zoom_speed
        new_position = {
            'x': self.current_position['x'] + (target_x - self.current_position['x']) * follow_speed,
            'y': self.current_position['y'] + (target_y - self.current_position['y']) * follow_speed
        }
        
        return new_zoom, new_position
    
    def apply_transform(self, zoom, position):
        """Apply zoom and position transform to OBS source"""
        scene_name = self.config['camera']['scene_name']
        source_name = self.config['camera']['source_name']
        
        # Get current transform
        current_transform = self.get_scene_item_transform(scene_name, source_name)
        if not current_transform:
            return False
        
        # Update transform with new zoom and position
        new_transform = {
            'scaleX': zoom,
            'scaleY': zoom,
            'positionX': current_transform.get('positionX', 0) + position['x'] * 100,
            'positionY': current_transform.get('positionY', 0) + position['y'] * 100
        }
        
        # Apply transform
        return self.set_scene_item_transform(scene_name, source_name, new_transform)
    
    def start_tracking(self):
        """Start the tracking loop"""
        if not self.ws:
            print("Not connected to OBS. Call connect() first.")
            return
        
        self.tracking_active = True
        print("Starting object tracking...")
        print("Press Ctrl+C to stop")
        
        try:
            while self.tracking_active:
                # In a real implementation, you would capture frames from OBS
                # This is a placeholder that simulates the tracking loop
                time.sleep(0.1)  # Run at ~10 FPS
                
                # Here you would:
                # 1. Capture frame from OBS source
                # 2. Detect objects in frame
                # 3. Calculate zoom and position
                # 4. Apply transform to OBS
                
                print(".", end="", flush=True)
                
        except KeyboardInterrupt:
            print("\nStopping tracking...")
            self.tracking_active = False
    
    def stop_tracking(self):
        """Stop the tracking loop"""
        self.tracking_active = False


def main():
    """Main entry point"""
    print("OBS Zoom and Follow Object Tracking System")
    print("=" * 50)
    
    # Create tracker instance
    tracker = OBSTracker()
    
    # Connect to OBS
    if not tracker.connect():
        print("\nFailed to connect to OBS.")
        print("\nPlease ensure:")
        print("1. OBS Studio (version 30.0.1 or later) is running")
        print("2. WebSocket server is enabled in OBS")
        print("   (Tools -> WebSocket Server Settings)")
        print("3. Configuration in config.json is correct")
        return 1
    
    try:
        # Start tracking
        tracker.start_tracking()
    except Exception as e:
        print(f"\nError during tracking: {e}")
        return 1
    finally:
        # Clean up
        tracker.disconnect()
    
    return 0


if __name__ == "__main__":
    sys.exit(main())
