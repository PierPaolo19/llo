#!/usr/bin/env python3
"""
Utility script to download the shape predictor model for facial landmark detection.
"""

import urllib.request
import bz2
import os
import sys


def download_shape_predictor():
    """Download and extract the shape predictor model."""
    url = "https://github.com/davisking/dlib-models/raw/master/shape_predictor_68_face_landmarks.dat.bz2"
    compressed_file = "shape_predictor_68_face_landmarks.dat.bz2"
    extracted_file = "shape_predictor_68_face_landmarks.dat"
    
    # Check if file already exists
    if os.path.exists(extracted_file):
        print(f"✓ {extracted_file} already exists")
        return True
    
    print("Downloading shape predictor model...")
    print(f"URL: {url}")
    print("This may take a few minutes (file size: ~65 MB)...")
    
    try:
        # Download file
        urllib.request.urlretrieve(url, compressed_file, reporthook=download_progress)
        print("\n✓ Download complete")
        
        # Extract file
        print("Extracting...")
        with bz2.open(compressed_file, 'rb') as src, open(extracted_file, 'wb') as dst:
            dst.write(src.read())
        
        # Remove compressed file
        os.remove(compressed_file)
        
        print(f"✓ Model extracted to {extracted_file}")
        print("✓ Setup complete!")
        return True
        
    except Exception as e:
        print(f"\n✗ Error: {e}")
        print("\nManual download instructions:")
        print(f"1. Download: {url}")
        print(f"2. Extract the .bz2 file")
        print(f"3. Place {extracted_file} in this directory")
        return False


def download_progress(block_num, block_size, total_size):
    """Display download progress."""
    if total_size <= 0:
        # Cannot calculate progress without total size
        downloaded = block_num * block_size
        sys.stdout.write(f"\rDownloaded: {downloaded / 1024 / 1024:.1f} MB")
    else:
        downloaded = block_num * block_size
        percent = min(downloaded * 100.0 / total_size, 100.0)
        sys.stdout.write(f"\rProgress: {percent:.1f}% ({downloaded / 1024 / 1024:.1f} MB)")
    sys.stdout.flush()


if __name__ == "__main__":
    download_shape_predictor()
