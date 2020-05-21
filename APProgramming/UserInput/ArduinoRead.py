import serial
from UserInput.UseData import *

def readInput():
    ser = serial.Serial('COM4', 9600)
    state = 0
    lastvalueID = -1

    while True:
        incomingbytes = ser.readline()
        incomingbytes = incomingbytes.decode()
        incomingbytes.rstrip()
        print(incomingbytes)

        if incomingbytes.find('S') != -1:
                incomingbytes = incomingbytes.translate({ord('S'): None})
                incomingstate = int(incomingbytes)
                if state != incomingstate:
                    state = incomingstate

        if incomingbytes.find('F') != -1:
            incomingbytes = incomingbytes.translate({ord('F'): None})
            sensorvalue = int(incomingbytes)
            lastvalueID = soundEffect(lastvalueID, sensorvalue, state)
