#!/usr/bin/env python3
"""
Basic tests for OBS Tracker
Tests configuration loading and basic functionality
"""

import json
import os
import sys
import unittest
from obs_tracker import OBSTracker


class TestOBSTrackerConfig(unittest.TestCase):
    """Test configuration loading"""
    
    def test_load_config_file(self):
        """Test loading configuration from file"""
        tracker = OBSTracker('config.json')
        self.assertIsNotNone(tracker.config)
        self.assertIn('obs', tracker.config)
        self.assertIn('tracking', tracker.config)
        self.assertIn('camera', tracker.config)
    
    def test_default_config(self):
        """Test default configuration when file not found"""
        tracker = OBSTracker('nonexistent_config.json')
        self.assertIsNotNone(tracker.config)
        self.assertEqual(tracker.config['obs']['host'], 'localhost')
        self.assertEqual(tracker.config['obs']['port'], 4455)
    
    def test_config_values(self):
        """Test configuration values are correct types"""
        tracker = OBSTracker('config.json')
        
        # Test OBS config
        self.assertIsInstance(tracker.config['obs']['host'], str)
        self.assertIsInstance(tracker.config['obs']['port'], int)
        self.assertIsInstance(tracker.config['obs']['password'], str)
        
        # Test tracking config
        self.assertIsInstance(tracker.config['tracking']['zoom_speed'], (int, float))
        self.assertIsInstance(tracker.config['tracking']['follow_speed'], (int, float))
        self.assertIsInstance(tracker.config['tracking']['min_zoom'], (int, float))
        self.assertIsInstance(tracker.config['tracking']['max_zoom'], (int, float))
        
        # Test camera config
        self.assertIsInstance(tracker.config['camera']['source_name'], str)
        self.assertIsInstance(tracker.config['camera']['scene_name'], str)


class TestOBSTrackerTracking(unittest.TestCase):
    """Test tracking functionality"""
    
    def test_initial_state(self):
        """Test tracker initial state"""
        tracker = OBSTracker()
        self.assertFalse(tracker.tracking_active)
        self.assertEqual(tracker.current_zoom, 1.0)
        self.assertEqual(tracker.current_position, {'x': 0, 'y': 0})
    
    def test_calculate_zoom_single_object(self):
        """Test zoom calculation with single object"""
        tracker = OBSTracker()
        objects = [{'x': 100, 'y': 100, 'size': 10, 'confidence': 1.0}]
        zoom, position = tracker.calculate_zoom_and_position(objects, 1920, 1080)
        
        self.assertIsInstance(zoom, float)
        self.assertIsInstance(position, dict)
        self.assertIn('x', position)
        self.assertIn('y', position)
    
    def test_calculate_zoom_multiple_objects(self):
        """Test zoom calculation with multiple objects"""
        tracker = OBSTracker()
        objects = [
            {'x': 100, 'y': 100, 'size': 10, 'confidence': 1.0},
            {'x': 200, 'y': 200, 'size': 10, 'confidence': 1.0}
        ]
        zoom, position = tracker.calculate_zoom_and_position(objects, 1920, 1080)
        
        self.assertIsInstance(zoom, float)
        self.assertGreaterEqual(zoom, tracker.config['tracking']['min_zoom'])
        self.assertLessEqual(zoom, tracker.config['tracking']['max_zoom'])
    
    def test_calculate_zoom_no_objects(self):
        """Test zoom calculation with no objects"""
        tracker = OBSTracker()
        objects = []
        zoom, position = tracker.calculate_zoom_and_position(objects, 1920, 1080)
        
        # Should return current values when no objects
        self.assertEqual(zoom, tracker.current_zoom)
        self.assertEqual(position, tracker.current_position)


class TestOBSTrackerDetection(unittest.TestCase):
    """Test object detection"""
    
    def test_detect_objects_exists(self):
        """Test that detect_objects method exists and is callable"""
        tracker = OBSTracker()
        self.assertTrue(hasattr(tracker, 'detect_objects'))
        self.assertTrue(callable(tracker.detect_objects))


def run_tests():
    """Run all tests"""
    print("Running OBS Tracker Tests")
    print("=" * 50)
    
    # Create test suite
    loader = unittest.TestLoader()
    suite = unittest.TestSuite()
    
    # Add test cases
    suite.addTests(loader.loadTestsFromTestCase(TestOBSTrackerConfig))
    suite.addTests(loader.loadTestsFromTestCase(TestOBSTrackerTracking))
    suite.addTests(loader.loadTestsFromTestCase(TestOBSTrackerDetection))
    
    # Run tests
    runner = unittest.TextTestRunner(verbosity=2)
    result = runner.run(suite)
    
    # Return exit code
    return 0 if result.wasSuccessful() else 1


if __name__ == '__main__':
    sys.exit(run_tests())
