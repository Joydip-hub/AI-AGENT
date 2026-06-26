@echo off
title AI-AGENT - Your AI Friend!
color 0B

echo.
echo ========================================
echo    Starting AI-AGENT...
echo ========================================
echo.

python chat.py

if errorlevel 1 (
    echo.
    echo Oops! Something went wrong.
    echo.
    echo Try running setup.bat first!
    echo.
    pause
)
