#!/bin/bash

# AI-AGENT Setup Script for Mac/Linux

echo ""
echo "========================================"
echo "   AI-AGENT - Super Easy Setup!"
echo "========================================"
echo ""
echo "This will install everything for you..."
echo ""

# Check if Python is installed
if ! command -v python3 &> /dev/null; then
    if ! command -v python &> /dev/null; then
        echo ""
        echo "Oops! Python is not installed."
        echo ""
        echo "Don't worry! Let me help you install it:"
        echo ""
        echo "For Mac:"
        echo "  1. Open Terminal"
        echo "  2. Type: brew install python3"
        echo "  3. Or go to: https://www.python.org/downloads/"
        echo ""
        echo "For Linux (Ubuntu/Debian):"
        echo "  1. Open Terminal"
        echo "  2. Type: sudo apt update"
        echo "  3. Type: sudo apt install python3 python3-pip"
        echo ""
        echo "After installing Python, run this file again!"
        echo ""
        exit 1
    fi
    PYTHON=python
else
    PYTHON=python3
fi

echo ""
echo "Python is installed! ✓"
echo ""

# Install required packages
echo "Installing packages... (this takes 1 minute)"
echo ""
$PYTHON -m pip install colorama langdetect --quiet 2>/dev/null || pip3 install colorama langdetect --quiet 2>/dev/null

echo ""
echo "========================================"
echo "   Setup Complete! ✓"
echo "========================================"
echo ""
echo "To start chatting, double-click: start.sh"
echo ""
echo "Or type: python3 chat.py"
echo ""
