import matplotlib
matplotlib.use('Agg')

import numpy as np
import random
import timeit
import math
from matplotlib import pyplot as plt
import std

from tqdm import tqdm as progress_bar


def mean(lst):
    return sum(lst) / len(lst)


def standard_deviation(lst):
    m = mean(lst)
    variance = sum([(value - m) ** 2 for value in lst])
    return math.sqrt(variance / len(lst))


if __name__ == '__main__':
    for low in (True, False):
        lens = range(10, 300, 10) if low else range(1000,30000,1000)
        py_time = []
        np_time = []
        c_time = []

        for l in progress_bar(lens, desc = 'Lower' if low else 'Upper'):
            rands = [random.random() for _ in range(0, l)]
            numpy_rands = np.array(rands)
            if low:
                py_time = np.append(py_time, timeit.timeit(lambda: standard_deviation(rands), number=10000))
            np_time = np.append(np_time, timeit.timeit(lambda: np.std(numpy_rands), number=10000))
            c_time = np.append(c_time, timeit.timeit(lambda: std.standard_dev(rands), number=10000))

        plt.figure()

        if low:
            plt.plot(lens, py_time, label='Python')
        plt.plot(lens, np_time, label='Numpy')
        plt.plot(lens, c_time, label='C++')

        plt.legend(loc='best')
        plt.ylabel('Time (Seconds)')
        plt.xlabel('Number of Elements')
        plt.title('Comparison of std dev performance')
        plt.savefig('lower_results.png' if low else 'upper_results.png')
