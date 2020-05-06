import scipy.io.wavfile as wave
import sounddevice as sd
import numpy as np

sf, outData = wave.read('A_Light_Breeze_from_South_West.wav')


def openOutputStream():
    stream = sd.Stream()
    return stream
