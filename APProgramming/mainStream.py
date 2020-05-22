import wave
import pyaudio as pa
import numpy as np
from SoundEffects.echo import *
from SoundEffects.vibrato import *
from SoundEffects.chorus import *

CHUNK = 1024

soundFile = wave.open('test3.wav', 'rb')

# p = pa.PyAudio()

# stream = p.open(format=p.get_format_from_width(soundFile.getsampwidth()),
#                channels=soundFile.getnchannels(),
#                rate=soundFile.getframerate(),
#                output=True)

#data = soundFile.readframes(CHUNK)

# while len(data) > 0:
  #   stream.write(data)
  #   data = soundFile.readframes(CHUNK)
    
# stream.stop_stream()
# stream.close()
# soundFile.close()

# p.terminate()
