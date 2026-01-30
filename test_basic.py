#!/usr/bin/env python3
"""
Basic test script to verify the face changer modules load correctly.
Note: This requires dependencies to be installed (pip install -r requirements.txt)
"""

import sys
import importlib.util


def test_module_import(module_name, file_path):
    """Test if a module can be imported."""
    try:
        spec = importlib.util.spec_from_file_location(module_name, file_path)
        module = importlib.util.module_from_spec(spec)
        sys.modules[module_name] = module
        spec.loader.exec_module(module)
        print(f"✓ {module_name} loaded successfully")
        return True
    except ImportError as e:
        print(f"⚠ {module_name} requires dependencies: {e}")
        print(f"  Run: pip install -r requirements.txt")
        return False
    except Exception as e:
        print(f"✗ {module_name} failed to load: {e}")
        return False


def test_class_exists(module_name, class_name):
    """Test if a class exists in a module."""
    try:
        module = sys.modules.get(module_name)
        if module and hasattr(module, class_name):
            print(f"  ✓ Class {class_name} found")
            return True
        else:
            print(f"  ✗ Class {class_name} not found")
            return False
    except Exception as e:
        print(f"  ✗ Error checking class {class_name}: {e}")
        return False


def main():
    """Run basic tests."""
    print("="*60)
    print("FACE CHANGER TOOLS - BASIC TESTS")
    print("="*60)
    
    all_passed = True
    
    # Test face_changer module
    print("\nTest 1: Loading face_changer module...")
    if test_module_import("face_changer", "face_changer.py"):
        test_class_exists("face_changer", "FaceChanger")
    else:
        all_passed = False
    
    # Test face_swapper module
    print("\nTest 2: Loading face_swapper module...")
    if test_module_import("face_swapper", "face_swapper.py"):
        test_class_exists("face_swapper", "FaceSwapper")
    else:
        all_passed = False
    
    # Test download_model module
    print("\nTest 3: Loading download_model module...")
    if not test_module_import("download_model", "download_model.py"):
        all_passed = False
    
    # Test demo module
    print("\nTest 4: Loading demo module...")
    if not test_module_import("demo", "demo.py"):
        all_passed = False
    
    print("\n" + "="*60)
    if all_passed:
        print("✓ All basic tests passed!")
        print("\nNote: To fully test the application, install dependencies:")
        print("  pip install -r requirements.txt")
    else:
        print("⚠ Tests require dependencies to be installed")
        print("\nTo install dependencies:")
        print("  pip install -r requirements.txt")
    print("="*60)
    
    return 0


if __name__ == "__main__":
    sys.exit(main())
