from SoundEffects.echo import *
from SoundEffects.vibrato import *
from SoundEffects.frequencyChange import *
from SoundEffects.chorus import *
from graphMethod import *
from UserInput.CollectData import *


import scipy.io.wavfile as wave
import sounddevice as sd
import numpy as np

sf, soundInput = wave.read("A Light Breeze from South West Redux.wav")
length = np.size(soundInput)
time = np.arange(0, length)


# ----------- CALCULATIONS FOR FREQUENCY CHANGE ---------#
freqSmall = resampleFreq(soundInput, 2)
print("Freq small")
freqMed = resampleFreq(soundInput, 5)
print("Freq med")
freqHigh = resampleFreq(soundInput, 10)
print("Freq high")
freqReallyHigh = resampleFreq(soundInput, 15)
print("Freq very high")

lengthFreqSmall = np.size(freqSmall)
lengthFreqMed = np.size(freqMed)
lengthFreqHigh = np.size(freqHigh)
lengthFreqRHigh = np.size(freqReallyHigh)

timeFreqSmall = np.arange(0, lengthFreqSmall)
timeFreqMed = np.arange(0, lengthFreqMed)
timeFreqHigh = np.arange(0, lengthFreqHigh)
timeFreqRHigh = np.arange(0, lengthFreqRHigh)

# ----------- NORMALISATION ------------ #
soundInput = soundInput[:] / 2 ** 15
freqSmall = freqSmall[:] / 2 ** 15
freqMed = freqMed[:] / 2 ** 15
freqHigh = freqHigh[:] / 2 ** 15
freqReallyHigh = freqReallyHigh[:] / 2 ** 15

# ------------ CALCULATIONS FOR ECHO ------------ #
echoSmall = echoEffect(soundInput, 0.5, sf)
print("echo small")
echoMed = echoEffect(soundInput, 1, sf)
print("echo mid")
echoHigh = echoEffect(soundInput, 1.5, sf)
print("echo high")
echoReallyHigh = echoEffect(soundInput, 2, sf)
print("echo small")

# ------------ CALCULATIONS FOR VIBRATO ------------ #
vibratoSmall = addVibrato(soundInput, 0.005, sf)
print("Vibrato small")
vibratoMed = addVibrato(soundInput, 0.01, sf)
print("Vibrato med")
vibratoHigh = addVibrato(soundInput, 0.05, sf)
print("Vibrato high")
vibratoReallyHigh = addVibrato(soundInput, 0.1, sf)
print("Vibrato very high")
# plotGraph(soundInput, vibrato, time)
# ------------ CALCULATIONS FOR CHORUS ------------ #
chorusSmall = chorusEffect(soundInput, 0.1, sf)
print("chorus small")
chorusMed = chorusEffect(soundInput, 0.5, sf)
print("chorus med")
chorusHigh = chorusEffect(soundInput, 1, sf)
print("chorus high")
chorusReallyHigh = chorusEffect(soundInput, 1.5, sf)
print("chorus very high")
# Makes sure to not stop the melody before everything has played through.
print("Done Processing")


def soundEffect(lastValueID, sensorvalue, state):

    if state == 0:
        if lastValueID != 0:
            sd.play(soundInput, sf)
            lastValueID = 0
        write_to_sheet()

    if state == 1:
        if 0 <= sensorvalue <= 1:
            if lastValueID != 1:
                sd.play(freqSmall, sf)
                lastValueID = 1
                data_storage.append(lastValueID)

        elif sensorvalue == 2:
            if lastValueID != 2:
                sd.play(freqMed, sf)
                lastValueID = 2
                data_storage.append(lastValueID)

        elif sensorvalue == 3:
            if lastValueID != 3:
                sd.play(freqHigh, sf)
                lastValueID = 3
                data_storage.append(lastValueID)

        elif 3 < sensorvalue:
            if lastValueID != 4:
                sd.play(freqReallyHigh, sf)
                lastValueID = 4
                data_storage.append(lastValueID)

    if state == 2:
        if 0 <= sensorvalue <= 1:
            if lastValueID != 5:
                sd.play(echoSmall, sf)
                lastValueID = 5
                data_storage1.append(lastValueID)
        elif sensorvalue == 2:
            if lastValueID != 6:
                sd.play(echoMed, sf)
                lastValueID = 6
                data_storage1.append(lastValueID)
        elif sensorvalue == 3:
            if lastValueID != 7:
                sd.play(echoHigh, sf)
                lastValueID = 7
                data_storage1.append(lastValueID)
        elif 3 < sensorvalue:
            if lastValueID != 8:
                sd.play(echoReallyHigh, sf)
                lastValueID = 8
                data_storage1.append(lastValueID)

    if state == 3:
        if 0 <= sensorvalue <= 1:
            if lastValueID != 9:
                sd.play(vibratoSmall, sf)
                lastValueID = 9
                data_storage2.append(lastValueID)

        elif sensorvalue == 2:
            if lastValueID != 10:
                sd.play(vibratoMed, sf)
                lastValueID = 10
                data_storage2.append(lastValueID)

        elif sensorvalue == 3:
            if lastValueID != 11:
                sd.play(vibratoHigh, sf)
                lastValueID = 11
                data_storage2.append(lastValueID)

        elif 3 < sensorvalue:
            if lastValueID != 12:
                sd.play(vibratoReallyHigh, sf)
                lastValueID = 12
                data_storage2.append(lastValueID)

    if state == 4:
        if 0 <= sensorvalue <= 1:
            if lastValueID != 13:
                sd.play(chorusSmall, sf)
                lastValueID = 13
                data_storage3.append(lastValueID)

        elif sensorvalue == 2:
            if lastValueID != 14:
                sd.play(chorusMed, sf)
                lastValueID = 14
                data_storage3.append(lastValueID)

        elif sensorvalue == 3:
            if lastValueID != 15:
                sd.play(chorusHigh, sf)
                lastValueID = 15
                data_storage3.append(lastValueID)

        elif 3 < sensorvalue:
            if lastValueID != 16:
                sd.play(chorusReallyHigh, sf)
                lastValueID = 16
                data_storage3.append(lastValueID)

    return lastValueID
