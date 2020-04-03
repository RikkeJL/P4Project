import sounddevice as sd
from echo import*
from vibrato import*
import scipy.io.wavfile as waves

sf, soundInput = wave.read('test3.wav')

# Normalises the value by ?????
soundInput = soundInput[:]/2**15

# ------------ CALCULATIONS FOR ECHO ------------ #
# Calculates the delay
# delay = np.int(np.round(0.15*sf))

# applies the echo filter to the input
# echo = echoEffect(soundInput, 10, delay)

# ------------ CALCULATIONS FOR VIBRATO ------------ #
maxDelay = 0.005*sf  # samples
digModFreq = 2*np.pi*5/sf  # rad/sample
vibrato = addVibrato(soundInput, maxDelay, digModFreq)

# Plays the melody based on the raw data and the sampling frequency.
sd.play(vibrato, sf)

# Makes sure to not stop the melody before everything has played through.
status = sd.wait()

