#!/usr/bin/env python3
"""
AI-AGENT Installer - Easy Setup Script
"""

import subprocess
import sys
import os

def print_banner():
    print("""
╔══════════════════════════════════════════════════════════════╗
║                                                              ║
║            🚀 AI-AGENT Easy Installer                        ║
║                                                              ║
╚══════════════════════════════════════════════════════════════╝
    """)

def check_python():
    """Check Python version"""
    print("🔍 Checking Python version...")
    if sys.version_info < (3, 8):
        print("❌ Python 3.8 or higher is required!")
        print(f"   Current version: {sys.version}")
        return False
    print(f"✓ Python {sys.version_info.major}.{sys.version_info.minor} detected")
    return True

def install_requirements():
    """Install required packages"""
    print("\n📦 Installing requirements...")
    try:
        subprocess.check_call([sys.executable, "-m", "pip", "install", "-r", "requirements.txt"])
        print("✓ Requirements installed successfully!")
        return True
    except subprocess.CalledProcessError:
        print("❌ Failed to install requirements")
        return False

def create_shortcut():
    """Create easy run script"""
    print("\n🔗 Creating run script...")
    
    # Create run.py for easy execution
    run_script = '''#!/usr/bin/env python3
"""Quick run script for AI-AGENT"""
import sys
import os
sys.path.insert(0, os.path.dirname(__file__))
from simple import main
if __name__ == "__main__":
    main()
'''
    
    with open("run.py", "w") as f:
        f.write(run_script)
    
    print("✓ Created run.py for easy execution!")
    return True

def main():
    """Main installer function"""
    print_banner()
    
    # Check Python
    if not check_python():
        sys.exit(1)
    
    # Install requirements
    if not install_requirements():
        print("\n⚠️  You may need to install requirements manually:")
        print("   pip install -r requirements.txt")
    
    # Create shortcut
    create_shortcut()
    
    # Success message
    print("""
╔══════════════════════════════════════════════════════════════╗
║                                                              ║
║            ✅ Installation Complete!                          ║
║                                                              ║
╚══════════════════════════════════════════════════════════════╝

🚀 To run AI-AGENT, use one of these commands:

   python simple.py
   python run.py
   python main.py

📖 For more information, see README.md

Enjoy chatting with AI-AGENT! 🤖
    """)

if __name__ == "__main__":
    main()
