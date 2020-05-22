import serial
from UserInput.UseData import *


def readInput():
    ser = serial.Serial('COM4', 9600) #tries to connect to the specified serial port,
                                      #and reads the values in 9600 bits/second.
    state = 0
    lastvalueID = -1

    while True:
        incomingbytes = ser.readline() #reads the specified byte array from the serial port.
        # The length of the expected line, is equal to the reads speed set in the serial.Serial

        incomingbytes = incomingbytes.decode() #decodes the array
        incomingbytes.rstrip() #removes noise and white spaces from the array

        if incomingbytes.find('S') != -1: #if the array holds a character S in it, then:
            incomingbytes = incomingbytes.translate({ord('S'): None}) #remove the S from the array.
            incomingstate = int(incomingbytes) #takes the value and typecast it as an integer.
            if state != incomingstate:
                state = incomingstate #if the state is not the same as the incoming state,
                                      #set state equal to incomingstate


        if incomingbytes.find('F') != -1: #if the array holds a character F in it, then:
            incomingbytes = incomingbytes.translate({ord('F'): None}) #remove the F from the array.
            sensorvalue = int(incomingbytes) #takes the value and typecast it as an integer.
            lastvalueID = soundEffect(lastvalueID, sensorvalue, state) # Run the function lastvalueID and
                                                                       # send the lastvalueID, sensorvalue and state.
                                                                       # The function returns a new lastvalueID
