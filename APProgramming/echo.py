import numpy as np
import wave


def echoEffect(inputSignal, filterCoef, delay):
    nData = np.size(inputSignal)
    outputSignal = np.zeros(nData)
    for n in np.arange(nData):
        if n < delay:
            outputSignal[n] = inputSignal[n]
        else:
            outputSignal[n] = inputSignal[n] + filterCoef * inputSignal[n - delay]
    return outputSignal
