import math
import random
import os

import matplotlib.pyplot as plot


class PlotBuilder(object):
    def __init__(self, generator, estimation, name, selection_size=100, runs=100, max_k=100, param=100):
        self.generator = generator
        self.estimation = estimation
        self.selection_size = selection_size
        self.name = name
        self.runs = runs
        self.max_k = max_k
        self.param = param

    def build_plot(self, plot_directory, filename):
        if not os.path.exists(plot_directory):
            os.makedirs(plot_directory)

        results = [self._get_standard_deviation(k) for k in range(1, self.max_k)]
        PlotBuilder.save_plot(os.path.join(plot_directory, filename), [k for k in range(1, self.max_k)], results)

    @staticmethod
    def save_plot(filename, x_values, y_values):
        plot.clf()
        plot.plot(x_values, y_values)
        plot.savefig(filename)

    def _get_estimation(self, k):
        values = [self.generator(self.param) ** k for _ in range(self.selection_size)]
        return self.estimation(self.selection_size, k, sum(values))

    def _get_standard_deviation(self, k):
        squares = [(self._get_estimation(k) - self.param) ** 2 for _ in range(self.runs)]
        return (sum(squares) / self.runs) ** 0.5


if __name__ == '__main__':
    uniformBuilder = PlotBuilder(lambda param: random.uniform(0, param),
                                 lambda number, k, values_sum: ((values_sum / number) * (k + 1)) ** (1 / k),
                                 "uniform")

    expovariateBuilder = PlotBuilder(random.expovariate,
                                     lambda number, k, values_sum: (math.factorial(k) * number / values_sum) ** (1 / k),
                                     "expovariate")

    for plotBuilder in {uniformBuilder, expovariateBuilder}:
        plotBuilder.build_plot("plots", plotBuilder.name)
