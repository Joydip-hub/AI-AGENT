@echo off
title AI-AGENT Setup
color 0A

echo.
echo ========================================
echo    AI-AGENT - Super Easy Setup!
echo ========================================
echo.
echo This will install everything for you...
echo.

REM Check if Python is installed
python --version >nul 2>&1
if errorlevel 1 (
    echo.
    echo Oops! Python is not installed.
    echo.
    echo Don't worry! Let me help you install it:
    echo.
    echo 1. Go to: https://www.python.org/downloads/
    echo 2. Click the big yellow "Download Python" button
    echo 3. Run the installer
    echo 4. IMPORTANT: Check the box that says "Add Python to PATH"
    echo 5. Click "Install Now"
    echo.
    echo After installing Python, run this file again!
    echo.
    pause
    start https://www.python.org/downloads/
    exit
)

echo.
echo Python is installed! ✓
echo.

REM Install required packages
echo Installing packages... (this takes 1 minute)
echo.
pip install colorama langdetect --quiet

echo.
echo ========================================
echo    Setup Complete! ✓
echo ========================================
echo.
echo To start chatting, double-click: START.bat
echo.
echo Or type: python chat.py
echo.
pause
