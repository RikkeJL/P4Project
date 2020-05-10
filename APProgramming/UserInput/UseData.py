from SoundEffects.echo import *
from SoundEffects.vibrato import *
from SoundEffects.frequencyChange import *
from SoundEffects.chorus import *

import scipy.io.wavfile as wave
import sounddevice as sd
import numpy as np

# ----------- CALCULATIONS FOR FREQUENCY CHANGE ---------#
#freq = resampleFreq(soundInput, 2)
# plotGraph(freq, time)

# ----------- NORMALISATION ------------ #
#soundInput = soundInput[:] / 2 ** 15

# ------------ CALCULATIONS FOR ECHO ------------ #
# echo = echoEffect(soundInput, 0.5, sf)

# ------------ CALCULATIONS FOR VIBRATO ------------ #
# vibrato = addVibrato(soundInput, sf)

# plotGraph(soundInput, vibrato, time)
# ------------ CALCULATIONS FOR CHORUS ------------ #
# chorus = chorusEffect(soundInput, sf)

# Makes sure to not stop the melody before everything has played through.
print("Done Processing")


def soundEffect(sensorvalue=0, state=0):

    print("Before if")
    print(sensorvalue)
    print(state)

    if state == 0:
        sound = 0

    if state == 1:
        if 0 <= sensorvalue <= 0.875:
            sound = 1
        elif 0.875 < sensorvalue <= 1.75:
            sound = 2
        elif 1.75 < sensorvalue <= 2.625:
            sound = 3
        elif 2.625 < sensorvalue:
            sound = 4

    if state == 2:
        if 0 <= sensorvalue <= 0.875:
            sound = 5
        elif 0.875 < sensorvalue <= 1.75:
            sound = 6
        elif 1.75 < sensorvalue <= 2.625:
            sound = 7
        elif 2.625 < sensorvalue:
            sound = 8

    if state == 3:
        if 0 <= sensorvalue <= 0.875:
            sound = 9
        elif 0.875 < sensorvalue <= 1.75:
            sound = 10
        elif 1.75 < sensorvalue <= 2.625:
            sound = 11
        elif 2.625 < sensorvalue:
            sound = 12

    if state == 4:
        if 0 <= sensorvalue <= 0.875:
            sound = 13
        elif 0.875 < sensorvalue <= 1.75:
            sound = 14
        elif 1.75 < sensorvalue <= 2.625:
            sound = 15
        elif 2.625 < sensorvalue:
            sound = 16

    print("after if")
    print(sensorvalue)
    print(state)

    print("sound value")
    print(sound)

    sd.stop()
    sf, soundInput = wave.read("A_Light_Breeze_from_South_West.wav")
    length = np.size(soundInput)
    soundInput = soundInput[:] / 2 ** 15
    time = np.arange(0, length)
    sd.play(soundInput, sf)
