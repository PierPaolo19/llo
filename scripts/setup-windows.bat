@echo off
REM Flash USDT - Windows Setup Batch Script
REM This script helps set up the development environment on Windows

echo ===================================
echo Flash USDT - Windows Setup
echo ===================================
echo.

REM Check for Node.js
echo Checking for Node.js...
node --version >nul 2>&1
if %errorlevel% neq 0 (
    echo [ERROR] Node.js not found!
    echo Please install Node.js from https://nodejs.org
    echo.
    pause
    exit /b 1
)

echo [OK] Node.js found
node --version
echo.

REM Check for npm
echo Checking for npm...
npm --version >nul 2>&1
if %errorlevel% neq 0 (
    echo [ERROR] npm not found!
    pause
    exit /b 1
)

echo [OK] npm found
npm --version
echo.

REM Check if we're in the right directory
if not exist "package.json" (
    echo [WARNING] package.json not found
    echo Please navigate to the Flash USDT project directory
    echo.
    pause
    exit /b 1
)

echo [OK] Found package.json
echo.

REM Offer to install dependencies
echo ===================================
echo Ready to install dependencies?
echo ===================================
echo.
set /p install="Install npm dependencies? (Y/N): "

if /i "%install%"=="Y" (
    echo.
    echo Installing dependencies...
    echo This may take several minutes...
    echo.
    
    call npm install
    
    if %errorlevel% equ 0 (
        echo.
        echo [OK] Dependencies installed successfully!
    ) else (
        echo.
        echo [ERROR] Failed to install dependencies
        echo Check the error messages above
        pause
        exit /b 1
    )
)

echo.
echo ===================================
echo Setup Complete!
echo ===================================
echo.
echo Next steps:
echo 1. Run in development mode:
echo    npm run desktop
echo.
echo 2. Build for Windows:
echo    npm run desktop:build
echo.
echo 3. For more info, see docs\WINDOWS.md
echo.
echo Press any key to exit...
pause >nul
