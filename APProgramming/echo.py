import numpy as np


def echoEffect(inputSignal, filterCoef, samplingFreq):
    delay = np.int(np.round(0.15 * samplingFreq))
    nData = np.size(inputSignal)
    outputSignal = np.zeros(nData)
    for n in np.arange(nData):
        print(n)
        if n < delay:
            outputSignal[n] = inputSignal[n]
        else:
            outputSignal[n] = inputSignal[n] + filterCoef * outputSignal[n - delay]
    print("Echo Done!")
    return outputSignal
