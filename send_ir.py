"""
Send saved IR codes using a Broadlink device.
Usage: python send_ir.py <ir_code.hex>
"""
import broadlink
import sys

def send_ir_code(hex_file):
    # Load IR code
    try:
        with open(hex_file, "r") as f:
            ir_hex = f.read().strip()
    except FileNotFoundError:
        print(f"Error: File '{hex_file}' not found.")
        return

    # Auto-discover Broadlink device
    devices = broadlink.discover(timeout=5)
    if not devices:
        print("Error: No Broadlink devices found.")
        return

    try:
        device = devices[0]
        device.auth()
        device.send_data(bytes.fromhex(ir_hex))
        print(f"Sent IR code from {hex_file}!")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python send_ir.py <ir_code.hex>")
        sys.exit(1)
    send_ir_code(sys.argv[1])