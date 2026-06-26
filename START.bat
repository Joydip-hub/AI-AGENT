@echo off
setlocal enabledelayedexpansion
title AI-AGENT - Your AI Friend!
color 0B

echo.
echo ========================================
echo    AI-AGENT - Starting...
echo ========================================
echo.

REM Try multiple ways to find Python
set PYTHON_CMD=

python --version >nul 2>&1
if !errorlevel! equ 0 (
    set PYTHON_CMD=python
    goto :start
)

python3 --version >nul 2>&1
if !errorlevel! equ 0 (
    set PYTHON_CMD=python3
    goto :start
)

py --version >nul 2>&1
if !errorlevel! equ 0 (
    set PYTHON_CMD=py
    goto :start
)

REM Python not found
echo.
echo [X] Python is not installed!
echo.
echo Please run "setup.bat" first to install everything.
echo.
echo Or download Python from: https://www.python.org/downloads/
echo Remember to check "Add Python to PATH" during installation!
echo.
pause
exit /b 1

:start
!PYTHON_CMD! chat.py
if !errorlevel! neq 0 (
    echo.
    echo [!] Something went wrong.
    echo Try running "setup.bat" first!
    echo.
    pause
)

endlocal
