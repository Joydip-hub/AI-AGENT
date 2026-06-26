@echo off
title AI-AGENT Installer
color 0A

echo.
echo ========================================
echo    AI-AGENT INSTALLER
echo ========================================
echo.
echo Checking if Python is installed...
echo.

python --version
if errorlevel 1 (
    echo.
    echo Python is NOT installed!
    echo.
    echo Please install Python:
    echo 1. Go to https://www.python.org/downloads/
    echo 2. Download Python
    echo 3. Run installer
    echo 4. CHECK "Add Python to PATH"
    echo 5. Click Install
    echo.
    echo Then run this file again!
    echo.
    pause
    exit
)

echo.
echo Python is installed!
echo.
echo Installing packages...
echo.

pip install colorama
pip install langdetect

echo.
echo ========================================
echo    INSTALLATION COMPLETE!
echo ========================================
echo.
echo Now double-click "START.bat" to chat!
echo.
pause
