# bluetooth-Scanning
# 🔍 Bluetooth Scanner

A simple Python script to scan for nearby Bluetooth devices using the `pybluez` library.

🚀 Features

- Scans nearby Bluetooth Classic devices.
- Displays MAC addresses and device names.
- Runs from the command line.



## 🧰 Requirements

- Python 3.x
- `pybluez` library (Bluetooth Classic support)



📦 Installation Guide

 1. 🐍 Create a Virtual Environment (Optional but Recommended)



python -m venv venv

source venv/bin/activate 

# On Windows: venv\Scripts\activate

🧪 Install pybluez
pip install pybluez

🐧 Linux (Ubuntu/Debian)
sudo apt update
sudo apt install bluetooth libbluetooth-dev python3-dev

pip install pybluez

sudo python bluetooth_scanner.py

🪟 Windows
pip install pybluez

Sample Output:

Scanning for Bluetooth devices...
Found 2 devices.
  00:1A:7D:DA:71:13 - Bluetooth Speaker
  78:02:B7:AE:44:11 - Wireless Headphones


