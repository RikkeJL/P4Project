import sounddevice as sd
from echo import*
from chorus import*
import scipy.io.wavfile as wave

# Gets the sampling frequency of the sound, as well as all the raw data from the sound, and saves it as a numpy array.
sf, soundInput = wave.read('A_Light_Breeze_from_South_West.wav')

# Normalises the values in the array
soundInput = soundInput[:]/2**15

# ------------ CALCULATIONS FOR ECHO ------------ #
echo = echoEffect(soundInput, 0.5, sf)

# ------------ CALCULATIONS FOR VIBRATO ------------ #

# vibrato = addVibrato(soundInput, sf)

# ------------ CALCULATIONS FOR CHORUS ------------ #

# chorus = chorusEffect(soundInput, sf)

# counter = np.int(input("Please enter an integer from 0-4: "))

# if counter == 1:
sd.play(echo, sf)
# elif counter == 2:
# sd.play(vibrato, sf)
# elif counter == 3:
# sd.play(chorus, sf)
# else:
# sd.play(soundInput)

# Makes sure to not stop the melody before everything has played through.
status = sd.wait()

