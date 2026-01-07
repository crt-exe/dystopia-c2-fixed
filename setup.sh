#!/usr/bin/env bash

# Dystopia-C2 Ultimate Setup Script (Verified Fix)
# This script handles permissions, missing DLLs, and inconsistent paths.

set -e

echo "[+] Starting Dystopia-C2 Ultimate Setup..."

# 1. Check for Root (Highly discouraged for Wine, but we'll handle it)
if [ "$EUID" -eq 0 ]; then
    echo "[!] Warning: Running as root. Wine prefers a non-root user."
    USER_HOME="/root"
else
    USER_HOME="$HOME"
fi

# 2. Install System Dependencies
echo "[+] Installing system dependencies..."
if [ -f /etc/debian_version ]; then
    sudo dpkg --add-architecture i386
    sudo apt-get update
    sudo apt-get install -y wine wine32 wine64 libwine libwine:i386 fonts-wine winetricks python3 python3-pip wget
elif [ -f /etc/arch-release ]; then
    sudo pacman -Syu --noconfirm
    sudo pacman -S --noconfirm wine wine-mono wine-gecko winetricks python python-pip wget
fi

# 3. Install Python Requirements for the Builder
echo "[+] Installing Python requirements for the builder..."
pip3 install -r requirements.txt --quiet --break-system-packages || pip3 install -r requirements.txt --quiet

# 4. Initialize Wine Prefix
WINE_DIR="$USER_HOME/.wine"
export WINEPREFIX="$WINE_DIR"
export WINEARCH=win32 # 32-bit is more stable for these tools

if [ ! -d "$WINE_DIR" ]; then
    echo "[+] Initializing 32-bit Wine prefix..."
    wineboot -i
    # Wait for initialization
    sleep 5
fi

# 5. Fix Permissions (Crucial for the 'Permission Denied' error)
echo "[+] Ensuring correct permissions for $WINE_DIR..."
sudo chown -R $(whoami):$(whoami) "$WINE_DIR" || true

# 6. Install MSVC Runtimes (Fixes c0000135 STATUS_DLL_NOT_FOUND)
echo "[+] Installing MSVC runtimes via winetricks..."
# We use -q for quiet mode and handle potential winetricks errors
winetricks -q vcrun2015 || echo "[!] Winetricks failed to install vcrun2015, but continuing..."

# 7. Install Python in Wine
WINE_PYTHON_DIR="C:\\Python38"
WINE_PYTHON_EXE="$WINE_DIR/drive_c/Python38/python.exe"

if [ ! -f "$WINE_PYTHON_EXE" ]; then
    echo "[+] Downloading Python 3.8.10 for Windows (32-bit)..."
    wget -q -O python-3.8.10.exe https://www.python.org/ftp/python/3.8.10/python-3.8.10.exe

    echo "[+] Installing Python in Wine to $WINE_PYTHON_DIR..."
    wine python-3.8.10.exe /quiet InstallAllUsers=1 TargetDir="$WINE_PYTHON_DIR"
    
    # Wait for installation
    echo "[*] Waiting for Python installation to complete..."
    for i in {1..30}; do
        if [ -f "$WINE_PYTHON_EXE" ]; then break; fi
        sleep 2
    done
fi

if [ ! -f "$WINE_PYTHON_EXE" ]; then
    echo "[!] Python installation failed or path is incorrect."
    exit 1
fi

# 8. Install Windows-side Python Dependencies
echo "[+] Installing Windows-side Python dependencies via Wine..."
wine "$WINE_PYTHON_EXE" -m pip install --upgrade pip --quiet
wine "$WINE_PYTHON_EXE" -m pip install pyinstaller==5.3 pillow pyscreeze pyautogui psutil keyboard pywin32 pycryptodome discord_webhook discord.py opencv-python sounddevice scipy pyTelegramBotAPI PyGithub --quiet

echo "[+] Setup Complete!"
echo "[*] You can now run: python3 builder.py"
