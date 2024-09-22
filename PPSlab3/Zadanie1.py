import numpy as np
import matplotlib.pyplot as plt


def create_signal(min, max, sr):
    t = np.arange(min, max, 1 / sr)
    y = np.sin(2 * np.pi * 5 * t)
    return t, y


def dft(x):
    N = len(x)
    n = np.arange(N)
    k = n.reshape((N, 1))
    e = np.exp(-2j * np.pi * k * n / N)

    X = np.dot(e, x)

    return X


sr = 1000

t, y = create_signal(0, 1, sr)
X = dft(y)

N = len(X)
n = np.arange(N)
T = N / sr
plt.plot(np.abs(X)[:N//2])
plt.xlabel('Freq (Hz)')
plt.ylabel('DFT Amplitude |X(freq)|')
plt.show()
