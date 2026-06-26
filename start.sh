#!/bin/bash

# AI-AGENT Start Script for Mac/Linux

echo ""
echo "========================================"
echo "   Starting AI-AGENT..."
echo "========================================"
echo ""

# Try python3 first, then python
if command -v python3 &> /dev/null; then
    python3 chat.py
elif command -v python &> /dev/null; then
    python chat.py
else
    echo "Oops! Python is not installed."
    echo "Please run setup.sh first!"
    echo ""
fi
