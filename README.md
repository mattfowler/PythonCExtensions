# PythonCExtensions
Using a Python C extension and comparing its performance to NumPy and Python

Companion to [Speeding Up Python and Numpy](https://medium.com/coding-with-clarity/speeding-up-python-and-numpy-c-ing-the-way-3b9658ed78f4)

You need to build the C extension before running this. To build and install the extension run:

```python
python setup.py install
```

`python_vs_c.py` has a main method which will compare Python, NumPy and the C extension for small arrays and plot the performance with matplotlib.

`c_vs_numpy.py` has a main method which will compare NumPy and the C extension for larger arrays and plot the performance with matplotlib to see at which point NumPy will win performance wise.

The head of master will work with Python 3.7, for Python 2.7 see the `2.7` tag in this repository.
