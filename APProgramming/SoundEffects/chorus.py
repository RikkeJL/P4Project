import numpy as np


def addVibratoToChorus(inputSignal, modDepth, digModFreq, offset):
    nData = np.size(inputSignal)  # Gets size of input signal array
    outputSignal = np.zeros(nData)  # makes an array of length nData purely out of zeros
    tmpSignal = np.zeros(nData)  # makes another array of length nData purely out of zeros
    for n in np.arange(nData):  # For all values from 0 to nData
        delay = offset + (modDepth/2)*(1-np.cos(digModFreq*n))  # calculates time-varying delay
        # calculate filter output
        if n < delay:  # if n is smaller than delay
            outputSignal[n] = 0  # set outputsignal n to 0
        else:
            intDelay = np.int(np.floor(delay))  # make an integer delay that is rounded down from the float delay
            tmpSignal[n] = inputSignal[n-intDelay]  # save the temp signal to be the nth - intdelay inputsignal
            fractionalDelay = delay-intDelay  # make a fractional delay based on the delay and intdelay
            apParameter = (1-fractionalDelay)/(1+fractionalDelay)  # calculates parameter b for allpass filter
            outputSignal[n] = apParameter*tmpSignal[n]+tmpSignal[n-1]-apParameter*outputSignal[n-1]  # runs song through
            # allpass filter
    return outputSignal  # returns outputsignal array


def chorusEffect(inputSignal, changeVal, sf):
    mixParam = np.array([0.9, 0.9, 0.8])  # sets mix parameters for the k'th simulated song
    offset = np.array([0.1, 0.12, 0.08])*sf  # sets the offsets
    digModFreq = 2*np.pi*np.array([0.1, 0.15, 0.05])/sf  # Calculates part of the time varying delay.
    modDepth = np.array([changeVal, changeVal-0.01, changeVal-0.05])*sf  # Maximum delay in samples
    outputSignal = inputSignal  # Set output signal to be equal to the input signal
    nAdditionInstruments = np.size(mixParam)  # make an array of nAdditional Instruments and make it the size of mix
    # params
    for ii in np.arange(nAdditionInstruments):  # for all values from 0 to nAdditionInstruments
        outputSignal = outputSignal+mixParam[ii]*addVibratoToChorus(inputSignal,
                                                                    modDepth[ii], digModFreq[ii], offset[ii])
        # The inputsignal through vibrato effect, while adding the outputsignal and multiplying it with the mix
        # parameters
    return outputSignal  # return output signal
