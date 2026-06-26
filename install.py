#!/usr/bin/env python3
"""
AI-AGENT Installer - Double Click to Install!
Works on Windows, Mac, and Linux
"""

import subprocess
import sys
import os
import platform

def print_banner():
    print("""
╔══════════════════════════════════════════════════════════════╗
║                                                              ║
║            AI-AGENT - Super Easy Installer!                  ║
║                                                              ║
╚══════════════════════════════════════════════════════════════╝
    """)

def check_python():
    """Check Python version"""
    print("[*] Checking Python version...")
    version = sys.version_info
    if version.major < 3 or (version.major == 3 and version.minor < 8):
        print(f"[X] Python 3.8+ required. You have {version.major}.{version.minor}")
        print("    Please download Python from: https://www.python.org/downloads/")
        return False
    print(f"[OK] Python {version.major}.{version.minor}.{version.micro} found!")
    return True

def install_package(package):
    """Install a single package"""
    try:
        subprocess.check_call(
            [sys.executable, "-m", "pip", "install", package, "--quiet", "--disable-pip-version-check"],
            stdout=subprocess.DEVNULL,
            stderr=subprocess.DEVNULL
        )
        return True
    except:
        try:
            subprocess.check_call(
                [sys.executable, "-m", "pip", "install", package, "--user", "--quiet"],
                stdout=subprocess.DEVNULL,
                stderr=subprocess.DEVNULL
            )
            return True
        except:
            return False

def install_requirements():
    """Install required packages"""
    print("\n[*] Installing packages...")
    
    packages = ["colorama", "langdetect"]
    success = 0
    
    for pkg in packages:
        print(f"    Installing {pkg}...", end=" ")
        if install_package(pkg):
            print("OK")
            success += 1
        else:
            print("SKIP (optional)")
    
    print(f"\n[OK] {success}/{len(packages)} packages installed!")
    return True

def create_shortcuts():
    """Create shortcut scripts"""
    print("\n[*] Creating shortcuts...")
    
    # Create run.py for easy execution
    run_content = '''#!/usr/bin/env python3
"""Quick run for AI-AGENT"""
import sys
import os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from chat import main
if __name__ == "__main__":
    main()
'''
    
    try:
        with open("run.py", "w") as f:
            f.write(run_content)
        print("[OK] Created run.py")
    except:
        pass
    
    return True

def main():
    """Main installer"""
    print_banner()
    
    # Check Python
    if not check_python():
        input("\nPress Enter to exit...")
        sys.exit(1)
    
    # Install requirements
    install_requirements()
    
    # Create shortcuts
    create_shortcuts()
    
    # Success!
    print("""
╔══════════════════════════════════════════════════════════════╗
║                                                              ║
║            [OK] INSTALLATION COMPLETE!                       ║
║                                                              ║
╚══════════════════════════════════════════════════════════════╝

    How to start AI-AGENT:
    
    OPTION 1: Double-click "START.bat" (Windows)
    OPTION 2: Double-click "chat.py"
    OPTION 3: Run "python chat.py" in terminal
    OPTION 4: Run "python run.py" in terminal
    
    Enjoy chatting with your AI friend!
    """)
    
    # Ask to start now
    try:
        choice = input("Start chatting now? (y/n): ").strip().lower()
        if choice in ['y', 'yes', '']:
            print("\nStarting AI-AGENT...\n")
            from chat import main as chat_main
            chat_main()
    except:
        pass

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n\nInstallation cancelled.")
    except Exception as e:
        print(f"\nError: {e}")
        input("Press Enter to exit...")
