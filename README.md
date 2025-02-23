A lightweight Python toolkit to control Broadlink IR devices (RM mini, RM Pro) for home automation. Learn and send IR commands, integrate with Stream Deck, or trigger commands via a local web server. Perfect for automating AC, TV, or other IR-controlled devices.

Features:

    Learn and save IR codes from any remote.

    Send IR commands via CLI or HTTP requests.

    Stream Deck integration for one-click control.

    No cloud dependencies (runs locally).

1. learn_ir.py (Learn IR Codes)
2. send_ir.py (Send IR Commands)

## Prerequisites
- Python 3.6+
- Broadlink device (RM mini/RM Pro) connected to your Wi-Fi.
- `broadlink` library: `pip install broadlink`.

## Usage
1. **Learn an IR code**:
   ```bash
   python learn_ir.py ac_power.hex
   
2. **Send an IR code**:
   ```bash
   python send_ir.py ac_power.hex

Stream Deck Integration

    Install the Stream Deck Web Request Plugin.

    Create buttons with the URL http://localhost:5000/ac/<command> (see web_server.py).
