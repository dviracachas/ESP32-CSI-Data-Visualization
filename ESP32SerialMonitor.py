import serial

# Open serial port
ser = serial.Serial('COM11', 921600, timeout=1)

# Read data
while True:
    line = ser.readline()   # Read a '\n' terminated line
    try:
        print(line.decode('utf-8').strip())
        
    except:
        print("Serial not readable")

# Close the serial port
ser.close()
