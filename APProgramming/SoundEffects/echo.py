import numpy as np


def echoEffect(inputSignal, filterCoef, samplingFreq):
    delay = np.int(np.round(0.15 * samplingFreq))  # Calculates the delay and makes it an integer
    nData = np.size(inputSignal)  # Gets the length of the input signal array
    outputSignal = np.zeros(nData)  # Sets output signal to be the an array of zeros with length nData
    for n in np.arange(nData):  # For all values from 0 to nData
        if n < delay:  # if n is smaller than the delay
            outputSignal[n] = inputSignal[n]  # set the output signal n to be equal to the input signal n
        else:
            outputSignal[n] = inputSignal[n] + filterCoef * outputSignal[n - delay]  # else set the output signal n to
            # be equal to the input signal run through a feedback filter.
    return outputSignal  # Return the output signal array
