import numpy as np


def resampleFreq(data, factor):
    freqchange = np.round(np.arange(0, len(data), factor)) #calulates the array for the data with the spacing between
                                                           #each datapoint as defined by the factor amount.
                                                           #The np.round is called to avoid spacing by a float number.

    freqchange = freqchange[freqchange < len(data)] #apply the data to the new array.
    return data[freqchange.astype(int)] #returns the array with the data.
