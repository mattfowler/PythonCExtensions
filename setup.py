from distutils.core import setup, Extension

std_module = Extension('std', sources=['python_vs_c/std.cpp'])

setup(name='std_performance',
      version='1.0',
      description='Module for calculating standard deviation.',
      ext_modules=[std_module])
