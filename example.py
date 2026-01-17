#!/usr/bin/env python3
"""
Example usage of OBS Tracker
Demonstrates basic setup and usage
"""

from obs_tracker import OBSTracker
import time


def example_basic_tracking():
    """Example: Basic tracking with default settings"""
    print("Example 1: Basic Tracking")
    print("-" * 40)
    
    # Create tracker with default config
    tracker = OBSTracker()
    
    # Connect to OBS
    if tracker.connect():
        print("Connected! Starting tracking for 10 seconds...")
        
        # Start tracking in a separate thread or with a timer
        tracker.tracking_active = True
        start_time = time.time()
        
        try:
            while time.time() - start_time < 10:
                time.sleep(0.1)
                print(".", end="", flush=True)
        except KeyboardInterrupt:
            print("\nInterrupted by user")
        finally:
            tracker.stop_tracking()
            tracker.disconnect()
    else:
        print("Failed to connect to OBS")


def example_custom_config():
    """Example: Tracking with custom configuration"""
    print("\nExample 2: Custom Configuration")
    print("-" * 40)
    
    # Create tracker with custom config file
    tracker = OBSTracker('config.json')
    
    # Modify settings programmatically
    tracker.config['tracking']['zoom_speed'] = 0.2
    tracker.config['tracking']['follow_speed'] = 0.1
    
    print(f"Zoom speed: {tracker.config['tracking']['zoom_speed']}")
    print(f"Follow speed: {tracker.config['tracking']['follow_speed']}")
    
    if tracker.connect():
        print("Connected with custom settings!")
        tracker.disconnect()
    else:
        print("Failed to connect to OBS")


def main():
    """Run examples"""
    print("OBS Tracker - Usage Examples")
    print("=" * 40)
    
    # Run example 1
    example_basic_tracking()
    
    # Run example 2
    example_custom_config()
    
    print("\n" + "=" * 40)
    print("Examples completed!")


if __name__ == "__main__":
    main()
