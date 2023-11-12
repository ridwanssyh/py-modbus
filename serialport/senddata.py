import serial
import time

ser = serial.Serial(
    port='COM6',\
    baudrate=115200,\
    parity=serial.PARITY_NONE,\
    stopbits=serial.STOPBITS_ONE,\
    bytesize=serial.EIGHTBITS,\
        timeout=0)

count = 0

while 1:
    ser.write(str.encode('%help'))
    for i in ser.read():
        print(i)
    count +=1