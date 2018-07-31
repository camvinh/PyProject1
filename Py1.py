import numpy as np
from numpy.fft import fft
import matplotlib.pyplot as plt
from matplotlib.pyplot import plot, show
x = np.linspace(0, 1, 1400)
y = 7*np.sin(2*np.pi*180*x) + 2.8*np.sin(2*np.pi*390*x) + 5.1*np.sin(2*np.pi*600*x) + 2.3 * np.random.rand(len(x))

yy = fft(y)
yreal = yy.real
yimag = yy.imag

yf = abs(fft(y))
yf1 = abs(fft(y))/len(x)
yf2 = yf1[range(int(len(x)/2))]

xf = np.arange(len(y))
xf1 = xf
xf2 = xf[range(int(len(x)/2))]


plt.subplot(221)
plt.plot(xf, yimag)
plt.title('Original wave')

plt.subplot(222)
plt.plot(xf, yf, 'r')
plt.title('FFT of Mixed wave(two sides frequency range)',fontsize=7,color='#7A378B')

plt.subplot(223)
plt.plot(xf1, yf1, 'g')
plt.title('FFT of Mixed wave(normalization)',fontsize=9,color='r')

plt.subplot(224)
plt.plot(xf2, yf2, 'b')
plt.title('FFT of Mixed wave',fontsize=10,color='#F08080')

plt.show()

a = np.arange(0,3,0.01)
b = 3*np.sin(2*np.pi*33*a +200)+1.89*np.sin(2*np.pi*21*a+200)+ 2.7*np.sin(2*np.pi*15*a+200)+ 1.2*np.random.rand(len(a))+ 5*np.random.rand(len(a))+ 7*np.random.rand(len(a))


fb = abs(fft(b))/len(a)
fb[0]=fb[len(fb)-1]
fa = np.arange(len(b))
#print(fb)
#plt.subplot(111)
plt.plot(a,b)
plt.show()

#plt.subplot(112)
plt.plot(fa,fb)


plt.show()

