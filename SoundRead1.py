from scipy.io import wavfile
import numpy as np
from scipy import fftpack
import matplotlib.pyplot as plt
import peakutils as pk

def chuli(path):
    freq, sig =wavfile.read(path)
    sample_freq = fftpack.fftfreq(sig.size, d=1/freq)
    sig_fft = fftpack.fft(sig)
    print(freq,sig.size)

    sample_freq = sample_freq[:int(len(sample_freq)/2)]
    sig_fft = abs(sig_fft[:sample_freq.size])/sample_freq.size*2
    t =np.arange(0,sig.size/freq,1/freq)

    plt.figure(figsize= (15,10))
    plt.subplot(2,1,1)
    plt.plot(t,sig)
    plt.title(path)

    print(sample_freq.size,sig_fft.size)

    plt.subplot(2,1,2)
    plt.plot(sample_freq,sig_fft)
    plt.show()

    print(path)
    pk_id = pk.indexes(sig_fft,  thres=0.3, min_dist=2)
    pk_max = np.max(sig_fft[pk_id])
    pk_min = np.min(sig_fft[pk_id])
    scl = 1/(pk_max)
    for id in pk_id:
        print('freq: %fHz, Value: %f' %(sample_freq[:int(len(sample_freq)/2)][id], (sig_fft[id])*scl))

    print('')
    print('***********************************************************************************************************')
    print('')

# for i in range(10):
#     chuli('a%d.wav' % i)
# for i in range(10):
#     chuli('b%d.wav' % i)
# for i in range(10):
#     chuli('c%d.wav' % i)

chuli('Wave Files/a0.wav')