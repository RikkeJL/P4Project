from frequencyChange import*
from echo import*
from chorus import*
from vibrato import*
import scipy.io.wavfile as waves

sf, soundInput = wave.read('test3.wav')

# Normalises the value by ?????
soundInput = soundInput[:,0]/2**15

# Calculates the delay
delay = np.int(np.round(0.15*sf))

# applies the echo filter to the input
echo = echoEffect(soundInput, 10, delay)

# Plays the melody based on the raw data and the sampling frequency.
sd.play(echo, sf)

# Makes sure to not stop the melody before everything has played through.
status = sd.wait()
