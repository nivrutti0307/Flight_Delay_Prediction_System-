#!/usr/bin/env python3
"""
Flight Delay Predictor - Setup Script
"""

import os
import sys
import subprocess
import platform

def run_command(command):
    """Run a command and return the result"""
    try:
        result = subprocess.run(command, shell=True, check=True, capture_output=True, text=True)
        return True, result.stdout
    except subprocess.CalledProcessError as e:
        return False, e.stderr

def check_python_version():
    """Check if Python version is compatible"""
    version = sys.version_info
    if version.major < 3 or (version.major == 3 and version.minor < 12):
        print("❌ Python 3.12 or higher is required!")
        print(f"Current version: {version.major}.{version.minor}.{version.micro}")
        return False
    print(f"✅ Python {version.major}.{version.minor}.{version.micro} detected")
    return True

def create_virtual_environment():
    """Create virtual environment"""
    print("\n🔧 Creating virtual environment...")
    success, output = run_command("python -m venv venv")
    if success:
        print("✅ Virtual environment created successfully")
        return True
    else:
        print(f"❌ Failed to create virtual environment: {output}")
        return False

def activate_virtual_environment():
    """Activate virtual environment"""
    if platform.system() == "Windows":
        activate_script = "venv\\Scripts\\activate"
    else:
        activate_script = "source venv/bin/activate"
    
    print(f"🔧 Activating virtual environment: {activate_script}")
    return activate_script

def install_dependencies():
    """Install project dependencies"""
    print("\n📦 Installing dependencies...")
    
    # Upgrade pip
    success, output = run_command("python -m pip install --upgrade pip")
    if not success:
        print(f"❌ Failed to upgrade pip: {output}")
        return False
    
    # Install requirements
    success, output = run_command("pip install -r requirements.txt")
    if success:
        print("✅ Dependencies installed successfully")
        return True
    else:
        print(f"❌ Failed to install dependencies: {output}")
        return False

def check_files():
    """Check if required files exist"""
    print("\n📁 Checking required files...")
    
    required_files = [
        "app.py",
        "flight_predictor.py",
        "flight_delay_predictor.pkl",
        "test_data.csv",
        "requirements.txt"
    ]
    
    missing_files = []
    for file in required_files:
        if os.path.exists(file):
            print(f"✅ {file}")
        else:
            print(f"❌ {file} (missing)")
            missing_files.append(file)
    
    if missing_files:
        print(f"\n⚠️  Missing files: {', '.join(missing_files)}")
        return False
    
    return True

def main():
    """Main setup function"""
    print("🚀 Flight Delay Predictor - Setup Script")
    print("=" * 50)
    
    # Check Python version
    if not check_python_version():
        sys.exit(1)
    
    # Check required files
    if not check_files():
        print("\n❌ Setup failed: Missing required files")
        sys.exit(1)
    
    # Create virtual environment
    if not create_virtual_environment():
        sys.exit(1)
    
    # Install dependencies
    if not install_dependencies():
        sys.exit(1)
    
    # Get activation command
    activate_cmd = activate_virtual_environment()
    
    print("\n" + "=" * 50)
    print("✅ Setup completed successfully!")
    print("\n🚀 To run the application:")
    print(f"1. Activate virtual environment: {activate_cmd}")
    print("2. Run the app: streamlit run app.py")
    print("3. Open browser: http://localhost:8501")
    print("\n📚 For more information, see README.md")
    print("🌐 For deployment guide, see docs/deployment-guide.md")

if __name__ == "__main__":
    main() 