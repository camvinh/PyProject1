from PyEMD import EMD
import numpy as np
import pylab as plt
import peakutils as pk

# Define signal
t = np.linspace(0.082, 2.128, 2000)
time_step = 1/2000
s = np.sin(40 * np.log(t)) * np.sign((np.log(t)))+np.random.rand(t.size)
#s = 83*np.sin(2*7*np.pi*t)+90*np.sin(2*4*np.pi*t**2)+50*t**2
+3*t**5
# Execute EMD on signal
IMF = EMD().emd(s,t)
N = IMF.shape[0]+1

# Plot results
plt.figure(figsize=(15,15))
plt.subplot(N,1,1)
plt.plot(t, s, 'r')
plt.title("Input signal: $S(t)=83sin(14\pi t) + 90sin(8\pi t^2) + 50t^2 + noise$")
plt.xlabel("Time [s]")
xf=np.fft.fftfreq(t.size,time_step)[:int(len(t)/2)]
for n, imf in enumerate(IMF):
    #print(imf)
    print('*******************************************************')
    plt.subplot(N,1,n+2)
    imf_fft = abs(np.fft.fft(imf))[:int(len(t)/2)]/len(t)*2
    pk_id = pk.indexes(imf_fft, thres=0.3, min_dist=3)
    for id in pk_id:
        print('freq: %dHz, Value: %f' % (xf[id], imf_fft[id]))

    #plt.plot(xf, imf_fft, 'g')
    plt.plot(t, imf, 'g')
    plt.title("IMF "+str(n+1))
    plt.xlabel("Time [s]")

plt.tight_layout()
plt.savefig('simple_example')
plt.show()