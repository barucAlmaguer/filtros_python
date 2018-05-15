import numpy as np
import matplotlib.pyplot as plt
from scipy import signal
from scipy.interpolate import UnivariateSpline

def mean_average(points, count):
    xf = []
    for i in range(count, len(points)):
        xf.append(np.mean(points[i-count:i]))
    return xf

def main():
    mean_count = 5
    t = np.linspace(0, 20, 250)
    x = 0.2 * np.sin(1.2 * np.sqrt(t))
    x2 = list(x)
    x += 0.05 * np.sin(2 * np.pi * 5.0 * t)
    xf = mean_average(x, mean_count)
    #xf_sp = signal.spline_filter(x)
    xf_uni = UnivariateSpline(t, x)
    print(t)
    print(x)
    plt.plot(t, x)
    plt.plot(t[mean_count:], xf)
    plt.plot(t, xf_uni)
    plt.show()

if __name__ == '__main__':
    main()