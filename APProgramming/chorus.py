from vibrato import*


def chorusEffect(inputSignal, mixParam, offset, digModFreq, modDepth):
    # add the original instrument to the mix
    outputSignal = inputSignal
    # add additional instruments using the vibrato effect
    nAdditionInstruments = np.size(mixParam)
    for ii in np.arange(nAdditionInstruments):
        outputSignal = outputSignal + \
                       mixParam[ii] * addVibrato(inputSignal, modDepth[ii], digModFreq[ii], offset[ii])
    print("Chorus Done!")
    return outputSignal
