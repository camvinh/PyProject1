from scipy import signal
import matplotlib.pyplot as plt
import numpy as np
from scipy.io import wavfile

t = np.loadtxt('time.data')
sig = np.loadtxt('sig.data')

# freq, x = wavfile.read('Wave Files/a0.wav')
# t = np.arange(0, x.size / freq, 1 / freq)
# sig = x

# t = np.linspace(-1, 1, 200, endpoint=False)
# sig  = np.cos(2 * np.pi * 7 * t) + signal.gausspulse(t - 0.4, fc=2)
# plt.plot(t,sig)
# plt.show()
widths = np.arange(1, 128)
cwtmatr = signal.cwt(sig, signal.ricker, widths)
print(cwtmatr.shape)
plt.imshow(cwtmatr, extent=[-1, 1, 128, 1], cmap='PRGn', aspect='auto', vmax=abs(cwtmatr).max(), vmin=-abs(cwtmatr).max())
# plt.subplots_adjust(bottom=5, right=28, top=9)
cax = plt.axes([0.85, 0.1, 0.075, 0.8])
plt.colorbar(cax=cax)
plt.show()
