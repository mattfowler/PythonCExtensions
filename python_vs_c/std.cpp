#include <vector>
#include <numeric>
#include <iterator>

#include <Python.h>

extern "C" {
    void initstd(void);
}

static double standardDeviation(std::vector<double> v)
{
    double sum = std::accumulate(v.begin(), v.end(), 0.0);
    double mean = sum / v.size();

    double squareSum = std::inner_product(v.begin(), v.end(), v.begin(), 0.0);
    return sqrt(squareSum / v.size() - mean * mean);
}

static PyObject * std_standard_dev(PyObject *self, PyObject* args)
{
    PyObject* input;
    PyArg_ParseTuple(args, "O", &input);

    int size = PyList_Size(input);

    std::vector<double> list;
    list.resize(size);

    for(int i = 0; i < size; i++) {
        list[i] = PyFloat_AS_DOUBLE(PyList_GET_ITEM(input, i));
    }

	return PyFloat_FromDouble(standardDeviation(list));
}

static PyMethodDef std_methods[] = {
	{"standard_dev", std_standard_dev,	METH_VARARGS,
	 "Return the standard deviation of a list."},
	{NULL,		NULL}		/* sentinel */
};

extern void initstd(void)
{
	PyImport_AddModule("std");
	Py_InitModule("std", std_methods);
}

int main(int argc, char **argv)
{
	Py_SetProgramName(argv[0]);

	Py_Initialize();

	initstd();

	Py_Exit(0);
}
