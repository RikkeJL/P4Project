import sounddevice as sd
import scipy.io.wavfile as wave
from echo import*
from vibrato import*
from frequencyChange import*
from chorus import*


sf, soundInput = wave.read('A_Light_Breeze_from_South_West.wav')

# ----------- CALCULATIONS FOR FREQUENCY CHANGE ---------#
freq = resampleFreq(soundInput)

# ----------- NORMALISATION ------------ #
soundInput = soundInput[:]/2**15

# ------------ CALCULATIONS FOR ECHO ------------ #
echo = echoEffect(soundInput, 0.5, sf)

# ------------ CALCULATIONS FOR VIBRATO ------------ #
vibrato = addVibrato(soundInput, sf)

# ------------ CALCULATIONS FOR CHORUS ------------ #
chorus = chorusEffect(soundInput, sf)

print("Done Processing")
# counter = np.int(input("Please enter an integer from 0-4: "))

# if counter == 1:
# sd.play(echo, sf)
# elif counter == 2:
# sd.play(vibrato, sf)
# elif counter == 3:
# sd.play(chorus, sf)
# else:
# sd.play(soundInput)

# Makes sure to not stop the melody before everything has played through.
# status = sd.wait()
