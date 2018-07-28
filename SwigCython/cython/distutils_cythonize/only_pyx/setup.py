# python setup.py build_ext --inplace
from distutils.core import setup
from Cython.Build import cythonize

setup(ext_modules=cythonize('fib.pyx'))
# cythonize calls the cython compiler on the .pyx source file or files, 
# and setup compiles the generated C or C++ code into a Python extension module.