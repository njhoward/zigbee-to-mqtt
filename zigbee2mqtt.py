import serial

port = '/dev/ttyUSB0'
baudrate = 115200  
duration = 60  # seconds to listen

try:
    with serial.Serial(port, baudrate, timeout=1) as ser:
        print(f"Listening to {port} at {baudrate} baud for {duration} seconds...\n")
        start_time = time.time()
        while time.time() - start_time < duration:
            line = ser.read(128)  # read up to 128 bytes
            if line:
                print(f"[{time.strftime('%H:%M:%S')}] Received: {line.hex()}")
        print("\nDone listening.")
except serial.SerialException as e:
    print(f"Error: {e}")
