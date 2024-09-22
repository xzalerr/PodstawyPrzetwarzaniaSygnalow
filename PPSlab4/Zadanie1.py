import numpy as np
import matplotlib.pyplot as plt


def create_signal(f1, f2, f3, sr):
    t = np.arange(0, 10, 1 / sr)
    y1 = np.sin(2 * np.pi * f1 * t)
    y2 = np.sin(2 * np.pi * f2 * t)
    y3 = np.sin(2 * np.pi * f3 * t)
    y = y1 + y2 + y3
    return t, y


def dft(x):
    N = len(x)
    n = np.arange(N)
    k = n.reshape((N, 1))
    e = np.exp(-2j * np.pi * k * n / N)

    X = np.dot(e, x)

    return X


sr = 1000
t, y = create_signal(1, 23, 126, sr)
X = dft(y)
N = len(X)
fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(10, 8))
ax1.plot(np.abs(X)[:N//2])
ax1.set_xlabel('Freq (Hz)')
ax1.set_ylabel('DFT Amplitude')
ax2.specgram(y, sr)
ax2.set_xlabel('Time [sec]')
ax2.set_ylabel('Frequency [Hz]')
plt.show()