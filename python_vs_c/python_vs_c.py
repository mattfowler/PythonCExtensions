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

if __name__ == '__main__':

    lens = range(10, 300, 10)
    lp_time = []
    py_time = []
    np_time = []
    c_time = []

    for l in lens:
        rands = [random.random() for _ in range(0, l)]
        numpy_rands = np.array(rands)
        py_time = np.append(py_time, timeit.timeit(lambda: standard_deviation(rands), number=10000))
        np_time = np.append(np_time, timeit.timeit(lambda: np.std(numpy_rands), number=10000))
        c_time = np.append(c_time, timeit.timeit(lambda: std.standard_dev(rands), number=10000))
    data = np.array([np.transpose(py_time), np.transpose(np_time), np.transpose(c_time)])

    df = pd.DataFrame(data.transpose(), index=lens, columns=['Python', 'Numpy', 'C++'])
    plt.figure()
    df.plot()
    plt.legend(loc='best')
    plt.ylabel('Time (Seconds)')
    plt.xlabel('Number of Elements')
    plt.title('10k Runs of Standard Deviation')
    plt.savefig('python_vs_c.png')
