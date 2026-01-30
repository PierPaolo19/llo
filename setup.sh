#!/bin/bash
# Installation script for Linux/macOS

echo "================================"
echo "Face Changer Tools - Setup"
echo "================================"

# Check Python version
echo "Checking Python version..."
python3 --version

if [ $? -ne 0 ]; then
    echo "Error: Python 3 is not installed"
    exit 1
fi

# Create virtual environment (optional but recommended)
echo ""
echo "Would you like to create a virtual environment? (recommended) [y/n]"
read -r response

if [[ "$response" =~ ^([yY][eE][sS]|[yY])$ ]]; then
    echo "Creating virtual environment..."
    python3 -m venv venv
    source venv/bin/activate
    echo "Virtual environment activated"
fi

# Install dependencies
echo ""
echo "Installing dependencies..."
pip install -r requirements.txt

if [ $? -ne 0 ]; then
    echo "Error: Failed to install dependencies"
    exit 1
fi

# Download model
echo ""
echo "Downloading facial landmark model..."
python3 download_model.py

if [ $? -ne 0 ]; then
    echo "Error: Failed to download model"
    exit 1
fi

# Run demo
echo ""
echo "Running setup verification..."
python3 demo.py

echo ""
echo "================================"
echo "Setup complete!"
echo "================================"
echo ""
echo "To get started:"
echo "  1. Activate virtual environment: source venv/bin/activate"
echo "  2. Run: python face_changer.py"
echo ""
