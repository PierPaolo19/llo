@echo off
REM Installation script for Windows

echo ================================
echo Face Changer Tools - Setup
echo ================================

REM Check Python version
echo Checking Python version...
python --version

if errorlevel 1 (
    echo Error: Python is not installed or not in PATH
    pause
    exit /b 1
)

REM Ask about virtual environment
echo.
set /p venv="Would you like to create a virtual environment? (recommended) [y/n]: "

if /i "%venv%"=="y" (
    echo Creating virtual environment...
    python -m venv venv
    call venv\Scripts\activate.bat
    echo Virtual environment activated
)

REM Install dependencies
echo.
echo Installing dependencies...
pip install -r requirements.txt

if errorlevel 1 (
    echo Error: Failed to install dependencies
    pause
    exit /b 1
)

REM Download model
echo.
echo Downloading facial landmark model...
python download_model.py

if errorlevel 1 (
    echo Error: Failed to download model
    pause
    exit /b 1
)

REM Run demo
echo.
echo Running setup verification...
python demo.py

echo.
echo ================================
echo Setup complete!
echo ================================
echo.
echo To get started:
echo   1. Activate virtual environment: venv\Scripts\activate.bat
echo   2. Run: python face_changer.py
echo.
pause
