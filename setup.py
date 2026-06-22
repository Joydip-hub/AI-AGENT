"""
Setup and Installation Script for AI-AGENT
"""

import os
import sys

def create_directories():
    """Create necessary directories"""
    directories = [
        'data/conversations',
        'logs',
        'models',
        'cache'
    ]
    
    for directory in directories:
        os.makedirs(directory, exist_ok=True)
        print(f"Created directory: {directory}")

def check_python_version():
    """Check Python version"""
    if sys.version_info < (3, 8):
        print("Error: Python 3.8 or higher is required")
        sys.exit(1)
    print(f"Python version: {sys.version}")

def install_dependencies():
    """Install required dependencies"""
    print("\nInstalling dependencies...")
    print("Run: pip install -r requirements.txt")

def setup_environment():
    """Setup environment files"""
    if not os.path.exists('.env'):
        if os.path.exists('.env.example'):
            print("\nCopying .env.example to .env")
            print("Please edit .env with your API keys")
    
    if not os.path.exists('config/config.yaml'):
        if os.path.exists('config/config.example.yaml'):
            print("\nCopying config.example.yaml to config.yaml")
            print("Please edit config.yaml with your settings")

def main():
    """Main setup function"""
    print("=" * 60)
    print("   AI-AGENT Setup")
    print("=" * 60)
    print()
    
    check_python_version()
    create_directories()
    install_dependencies()
    setup_environment()
    
    print("\n" + "=" * 60)
    print("Setup complete!")
    print("=" * 60)
    print("\nNext steps:")
    print("1. Install dependencies: pip install -r requirements.txt")
    print("2. Copy .env.example to .env and add your API keys")
    print("3. Run the chatbot: python main.py")
    print("   Or simple version: python chat.py")
    print()

if __name__ == "__main__":
    main()
