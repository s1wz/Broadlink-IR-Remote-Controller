Broadlink IR Controller 

Control your Broadlink IR devices (AC, TV, etc.) via Python scripts, HTTP API, or Stream Deck. Perfect for home automation!

Python Version
License: MIT
Features 

     Learn and save IR codes from any remote

     Send commands via CLI or HTTP API

     Stream Deck integration

     Local web server (no cloud dependencies)

     Auto-device discovery


Requirements 

    Python 3.8+

    Broadlink device (RM mini/RM Pro)

    Broadlink App (for initial setup)

Installation 
bash
Copy

# Clone repository
git clone https://github.com/s1wz/Broadlink-IR-Remote-Controller.git
cd broadlink-ir-controller

# Install dependencies
pip install -r requirements.txt

# Copy and edit environment file
cp .env.example .env

Configuration 

Edit .env:
ini
Copy

# Broadlink Device
BROADLINK_IP=192.168.0.0 # Enter the IP Address of BroadLink

BROADLINK_MAC=a1b2c3d4e5f6 # Enter the Mac Address of Broadlink

BROADLINK_DEVTYPE=0x2712  # RM mini 3

```markdown
## Supported Device Types
```plaintext
| Device Name   | devtype (Hex) | devtype (Decimal) | Description                     |
|---------------|---------------|-------------------|---------------------------------|
| RM mini 3     | 0x2712        | 10002             | Most popular IR controller      |
| RM4 mini      | 0x5F36        | 24374             | Updated RM mini                 |
| RM4 Pro       | 0x51BC        | 20924             | IR + RF support                 |
| RM Pro+       | 0x27C2        | 10178             | Older Pro model                 |
| RM3 mini      | 0x2737        | 10039             |                                 |
| RM3 Pro       | 0x2783        | 10115             |                                 |
| SP1           | 0x2711        | 10001             | Smart plug                      |
| SP2           | 0x2719        | 10009             | Smart plug                      |
| MP1           | 0x4EB5        | 20149             | Multi-outlet power strip        |


```markdown 

# Web Server
PORT=5000
HOST=0.0.0.0

Usage 
1. Learn IR Codes
bash
Copy

python learn_ir.py commands/ac_power.hex

Point your remote at the Broadlink device when prompted
2. Send IR Commands
bash
Copy

python send_ir.py commands/ac_power.hex

3. Start Web Server
bash
Copy

python webserver.py

API Endpoints:

    GET /health - Service status

    GET /command/<cmd> - Send IR command

Stream Deck Integration 

    Install Web Request Plugin

    Create buttons with:
    Copy

    URL: http://localhost:5000/command/power
    Method: GET

    Map commands:
    Button	Command
    Power	/command/power
    Temp+	/command/temp_up

Troubleshooting 
Issue	Solution
"Device not found"	Check Wi-Fi connection
"IR file missing"	Verify .hex file exists in /commands
Connection timeout	Restart webserver.py

Security Note:

    Only expose this server on your local network

    Add authentication if exposing to the internet

    Use HTTPS in production environments
