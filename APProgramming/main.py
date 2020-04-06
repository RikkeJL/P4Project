import sounddevice as sd
from echo import*
from chorus import*
import scipy.io.wavfile as wave

sf, soundInput = wave.read('test3.wav')

# Normalises the value by ?????
soundInput = soundInput[:, 0]/2**15

# ------------ CALCULATIONS FOR ECHO ------------ #
# Calculates the delay
# delay = np.int(np.round(0.15*sf))

# applies the echo filter to the input
echo = echoEffect(soundInput, 10, sf)

# ------------ CALCULATIONS FOR VIBRATO ------------ #
maxDelay = 0.005*sf  # samples
digModFreq = 2*np.pi*5/sf  # rad/sample
vibrato = addVibrato(soundInput, maxDelay, digModFreq)

# ------------ CALCULATIONS FOR CHORUS ------------ #
mixParam = np.array([0.9, 0.9, 0.8])
offset = np.array([0.01, 0.012, 0.008])*sf  # samples
digModFreq = 2*np.pi*np.array([0.1, 0.15, 0.05])/sf  # radians/sample
modDepth = np.array([0.02, 0.021, 0.018])*sf  # samples
chorus = chorusEffect(soundInput, mixParam, offset, digModFreq, modDepth)


# Plays the melody based on the raw data and the sampling frequency.
# sd.play(chorus, sf)

# Makes sure to not stop the melody before everything has played through.
# status = sd.wait()

