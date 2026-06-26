@echo off
title AI-AGENT
color 0B

echo.
echo Starting AI-AGENT...
echo.

python chat.py

if errorlevel 1 (
    echo.
    echo Python is not installed or something went wrong!
    echo.
    echo Please install Python from: https://www.python.org/downloads/
    echo Remember to check "Add Python to PATH"!
    echo.
    pause
)
