
from echo import*
import sounddevice as sd
import scipy.io.wavfile as wave

sf, soundInput = wave.read('A_Light_Breeze_from_South_West.wav')
delay = np.int(np.round(0.15*sf))
echo = echoEffect(soundInput, 0.5, delay)

sd.play(echo, sf)
status = sd.wait()
