import random
import os

import matplotlib.pyplot as plot

from scipy.stats import chi2, norm


def get_results(max_n, gamma, mode):
    if mode == 'a':
        return [sum([sum([random.normalvariate(0, 1) ** 2
                          for _ in range(1, n)]) / 10 * (
                                 1 / chi2.ppf((1 - gamma) / 2, n) - 1 / chi2.ppf((1 + gamma) / 2, n))
                     for _ in range(10)])
                for n in range(1, max_n)]

    return [sum([sum([random.normalvariate(0, 1)
                      for _ in range(1, n)]) ** 2 / 10 / n * (
                             1 / (norm.ppf((3 - gamma) / 4) ** 2) - (1 / norm.ppf((3 + gamma) / 4) ** 2))
                 for _ in range(10)])
            for n in range(1, max_n)]


def save_plot(filename, x_values, y_values):
    plot.clf()
    plot.plot(x_values, y_values)
    plot.savefig(filename)


if __name__ == '__main__':
    max_n = 5000
    gamma = 0.5

    x_values = [i for i in range(1, max_n)]
    for mode in ['a', 'b']:
        y_values = get_results(max_n, gamma, mode)
        save_plot(os.path.join('plots', 'plot_{mode}'.format(mode=mode)), x_values, y_values=y_values)
