import numpy as np
import pywt
import matplotlib.pyplot as plt
from PyEMD import EMD
sig= np.loadtxt('a0.txt')
print(type(sig))
print(sig)
print(sig.shape)
coeff_list = [sig, None]
print(type(coeff_list))
print(len(coeff_list))

w=pywt.waverec(coeff_list, pywt.Wavelet('sym5'))
freq=44100
t=np.arange(0,w.size/freq,1/freq)

IMF = EMD().emd(w,t)
N = IMF.shape[0]+1


print(len(w))
plt.plot(w)
plt.show()