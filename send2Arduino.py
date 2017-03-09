"""
Level : Function
Dec : 
Created on : 2017.03.06
Author : Iflier
"""
print(__doc__)

import sys
import time
import serial

flag = True

port = "/dev/ttyACM0"
try:
    arduino = serial.Serial(port, 115200, timeout=5)
    print("Connect to Arduino Succeed!  :)")
except:
    print("Connect to Port {0} failed  :(".format(port))
    sys.exit(1)

while flag:
    try:
        byte_counter = arduino.write("L".encode('utf-8'))

        print("Number of byte(s) write: {0}".format(byte_counter))
        time.sleep(0.01)
        returned = arduino.read()
        # print(returned)
        print("Returned from arduino  {0}".format(returned.decode('utf-8')))
    except KeyboardInterrupt:
        flag = False
arduino.close()
