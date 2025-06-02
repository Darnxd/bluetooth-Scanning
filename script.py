import bluetooth

def scan_bluetooth_devices():
    print("Scanning for nearby Bluetooth devices...")
    devices = bluetooth.discover_devices(duration=8, lookup_names=True)
    print(f"Found {len(devices)} devices.")
    for addr, name in devices:
        print(f"  {addr} - {name}")

if __name__ == "__main__":
    scan_bluetooth_devices()
