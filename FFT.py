import numpy as np
from scipy import fftpack
import matplotlib.pyplot as plt
import peakutils as pk
time_step = 0.001
period = 0.04
t = np.arange(0, 5, time_step)
sig = 83*np.sin(2*7*np.pi*t)+90*np.sin(2*4*np.pi*t**2)+50*t**2
#sig = np.sin(2*np.pi*7*t)+np.cos(2*8*np.pi*t)+3*t
sample_freq = fftpack.fftfreq(sig.size, d=time_step)
sig_fft = fftpack.fft(sig)
sig_fft[0] = 0
shifted = np.fft.fftshift(sig_fft)

#print(sample_freq)
#print(abs(sig_fft))

plt.figure(figsize= (15,10))

plt.subplot(221)
plt.plot(t,sig_fft)
plt.title('sig_fft')

re_fft = (abs(sig_fft)[:int(len(sample_freq)/2)])/len(t)*2
plt.subplot(222)
plt.plot(sample_freq[:int(len(sample_freq)/2)], re_fft)
plt.title('abs(sig_fft)')

plt.subplot(223)
plt.plot(shifted)
plt.title('shifted')

plt.subplot(224)
plt.plot(abs(shifted))
plt.title('abs(shifted)')

plt.show()
#print(sig_fft)

pk_id = pk.indexes(re_fft,  thres=0.1, min_dist=2)
print(np.max(re_fft[pk_id]))
print(np.min(re_fft[pk_id]))
for id in pk_id:
    print('freq: %fHz, Value: %f' %(sample_freq[:int(len(sample_freq)/2)][id], re_fft[id]))

a=[1,2,3]
b=[4,5,6]
c=[5,6,7,8,9,10]
d=list(zip(a,b))
e=list(zip(a,c))
print(d)
print(e)