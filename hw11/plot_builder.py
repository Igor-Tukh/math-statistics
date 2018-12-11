import matplotlib.pyplot as plt
import numpy as np
import os

NUMBER_OF_EXPERIMENTS = 239239
a = 0.3
c = 1 / (2 * np.exp(-a) + 2 * a)
eps = 1e-9


def save_plot(filename, x_values, y_values):
    plt.clf()
    plt.plot(x_values, y_values)
    plt.savefig(filename)


def save_hist(filename, values):
    plt.clf()
    plt.hist(values, bins=5000)
    plt.savefig(filename)


def inverse(number_of_experiments):
    values = []

    for _ in range(number_of_experiments):
        y = np.random.uniform(0, 1)
        if y + eps < c * np.exp(-a):
            x = np.log(y / c)
        elif y > c * np.exp(-a) + 2 * c * a + eps:
            x = -np.log((1 - y) / c)
        else:
            x = y / c - np.exp(-a) - a
        values.append(x)

    values.sort()
    return values


def decomposition(number_of_experiments):
    values = []

    for _ in range(number_of_experiments):
        y = np.random.uniform(0, 1)
        if y + eps < c * np.exp(-a):
            x = -(np.random.exponential(1) + a)
        elif y > c * np.exp(-a) + 2 * c * a + eps:
            x = np.random.exponential(1) + a
        else:
            x = np.random.uniform(-a, a)  # Let's assume, that we have it. Anyway, we have uniform[0; 1] * 2 * a - a
        values.append(x)

    values.sort()
    return values


if __name__ == '__main__':
    for func, name in zip([inverse, decomposition], ['inverse', 'decomposition']):
        save_plot(os.path.join('plots', name), range(NUMBER_OF_EXPERIMENTS), func(NUMBER_OF_EXPERIMENTS))
        save_hist(os.path.join('hists', name), func(NUMBER_OF_EXPERIMENTS))
