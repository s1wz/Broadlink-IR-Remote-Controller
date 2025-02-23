"""
Broadlink HTTP Server
Expose Broadlink IR commands as RESTful API endpoints for integration with Stream Deck/web requests.
"""

from flask import Flask, jsonify
import broadlink
import threading
import os
from dotenv import load_dotenv  # Optional for .env support

# Load environment variables (create a .env file)
load_dotenv()

app = Flask(__name__)

# Configuration (set these in .env or replace with your values)
DEVICE_IP = os.getenv("BROADLINK_IP", "192.168.3.8")
DEVICE_MAC = os.getenv("BROADLINK_MAC", "a043b0705e82")
DEVTYPE = int(os.getenv("BROADLINK_DEVTYPE", "0x2712"), 16)  # RM mini 3
PORT = int(os.getenv("PORT", 5000))

# Command mapping (customize with your HEX files)
COMMAND_MAP = {
    "power": "ac_power.hex",
    "temp_up": "ac_temp_up.hex",
    "temp_down": "ac_temp_down.hex",
    "fan_high": "ac_fan_high.hex"
}

# Global device connection
device = None

def connect_broadlink():
    """Initialize connection to Broadlink device"""
    global device
    try:
        device = broadlink.rm(
            host=(DEVICE_IP, 80),
            mac=bytearray.fromhex(DEVICE_MAC.replace(":", "")),
            devtype=DEVTYPE
        )
        device.auth()
        print(f"Connected to Broadlink device at {DEVICE_IP}")
    except Exception as e:
        print(f"Connection failed: {e}")
        device = None

def send_ir_command(hex_file):
    """Send IR command from hex file"""
    if not device:
        return False, "Device not connected"
    
    try:
        with open(hex_file, "r") as f:
            ir_hex = f.read().strip()
        device.send_data(bytes.fromhex(ir_hex))
        return True, None
    except FileNotFoundError:
        return False, f"IR file {hex_file} not found"
    except Exception as e:
        return False, str(e)

@app.route('/health', methods=['GET'])
def health_check():
    """Service health check"""
    return jsonify({"status": "ok", "connected": device is not None})

@app.route('/command/<cmd>', methods=['GET'])
def handle_command(cmd):
    """Handle IR command request"""
    if cmd not in COMMAND_MAP:
        return jsonify({"status": "error", "message": "Invalid command"}), 400
    
    hex_file = COMMAND_MAP[cmd]
    success, error = send_ir_command(hex_file)
    
    if success:
        return jsonify({"status": "success", "command": cmd})
    return jsonify({"status": "error", "message": error}), 500

def run_server():
    """Run Flask server in production mode"""
    from waitress import serve
    serve(app, host="0.0.0.0", port=PORT)

if __name__ == '__main__':
    # Initial connection attempt
    connect_broadlink()
    
    # Auto-reconnect thread
    if not device:
        print("Attempting device discovery...")
        devices = broadlink.discover(timeout=5)
        if devices:
            device = devices[0]
            device.auth()
    
    # Start server
    print(f"Starting server on port {PORT}")
    run_server()