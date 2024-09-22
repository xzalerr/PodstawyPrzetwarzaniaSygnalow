import datetime
import numpy as np


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


def fft(x):
    return np.fft.fft(x)


sr = 1000
t, y = create_signal(0, 1, sr)

start_custom_dft = datetime.datetime.now()
X = dft(y)
end_custom_dft = datetime.datetime.now()
time_custom_dft = end_custom_dft - start_custom_dft

start_fft = datetime.datetime.now()
Y = fft(y)
end_fft = datetime.datetime.now()
time_np_fft = end_fft - start_fft

print("Time for custom DFT:", time_custom_dft)
print("Time for NumPy FFT:", time_np_fft)
