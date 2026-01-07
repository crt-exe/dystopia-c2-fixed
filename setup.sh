#!/usr/bin/env bash

# Dystopia-C2 Setup Script (Fixed Version)
# This script installs dependencies and sets up the Wine environment for building Windows EXEs on Linux.

echo "[+] Starting Dystopia-C2 Setup..."

# 1. Install System Dependencies
if [[ "$OSTYPE" == "linux-gnu"* ]]; then
    if [ -f /etc/debian_version ]; then
        echo "[+] Debian-based system detected."
        sudo dpkg --add-architecture i386
        sudo apt-get update
        sudo apt-get install -y wine wine32 wine64 libwine libwine:i386 fonts-wine python3 python3-pip wget
    elif [ -f /etc/arch-release ]; then
        echo "[+] Arch-based system detected."
        sudo pacman -Syu --noconfirm
        sudo pacman -S --noconfirm wine wine-mono wine-gecko python python-pip wget
    else
        echo "[!] Unsupported Linux distribution. Please install wine, python3, and pip manually."
    fi
fi

# 2. Install Python Requirements for the Builder
echo "[+] Installing Python requirements for the builder..."
pip3 install -r requirements.txt

# 3. Setup Wine Python Environment
WINE_DIR="$HOME/.wine"
WINE_PYTHON_DIR="$WINE_DIR/drive_c/Python38"
WINE_PYTHON_EXE="$WINE_PYTHON_DIR/python.exe"

if [ ! -f "$WINE_PYTHON_EXE" ]; then
    echo "[+] Downloading Python 3.8.10 for Windows..."
    # Using 3.8.10 as it's stable and compatible
    wget -O python-3.8.10.exe https://www.python.org/ftp/python/3.8.10/python-3.8.10.exe

    echo "[+] Installing Python in Wine (this may take a moment)..."
    # Initialize wine prefix if not exists
    wineboot -i
    # Install Python to a fixed path C:\Python38
    wine python-3.8.10.exe /quiet InstallAllUsers=1 TargetDir=C:\\Python38
    
    # Wait for installation to finish (wine processes can be slow)
    sleep 10
fi

# 4. Install Windows-side Python Dependencies
echo "[+] Installing Windows-side Python dependencies via Wine..."
wine "$WINE_PYTHON_EXE" -m pip install --upgrade pip
wine "$WINE_PYTHON_EXE" -m pip install pyinstaller pillow pyscreeze pyautogui psutil keyboard pywin32 pycryptodome discord_webhook discord.py opencv-python sounddevice scipy pyTelegramBotAPI PyGithub

echo "[+] Setup Complete!"
echo "[*] You can now run: python3 builder.py"
