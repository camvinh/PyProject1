import numpy as np
import matplotlib.pyplot as plt
from scipy import signal
from scipy.signal.windows import kaiser
from scipy.io import wavfile




def Chuli(path):
    freq, x = wavfile.read(path)
    # t = np.arange(0, x.size / freq, 1 / freq)
    f, t, Sxx = signal.spectrogram(x, freq)
    print(f.size)
    f1 = f[:6]
    Sxx1 = Sxx[:6, :]
    plt.title(path)
    plt.pcolormesh(t, f1, Sxx1)
    plt.ylabel('Frequency [Hz]')
    plt.xlabel('Time [sec]')
    plt.show()

Chuli('Wave Files/a0.wav')
# for i in range(4):
#     Chuli('Wave Files/a%d.wav' % i)
#
# for i in range(4):
#     Chuli('Wave Files/b%d.wav' % i)
#
# for i in range(4):
#     Chuli('Wave Files/c%d.wav' % i)