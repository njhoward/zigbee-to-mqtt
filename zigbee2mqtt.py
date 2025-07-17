import serial

# Replace this with the actual port if different
port = '/dev/ttyUSB0'
baudrate = 115200  # default for Sonoff Zigbee 3.0 dongle

try:
    with serial.Serial(port, baudrate, timeout=2) as ser:
        print(f"Connected to {port} at {baudrate} baud.")
        ser.write(b'\x00')  # write a dummy byte
        print("Wrote one byte. Waiting for response (if any)...")
        response = ser.read(64)
        print(f"Read {len(response)} bytes: {response.hex()}")
except serial.SerialException as e:
    print(f"Error: {e}")
