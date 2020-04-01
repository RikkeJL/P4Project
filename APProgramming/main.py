from frequencyChange import*
from echo import*
from chorus import*
from vibrato import*
import pyaudio
import wave as wv
import scipy.io.wavfile as waves

filename = 'A_Light_Breeze_from_South_West.wav'

# Set chunk size of 1024 samples per data frame
chunk = 1024

# Open the sound file

wf = wave.open(filename, 'rb')

# delay = np.int(np.round(0.15*wf.getframerate()))
# echo = echoEffect(, 0.5, delay)
# Create an interface to PortAudio
p = pyaudio.PyAudio()

# Open a .Stream object to write the WAV file to
# 'output = True' indicates that the sound will be played rather than recorded
stream = p.open(format=p.get_format_from_width(wf.getsampwidth()),
                channels=wf.getnchannels(),
                rate=wf.getframerate(),
                output=True)


# Read data in chunks
data = wf.readframes(chunk)

# Play the sound by writing the audio data to the stream
while data != '':
    stream.write(data)
    data = wf.readframes(chunk)

# Close and terminate the stream
stream.close()
p.terminate()
