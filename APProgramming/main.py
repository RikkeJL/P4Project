from SoundEffects.echo import*
from SoundEffects.vibrato import*
from SoundEffects.frequencyChange import*
from SoundEffects.chorus import*
from graphMethod import*
from UserInput.UseData import*
from UserInput.ArduinoRead import*
import sounddevice as sd
import scipy.io.wavfile as wave


# length = np.size(outData)
# time = np.arange(0, length)

#sf, soundInput = wave.read("test3.wav")


# ----------- CALCULATIONS FOR FREQUENCY CHANGE ---------#
# freq = resampleFreq(soundInput, 2)

# plotGraph(freq, time)

# ----------- NORMALISATION ------------ #
#soundInput = soundInput[:, 0]/2**15

#length = np.size(soundInput)
#time = np.arange(0, length)

# ------------ CALCULATIONS FOR ECHO ------------ #
# echo = echoEffect(soundInput, 0.5, sf)

# ------------ CALCULATIONS FOR VIBRATO ------------ #
# vibrato = addVibrato(soundInput, sf)
# plotGraph(soundInput, vibrato, time)
# ------------ CALCULATIONS FOR CHORUS ------------ #
#chorus = chorusEffect(soundInput, sf)
#plotGraph(soundInput, chorus, time)

# counter = np.int(input("Please enter an integer from 0-4: "))

# if counter == 1:
# sd.play(echo, sf)
# elif counter == 2:
# sd.play(vibrato, sf)
# elif counter == 3:
#sd.play(chorus, sf)
# elif counter == 4:
# sd.play(freq, sf)
# else:
# sd.play(soundInput, sf)
# status = sd.wait()

readInput()
