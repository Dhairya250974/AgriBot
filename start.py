#!/usr/bin/env python3
"""
AgriBot Startup Script
This script helps you start the AgriBot application with proper setup.
"""

import os
import sys
import subprocess
import webbrowser
import time
from pathlib import Path

def check_dependencies():
    """Check if required dependencies are installed"""
    try:
        import flask
        import pandas
        import numpy
        import sklearn
        import requests
        print("✅ All dependencies are installed")
        return True
    except ImportError as e:
        print(f"❌ Missing dependency: {e}")
        print("📦 Installing dependencies...")
        try:
            subprocess.check_call([sys.executable, "-m", "pip", "install", "-r", "requirements.txt"])
            print("✅ Dependencies installed successfully")
            return True
        except subprocess.CalledProcessError:
            print("❌ Failed to install dependencies")
            return False

def start_server():
    """Start the Flask server"""
    print("🚀 Starting AgriBot Server...")
    print("=" * 50)
    
    # Check if server.py exists
    if not os.path.exists("server.py"):
        print("❌ server.py not found in current directory")
        return False
    
    # Start the server
    try:
        print("🌱 AgriBot Server is starting...")
        print("📊 Crop Recommendation: http://127.0.0.1:5050/crop")
        print("🧪 Fertilizer Recommendation: http://127.0.0.1:5050/fertilizer")
        print("❤️ Health Check: http://127.0.0.1:5050/health")
        print("🌐 Frontend: Open index.html in your browser")
        print("=" * 50)
        print("Press Ctrl+C to stop the server")
        
        # Start the Flask app
        os.system("python server.py")
        
    except KeyboardInterrupt:
        print("\n👋 Server stopped by user")
    except Exception as e:
        print(f"❌ Error starting server: {e}")
        return False
    
    return True

def main():
    """Main function"""
    print("🌾 Welcome to AgriBot - Smart Agriculture Assistant")
    print("=" * 50)
    
    # Check if we're in the right directory
    if not os.path.exists("server.py") or not os.path.exists("index.html"):
        print("❌ Please run this script from the AgriBot project directory")
        return
    
    # Check dependencies
    if not check_dependencies():
        print("❌ Please install dependencies manually: pip install -r requirements.txt")
        return
    
    # Start server
    start_server()

if __name__ == "__main__":
    main()
