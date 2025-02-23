"""
Learn and save IR codes using a Broadlink device.
Usage: python learn_ir.py <output_filename.hex>
"""
import broadlink
import sys

def learn_ir_code(output_file):
    # Auto-discover Broadlink device
    devices = broadlink.discover(timeout=5)
    if not devices:
        print("Error: No Broadlink devices found.")
        return

    device = devices[0]
    device.auth()

    try:
        # Enter learning mode
        device.enter_learning()
        input("Point your remote at the Broadlink device and press a button...")

        # Capture IR code
        ir_packet = device.check_data()
        if ir_packet:
            with open(output_file, "w") as f:
                f.write(ir_packet.hex())
            print(f"IR code saved to {output_file}!")
        else:
            print("Error: No IR code received.")

    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python learn_ir.py <output_filename.hex>")
        sys.exit(1)
    learn_ir_code(sys.argv[1])