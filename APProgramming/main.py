import sounddevice as sd
from echo import*
from vibrato import*
from frequencyChange import*
import scipy.io.wavfile as wave

sf, soundInput = wave.read('A_Light_Breeze_from_South_West.wav')

# ----------- CALCULATIONS FOR FREQUENCY CHANGE ---------#
soundInput = resampleFreq(soundInput, 0.5)

#--------------NORMALISATION OF INPUT--------------------#
# Normalises the value by ?????
soundInput = soundInput[:]/2**15

# ------------ CALCULATIONS FOR ECHO ------------ #
# Calculates the delay
# delay = np.int(np.round(0.15*sf))

# applies the echo filter to the input
# echo = echoEffect(soundInput, 10, delay)

# ------------ CALCULATIONS FOR VIBRATO ------------ #
#maxDelay = 0.005*sf  # samples
#digModFreq = 2*np.pi*5/sf  # rad/sample
#vibrato = addVibrato(soundInput, maxDelay, digModFreq)

# Plays the melody based on the raw data and the sampling frequency.
sd.play(soundInput, sf)

# Makes sure to not stop the melody before everything has played through.
status = sd.wait()
