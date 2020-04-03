import numpy as np


def echoEffect(inputSignal, filterCoef, delay):
    nData = np.size(inputSignal)
    outputSignal = np.zeros(nData)
    for n in np.arange(nData):
        if n < delay:
            outputSignal[n] = inputSignal[n]
        else:
            outputSignal[n] = inputSignal[n] + filterCoef * outputSignal[n - delay]
    return outputSignal
