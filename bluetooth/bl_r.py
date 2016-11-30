import serial
ser = serial.Serial('COM18')  # open serial port
print(ser.name)         # check which port was really used
#ser.open()
x = ser.read(2)
if (x=='TO'):
    print('Message Received')
ser.close()