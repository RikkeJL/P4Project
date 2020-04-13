import numpy as np


def resampleFreq(data):
    # controls how we increase the pitch. If positive it increases pitch, if negative it decreases pitch.
    pitch = -10000

    # apply a fast fourier transform to the data. The types used is Real Fast Fourier Transform.
    fftData = np.fft.rfft(data)

    # we create a temporary array to store the data in.
    tempData = [0] * len(fftData)

    # checks the operation which operation we wish to run and then run it.
    if pitch >= 0:
        # increase frequency
        tempData[pitch:len(fftData)] = fftData[0:(len(fftData) - pitch)]
        tempData[0:pitch] = fftData[(len(fftData) - pitch):len(fftData)]
    else:
        # decrease frequency
        tempData[0:(len(fftData) + pitch)] = fftData[-pitch:len(fftData)]
        tempData[(len(fftData) + pitch):len(fftData)] = fftData[0:-pitch]

    # Packing the data into a final data array
    pitchedData = np.array(tempData)

    # inverse transform to get back to temporal data
    pitchedData = np.fft.irfft(pitchedData)

    # returns the data
    return pitchedData
