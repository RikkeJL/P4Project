from UserInput.UseData import *

import serial
import time

statelock = -1

def readInput():
    ser = serial.Serial('COM3', 9600)
    state = 0
    lastvalueID = -1

    while True:
        incomingbytes = ser.readline()
        incomingbytes = incomingbytes.decode()
        incomingbytes.rstrip()
        print(incomingbytes)

        if incomingbytes.find('S') != -1:
                print("S value found!")
                incomingbytes = incomingbytes.translate({ord('S'): None})
                incomingstate = int(incomingbytes)
                if state == incomingstate:
                    state = int(incomingstate)
                    print("S value is: ", state)
                statelock = state

        if incomingbytes.find('F') != -1:
            print("F value found!")
            incomingbytes = incomingbytes.translate({ord('F'): None})
            print("F value is: ", incomingbytes)
            sensorvalue = float(incomingbytes)
            lastvalueID = soundEffect(lastvalueID, sensorvalue, state)