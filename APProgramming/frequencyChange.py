import numpy as np

def resampleFreq(data, factor):
    freqchange = np.round(np.arange(0, len(data), factor))
    freqchange = freqchange[freqchange < len(data)]
    return data[freqchange.astype(int)]
