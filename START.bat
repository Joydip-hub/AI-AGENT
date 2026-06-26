@echo off
title AI-AGENT - Your AI Friend!
color 0B

echo.
echo ========================================
echo    AI-AGENT - Starting...
echo ========================================
echo.

python chat.py

if errorlevel 1 (
    echo.
    echo Something went wrong!
    echo.
    echo Please run INSTALL.bat first!
    echo.
    pause
)
