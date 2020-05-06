import sys
from mainStream import*
from SoundEffects.echo import*
from SoundEffects.vibrato import*
from SoundEffects.frequencyChange import*
from SoundEffects.chorus import*
from graphMethod import*

length = np.size(outData)
time = np.arange(0, length)

stream = openOutputStream()

with stream:
    stream.read()


# ----------- CALCULATIONS FOR FREQUENCY CHANGE ---------#
# freq = resampleFreq(soundInput, 2)

# plotGraph(freq, time)

# ----------- NORMALISATION ------------ #
# soundInput = soundInput[:]/2**15

# ------------ CALCULATIONS FOR ECHO ------------ #
# echo = echoEffect(soundInput, 0.5, sf)

# ------------ CALCULATIONS FOR VIBRATO ------------ #
# vibrato = addVibrato(soundInput, sf)
# plotGraph(soundInput, vibrato, time)
# ------------ CALCULATIONS FOR CHORUS ------------ #
# chorus = chorusEffect(soundInput, sf)

# counter = np.int(input("Please enter an integer from 0-4: "))

# if counter == 1:
# sd.play(echo, sf)
# elif counter == 2:
# sd.play(vibrato, sf)
# elif counter == 3:
# sd.play(chorus, sf)
# elif counter == 4:
# sd.play(freq, sf)
# else:
# sd.play(soundInput, sf)

# Makes sure to not stop the melody before everything has played through.
# status = sd.wait()
