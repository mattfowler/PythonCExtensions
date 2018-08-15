import matplotlib
matplotlib.use('Agg')

import numpy as np
import random
import timeit
import math
from matplotlib import pyplot as plt
import std
import numba

from tqdm import tqdm as progress_bar


def mean(lst):
    return sum(lst) / len(lst)


def standard_deviation(lst):
    m = mean(lst)
    variance = sum([(value - m) ** 2 for value in lst])
    return math.sqrt(variance / len(lst))

@numba.jit(numba.double(numba.double[:]), nopython=True)
def numba_standard_deviation(lst):
    return np.std(lst)

@numba.jit(numba.double(numba.double[:]), nopython=True)
def numba_longer_standard_deviation(lst):
    m = np.mean(lst)
    variance = np.sum((lst - m) ** 2)
    return math.sqrt(variance / len(lst))


if __name__ == '__main__':
    fig, axs = plt.subplots(1,2,figsize=(14,6))

    for ax in axs:
        low = ax is axs[0]

        lens = range(10, 300, 10) if low else range(1000,30000,1000)
        py_time = []
        np_time = []
        numba1_time = []
        numba2_time = []
        c_time = []

        for l in progress_bar(lens, desc = 'Lower' if low else 'Upper'):
            rands = [random.random() for _ in range(l)]
            numpy_rands = np.array(rands)

            numba1_time.append(timeit.timeit(lambda: numba_standard_deviation(numpy_rands), number=1000))
            numba2_time.append(timeit.timeit(lambda: numba_longer_standard_deviation(numpy_rands), number=1000))
            np_time.append(timeit.timeit(lambda: np.std(numpy_rands), number=1000))
            c_time.append(timeit.timeit(lambda: std.standard_dev(rands), number=1000))
            if low:
                py_time.append(timeit.timeit(lambda: standard_deviation(rands), number=1000))


        ax.plot(lens, c_time, label='C++')
        ax.plot(lens, np_time, label='Numpy')
        ax.plot(lens, numba1_time, label='Numba np.std')
        ax.plot(lens, numba2_time, label='Numba longer')
        if low:
            ax.plot(lens, py_time, label='Python')

        ax.legend(loc='best')
        ax.set_ylabel('Time (Seconds)')
        ax.set_xlabel('Number of Elements')
        ax.set_title('Comparison of std dev performance')

    plt.savefig('results.png')
