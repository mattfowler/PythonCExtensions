import numpy as np
import random
import timeit
import math
import pandas as pd
from matplotlib import pyplot as plt
import std


def mean(lst):
    return sum(lst) / len(lst)


def standard_deviation(lst):
    m = mean(lst)
    variance = sum([(value - m) ** 2 for value in lst])
    return math.sqrt(variance / len(lst))

def mean_loop(lst):
    sum = 0.0
    for val in lst:
        sum = sum + val
    return sum / len(lst)


def standard_deviation_loop(lst):
    diffsquared = 0
    sum_diffsquared = 0
    average = mean_loop(lst)
    for val in lst:
        diffsquared = (val - average) ** 2
        sum_diffsquared = diffsquared + sum_diffsquared
    return (sum_diffsquared / len(lst)) ** (1 / 2)


if __name__ == '__main__':

    lens = range(10, 300, 10)
    lp_time = []
    py_time = []
    np_time = []
    c_time = []

    for l in lens:
        rands = [random.random() for _ in range(0, l)]
        numpy_rands = np.array(rands)
        lp_time = np.append(py_time, timeit.timeit(lambda: standard_deviation_loop(rands), number=10000))
        py_time = np.append(py_time, timeit.timeit(lambda: standard_deviation(rands), number=10000))
        np_time = np.append(np_time, timeit.timeit(lambda: np.std(numpy_rands), number=10000))
        c_time = np.append(c_time, timeit.timeit(lambda: std.standard_dev(rands), number=10000))
    data = np.array([np.transpose(lp_time), np.transpose(py_time), np.transpose(np_time), np.transpose(c_time)])

    df = pd.DataFrame(data.transpose(), index=lens, columns=['Python Loop', 'Python', 'Numpy', 'C++'])
    plt.figure()
    df.plot()
    plt.legend(loc='best')
    plt.ylabel('Time (Seconds)')
    plt.xlabel('Number of Elements')
    plt.title('10k Runs of Standard Deviation')
    plt.show()
