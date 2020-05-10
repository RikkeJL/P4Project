from UserInput.UseData import *

import serial
import time

def readInput():
    ser = serial.Serial('COM3', 9600)
    state = 0
    errrorhandler = True


    while True:
        incomingbytes = ser.readline()
        incomingbytes = incomingbytes.decode()
        incomingbytes.rstrip()
        print(incomingbytes)

        if incomingbytes.find('S') != -1:
            while errrorhandler:
                print("S value found!")
                incomingbytes = incomingbytes.translate({ord('S'): None})
                incomingstate = incomingbytes
                state = int(incomingstate)
                print("S value is: ", state)
                errrorhandler = False

        if incomingbytes.find('F') != -1:
            print("F value found!")
            incomingbytes = incomingbytes.translate({ord('F'): None})
            print("F value is: ", incomingbytes)
            sensorvalue = float(incomingbytes)
            soundEffect(sensorvalue, state)
