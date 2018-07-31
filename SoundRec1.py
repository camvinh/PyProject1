import numpy as np
import sounddevice as sd
from scipy.io import wavfile
# Hz
fs = 44100
# Hz
f = 440
# s
length = 2

#myarray = np.arange(fs*length)
#myarray = np.tan(2*np.pi*f/fs*myarray + np.pi/4)

#sd.play(myarray, fs)

#print(str(sd.query_devices()))
sd.default.device[0] = 1
ch = 'c'
for i in range(10):
    print('%s%d' % (ch, i))
    print('start')
    recording = sd.rec(frames=fs * length, samplerate=fs, blocking=True, channels=1)
    wavfile.write('%s%d.wav' % (ch, i), fs, recording)
    print('finish')


