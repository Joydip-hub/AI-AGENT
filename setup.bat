@echo off
setlocal enabledelayedexpansion
title AI-AGENT Installer
color 0A

echo.
echo ========================================
echo    AI-AGENT - Super Easy Installer!
echo ========================================
echo.

REM Try multiple ways to find Python
set PYTHON_CMD=

REM Try python first
python --version >nul 2>&1
if !errorlevel! equ 0 (
    set PYTHON_CMD=python
    goto :found_python
)

REM Try python3
python3 --version >nul 2>&1
if !errorlevel! equ 0 (
    set PYTHON_CMD=python3
    goto :found_python
)

REM Try py (Python Launcher for Windows)
py --version >nul 2>&1
if !errorlevel! equ 0 (
    set PYTHON_CMD=py
    goto :found_python
)

REM Try common Python install paths
for %%P in (
    "%LOCALAPPDATA%\Programs\Python\Python312\python.exe"
    "%LOCALAPPDATA%\Programs\Python\Python311\python.exe"
    "%LOCALAPPDATA%\Programs\Python\Python310\python.exe"
    "%LOCALAPPDATA%\Programs\Python\Python39\python.exe"
    "%ProgramFiles%\Python312\python.exe"
    "%ProgramFiles%\Python311\python.exe"
    "%ProgramFiles%\Python310\python.exe"
    "C:\Python312\python.exe"
    "C:\Python311\python.exe"
    "C:\Python310\python.exe"
) do (
    if exist %%P (
        set PYTHON_CMD=%%P
        goto :found_python
    )
)

REM Python not found - show help
echo.
echo [X] Python is NOT installed on your computer!
echo.
echo Don't worry! Let's install it together:
echo.
echo ----------------------------------------
echo   STEP 1: Download Python
echo ----------------------------------------
echo.
echo   I will open the download page for you.
echo   Look for the BIG YELLOW button that says "Download Python 3.x.x"
echo   Click it to download!
echo.
echo ----------------------------------------
echo   STEP 2: Install Python
echo ----------------------------------------
echo.
echo   1. Open the downloaded file
echo   2. VERY IMPORTANT: Check the box that says:
echo      [X] Add Python 3.x to PATH
echo   3. Click "Install Now"
echo   4. Wait for it to finish
echo   5. Come back here and run this file again!
echo.
echo ----------------------------------------
echo.
echo Press any key to open the Python download page...
pause >nul
start https://www.python.org/downloads/
echo.
echo After installing Python, run this file again!
echo.
pause
exit /b 1

:found_python
echo [OK] Python found: !PYTHON_CMD!
echo.

REM Check pip
echo Checking pip...
!PYTHON_CMD! -m pip --version >nul 2>&1
if !errorlevel! neq 0 (
    echo.
    echo [!] pip is not working. Trying to fix...
    !PYTHON_CMD! -m ensurepip --default-pip >nul 2>&1
    !PYTHON_CMD! -m pip install --upgrade pip >nul 2>&1
)

REM Install packages
echo.
echo [..] Installing packages (takes 30-60 seconds)...
echo.

!PYTHON_CMD! -m pip install colorama --quiet --disable-pip-version-check 2>nul
if !errorlevel! neq 0 (
    echo [!] Trying alternative install method...
    !PYTHON_CMD! -m pip install colorama --user --quiet 2>nul
)

!PYTHON_CMD! -m pip install langdetect --quiet --disable-pip-version-check 2>nul
if !errorlevel! neq 0 (
    echo [!] Trying alternative install method...
    !PYTHON_CMD! -m pip install langdetect --user --quiet 2>nul
)

echo.
echo ========================================
echo    [OK] SETUP COMPLETE!
echo ========================================
echo.
echo    How to start chatting:
echo.
echo    OPTION 1: Double-click "START.bat"
echo    OPTION 2: Double-click "chat.py"
echo    OPTION 3: Open CMD here and type: !PYTHON_CMD! chat.py
echo.
echo ========================================
echo.
echo Press any key to start chatting now...
pause >nul

REM Start the chatbot
!PYTHON_CMD! chat.py

endlocal
