import numpy as np


def addVibratoToChorus(inputSignal, sf, digModFreq, changeVal, offset):
    modDepth = changeVal * sf  # samples
    nData = np.size(inputSignal)
    outputSignal = np.zeros(nData)
    tmpSignal = np.zeros(nData)
    for n in np.arange(nData):
        # calculate delay
        delay = offset + (modDepth/2)*(1-np.cos(digModFreq*n))
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


def chorusEffect(inputSignal, changeVal, sf):
    mixParam = np.array([0.9, 0.9, 0.8])
    offset = np.array([0.1, 0.12, 0.08])*sf  # samples
    digModFreq = 2*np.pi*np.array([0.1, 0.15, 0.05])/sf  # radians/sample
    modDepth = np.array([0.02, 0.021, 0.018])*sf  # samples
    # add the original instrument to the mix
    outputSignal = inputSignal
    # add additional instruments using the vibrato effect
    nAdditionInstruments = np.size(mixParam)
    for ii in np.arange(nAdditionInstruments):
        outputSignal = outputSignal+mixParam[ii]*addVibratoToChorus(inputSignal,
                                                                    modDepth[ii], changeVal, digModFreq[ii], offset[ii])
    print("Chorus Done!")
    return outputSignal
