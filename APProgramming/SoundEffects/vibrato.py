import numpy as np


def addVibrato(inputSignal, changeVal, sf, offset=1):
    modDepth = changeVal * sf  # Maximum delay in samples
    digModFreq = 2 * np.pi * 5 / sf  # Calculates part of the time varying delay.
    nData = np.size(inputSignal)  # Gets size of input signal array
    outputSignal = np.zeros(nData)  # makes an array of length nData purely out of zeros
    tmpSignal = np.zeros(nData)  # makes another array of length nData purely out of zeros
    for n in np.arange(nData):  # For all values from 0 to nData
        delay = offset + (modDepth/2)*(1-np.cos(digModFreq*n))  # calculates time-varying delay
        if n < delay:  # if n is smaller than delay
            outputSignal[n] = 0  # set outputsignal n to 0
        else:
            intDelay = np.int(np.floor(delay))  # make an integer delay that is rounded down from the float delay
            tmpSignal[n] = inputSignal[n-intDelay]  # save the temp signal to be the nth - intdelay inputsignal
            fractionalDelay = delay-intDelay  # make a fractional delay based on the delay and intdelay
            apParameter = (1-fractionalDelay)/(1+fractionalDelay)  # calculates parameter b for allpass filter
            outputSignal[n] = apParameter*tmpSignal[n]+tmpSignal[n-1]-apParameter*outputSignal[n-1]  #runs song through
            # allpass filter
    return outputSignal  # returns outputsignal array
