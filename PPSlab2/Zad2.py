import numpy as np
import matplotlib.pyplot as plt


def display_sin(min, max):
    x = np.arange(min, max, 0.1)
    y = np.sin(x)

    plt.plot(x, y, color="darkblue")
    plt.show()


min = float(input("Podaj zakres dolny: "))
max = float(input("Podaj zakres górny: "))
display_sin(min, max)