import serial
import pyuarm

ser = serial.Serial('COM18')  # open serial port
#print(ser.name)         # check which port was really used
#ser.open()
x = ser.read(2)
#print(x)
if (x==x):
    print('Open Request Received')
ser.close()

uarm = pyuarm.get_uarm()
uarm.set_position(0,300,170)
uarm.disconnect()
#uarm.dettach()