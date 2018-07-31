import numpy as np
from tftb.generators import fmsin, fmconst, amgauss
from scipy.signal.windows import kaiser
from tftb.processing.reassigned import  spectrogram
from pyhht.emd import EMD
import matplotlib.pyplot as plt
from scipy import signal
from scipy.io import wavfile

freq, x =wavfile.read('Wave Files/a2.wav')
t = np.arange(0, x.size/freq, 1/freq)
#
#
#
# N = 2001
# T = np.arange(1, N + 1, step=4)
# t = np.arange(1, N + 1)
#
# p = N / 2
#
# fmin1 = 1.0 / 64
# fmax1 = 1.5 * 1.0 / 8
# x1 = fmsin(N, fmin1, fmax1, p, N / 2, fmax1)[0]
#
# #x1 = np.sin(2*np.pi*50*t)+np.sin(2*np.pi*150*t**3)
#
# print(len(x1))
#
# fmin2 = 1.0 / 32
# fmax2 = 1.5 * 1.0 / 4
# x2 = fmsin(N, fmin2, fmax2, p, N / 2, fmax2)[0]
#
# print(len(x2))
#
# f0 = 1.5 * 1.0 / 16
#
# x3 = amgauss(N, N / 2, N / 8) * fmconst(N, f0)[0]
#
# a1 = 1
# a2 = 1
# a3 = 1
#
# x = np.real(a1 * x1 + a2 * x2 + a3 * x3)
# x = x / np.max(np.abs(x))
#
# decomposer = EMD(x)
# imf = decomposer.decompose()
#
# n_freq_bins = 256

short_window_length = 127
beta = 3 * np.pi
window = kaiser(short_window_length, beta=beta)
plt.figure(figsize=(15,15))
plt.plot(x)
plt.show()
f, t, Sxx = signal.spectrogram(x,freq)
print('f')
print(f)
print('t')
print(t.shape)
print('Sxx')
print(Sxx.shape)

# for i in range(0,5):
#      print(Sxx[0][i])
_positon = np.argmax(Sxx)
print(_positon)
m, n = divmod(_positon, Sxx.shape[1])
print('%d, %d'%(m,n))
print('f = %f'%f[m])
print('t = %f'%t[n])
print('Sxx = %f'%Sxx[m,n])
plt.pcolormesh(t, f, Sxx)
plt.ylabel('Frequency [Hz]')
plt.xlabel('Time [sec]')
plt.show()

f1 = f[:6]
Sxx1 = Sxx[:6,:]
plt.pcolormesh(t, f1, Sxx1)
plt.ylabel('Frequency [Hz]')
plt.xlabel('Time [sec]')
plt.show()



# _, re_spec_sig, _ = spectrogram(x, t, n_freq_bins, window)
# _, re_spec_imf1, _ = spectrogram(imf[0, :], t, n_freq_bins, window)
# _, re_spec_imf2, _ = spectrogram(imf[1, :], t, n_freq_bins, window)
# _, re_spec_imf3, _ = spectrogram(imf[2, :], t, n_freq_bins, window)
#
# fig = plt.figure(figsize=(15,15))
# for i, rspec in enumerate([re_spec_sig, re_spec_imf1, re_spec_imf2,
#                            re_spec_imf3]):
#     rspec = np.abs(rspec)[:128, :]
#     ax = fig.add_subplot(2, 2, i + 1)
#     ax.imshow(np.flipud(rspec), extent=[0, 1, 0, 1])
#     ax.tick_params(which='both', left=False, bottom=False, labelleft=False,
#             labelbottom=False)
#     ax.set_xlabel('time')
#     ax.set_ylabel('frequency')
#     if i == 0:
#         ax.set_title('signal')
#     else:
#         ax.set_title('mode #{}'.format(i))
# plt.show()