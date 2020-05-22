from SoundEffects.echo import *
from SoundEffects.vibrato import *
from SoundEffects.frequencyChange import *
from SoundEffects.chorus import *
from graphMethod import *
from UserInput.CollectData import *


import scipy.io.wavfile as wave
import sounddevice as sd
import numpy as np

sf, soundInput = wave.read("A Light Breeze from South West Redux.wav")  # Saves the sampling frequency as sf and loads
# the raw data of the song as an array and saves it to soundInput.
length = np.size(soundInput)  # Gets the length of the song array.
time = np.arange(0, length)  # makes an array from 0 to the length of the song array, with the values 0-length


# ----------- CALCULATIONS FOR FREQUENCY CHANGE ---------#
freqSmall = resampleFreq(soundInput, 2)  # Runs the method for frequency change with small frequency
print("Freq small")  # Prints when the method is done
freqMed = resampleFreq(soundInput, 5)  # Runs the method for frequency change with medium frequency
print("Freq med")  # Prints when the method is done
freqHigh = resampleFreq(soundInput, 10)  # Runs the method for frequency change with high frequency
print("Freq high")  # Prints when the method is done
freqReallyHigh = resampleFreq(soundInput, 15)  # Runs the method for frequency change with very high frequency
print("Freq very high")  # Prints when the method is done


# ------------ FREQUENCY CHANGE GRAPH CALCULATIONS ------------ #
lengthFreqSmall = np.size(freqSmall)  # Gets the length of the freqSmall array.
lengthFreqMed = np.size(freqMed)  # Gets the length of the freqMed array.
lengthFreqHigh = np.size(freqHigh)  # Gets the length of the freqHigh array.
lengthFreqRHigh = np.size(freqReallyHigh)  # Gets the length of the freqReallyHigh array.

timeFreqSmall = np.arange(0, lengthFreqSmall)  # makes an array from 0 to the length of the freqSmall array, with the values 0-length
timeFreqMed = np.arange(0, lengthFreqMed)  # makes an array from 0 to the length of the song freqMed, with the values 0-length
timeFreqHigh = np.arange(0, lengthFreqHigh)  # makes an array from 0 to the length of the song freqHigh, with the values 0-length
timeFreqRHigh = np.arange(0, lengthFreqRHigh)  # makes an array from 0 to the length of the song freqReallyHigh, with the values 0-length

# ----------- NORMALISATION ------------ #
soundInput = soundInput[:] / 2 ** 15  # Normalises all the soundInput values.

# ------------ CALCULATIONS FOR ECHO ------------ #
echoSmall = echoEffect(soundInput, 0.5, sf)  # Runs the method for echo effect with small echo
print("echo small")  # Prints when the method is done
echoMed = echoEffect(soundInput, 1, sf)  # Runs the method for echo effect with medium echo
print("echo mid")  # Prints when the method is done
echoHigh = echoEffect(soundInput, 1.5, sf)  # Runs the method for echo effect with high echo
print("echo high")  # Prints when the method is done
echoReallyHigh = echoEffect(soundInput, 2, sf)  # Runs the method for echo effect with very high echo
print("echo small")  # Prints when the method is done

# ------------ CALCULATIONS FOR VIBRATO ------------ #
vibratoSmall = addVibrato(soundInput, 0.005, sf)  # Runs the method for Vibrato effect with small vibrato
print("Vibrato small")  # Prints when the method is done
vibratoMed = addVibrato(soundInput, 0.01, sf)  # Runs the method for Vibrato effect with medium vibrato
print("Vibrato med")  # Prints when the method is done
vibratoHigh = addVibrato(soundInput, 0.05, sf)  # Runs the method for Vibrato effect with high vibrato
print("Vibrato high")  # Prints when the method is done
vibratoReallyHigh = addVibrato(soundInput, 0.1, sf)  # Runs the method for Vibrato effect with very high vibrato
print("Vibrato very high")  # Prints when the method is done
# plotGraph(soundInput, vibrato, time)
# ------------ CALCULATIONS FOR CHORUS ------------ #
chorusSmall = chorusEffect(soundInput, 0.1, sf)  # Runs the method for Chorus effect with small chorus
print("chorus small")  # Prints when the method is done
chorusMed = chorusEffect(soundInput, 0.5, sf)  # Runs the method for Chorus effect with medium chorus
print("chorus med")  # Prints when the method is done
chorusHigh = chorusEffect(soundInput, 1, sf)  # Runs the method for Chorus effect with high chorus
print("chorus high")  # Prints when the method is done
chorusReallyHigh = chorusEffect(soundInput, 1.5, sf)  # Runs the method for Chorus effect with very high chorus
print("chorus very high")  # Prints when the method is done
# Makes sure to not stop the melody before everything has played through.
print("Done Processing")  # Prints when all audio processing methods are done


def soundEffect(lastValueID, sensorvalue, state):

    if state == 0:
        if lastValueID != 0:
            sd.play(soundInput, sf)  # The song plays if the state is 0 and the lastValueID isn't zero
            lastValueID = 0  # Sets lastValueID to zero
        write_to_sheet()  # runs the write_to_sheet Method.

    if state == 1:
        if 0 <= sensorvalue <= 1:
            if lastValueID != 1:
                sd.play(freqSmall, sf)  # The song plays if the state is 1, the sensor value is between 0 and 1
                # and the lastValueID isn't 1
                lastValueID = 1  # Sets lastValueID to 1
                data_storage.append(lastValueID)  # Stores the value of lastValueID to an array used for data collection

        elif sensorvalue == 2:
            if lastValueID != 2:
                sd.play(freqMed, sf)  # The song plays if the sensor value is 2 and the lastValueID isn't 2
                lastValueID = 2  # Sets lastValueID to 2
                data_storage.append(lastValueID)  # Stores the value of lastValueID to an array used for data collection

        elif sensorvalue == 3:
            if lastValueID != 3:
                sd.play(freqHigh, sf)  # The song plays if the sensor value is 3 and the lastValueID isn't 3
                lastValueID = 3  # Sets lastValueID to 3
                data_storage.append(lastValueID)  # Stores the value of lastValueID to an array used for data collection

        elif 3 < sensorvalue:
            if lastValueID != 4:
                sd.play(freqReallyHigh, sf)  # The song plays if the sensor value is 4 and the lastValueID isn't 4
                lastValueID = 4  # Sets lastValueID to 4
                data_storage.append(lastValueID)  # Stores the value of lastValueID to an array used for data collection

    if state == 2:
        if 0 <= sensorvalue <= 1:
            if lastValueID != 5:
                sd.play(echoSmall, sf)  # The song plays if the state is 2, the sensor value is between 0 and 1
                # and the lastValueID isn't 5
                lastValueID = 5  # Sets lastValueID to 5
                data_storage1.append(lastValueID)  # Stores the value of lastValueID to an array used for data collection
        elif sensorvalue == 2:
            if lastValueID != 6:
                sd.play(echoMed, sf)  # The song plays if the sensor value is 6 and the lastValueID isn't 6
                lastValueID = 6  # Sets lastValueID to 6
                data_storage1.append(lastValueID)  # Stores the value of lastValueID to an array used for data collection
        elif sensorvalue == 3:
            if lastValueID != 7:
                sd.play(echoHigh, sf)  # The song plays if the sensor value is 7 and the lastValueID isn't 7
                lastValueID = 7  # Sets lastValueID to 7
                data_storage1.append(lastValueID)  # Stores the value of lastValueID to an array used for data collection
        elif 3 < sensorvalue:
            if lastValueID != 8:
                sd.play(echoReallyHigh, sf)  # The song plays if the sensor value is 8 and the lastValueID isn't 8
                lastValueID = 8  # Sets lastValueID to 8
                data_storage1.append(lastValueID)  # Stores the value of lastValueID to an array used for data collection

    if state == 3:
        if 0 <= sensorvalue <= 1:
            if lastValueID != 9:
                sd.play(vibratoSmall, sf)  # The song plays if the state is 3, the sensor value is between 0 and 1
                # and the lastValueID isn't 9
                lastValueID = 9  # Sets lastValueID to 9
                data_storage2.append(lastValueID)  # Stores the value of lastValueID to an array used for data collection

        elif sensorvalue == 2:
            if lastValueID != 10:
                sd.play(vibratoMed, sf)  # The song plays if the sensor value is 10 and the lastValueID isn't 10
                lastValueID = 10  # Sets lastValueID to 10
                data_storage2.append(lastValueID)  # Stores the value of lastValueID to an array used for data collection

        elif sensorvalue == 3:
            if lastValueID != 11:
                sd.play(vibratoHigh, sf)  # The song plays if the sensor value is 11 and the lastValueID isn't 11
                lastValueID = 11  # Sets lastValueID to 11
                data_storage2.append(lastValueID)  # Stores the value of lastValueID to an array used for data collection

        elif 3 < sensorvalue:
            if lastValueID != 12:
                sd.play(vibratoReallyHigh, sf)  # The song plays if the sensor value is 12 and the lastValueID isn't 12
                lastValueID = 12  # Sets lastValueID to 12
                data_storage2.append(lastValueID)  # Stores the value of lastValueID to an array used for data collection

    if state == 4:
        if 0 <= sensorvalue <= 1:
            if lastValueID != 13:
                sd.play(chorusSmall, sf)  # The song plays if the state is 4, the sensor value is between 0 and 1
                # and the lastValueID isn't 13
                lastValueID = 13  # Sets lastValueID to 13
                data_storage3.append(lastValueID)  # Stores the value of lastValueID to an array used for data collection

        elif sensorvalue == 2:
            if lastValueID != 14:
                sd.play(chorusMed, sf)  # The song plays if the sensor value is 14 and the lastValueID isn't 14
                lastValueID = 14  # Sets lastValueID to 14
                data_storage3.append(lastValueID)  # Stores the value of lastValueID to an array used for data collection

        elif sensorvalue == 3:
            if lastValueID != 15:
                sd.play(chorusHigh, sf)  # The song plays if the sensor value is 15 and the lastValueID isn't 15
                lastValueID = 15  # Sets lastValueID to 15
                data_storage3.append(lastValueID)  # Stores the value of lastValueID to an array used for data collection

        elif 3 < sensorvalue:
            if lastValueID != 16:
                sd.play(chorusReallyHigh, sf)  # The song plays if the sensor value is 16 and the lastValueID isn't 16
                lastValueID = 16  # Sets lastValueID to 16
                data_storage3.append(lastValueID)  # Stores the value of lastValueID to an array used for data collection

    return lastValueID  # Returns the lastValueID for the ArduinoRead method to use.
