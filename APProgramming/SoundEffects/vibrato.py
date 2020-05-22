import numpy as np


def addVibrato(inputSignal, changeVal, sf, offset=1):
    modDepth = changeVal * sf  # samples
    digModFreq = 2 * np.pi * 5 / sf  # rad/sample
    nData = np.size(inputSignal)
    outputSignal = np.zeros(nData)
    tmpSignal = np.zeros(nData)
    for n in np.arange(nData):
        delay = offset + (modDepth/2)*(1-np.cos(digModFreq*n))  # calculate delay
        # calculate filter output
        if n < delay:
            outputSignal[n] = 0
        else:
            intDelay = np.int(np.floor(delay))
            tmpSignal[n] = inputSignal[n-intDelay]
            fractionalDelay = delay-intDelay
            apParameter = (1-fractionalDelay)/(1+fractionalDelay)
            outputSignal[n] = apParameter*tmpSignal[n]+tmpSignal[n-1]-apParameter*outputSignal[n-1]
    return outputSignal
