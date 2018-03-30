from distutils.core import setup, Extension
from Cython.Build import cythonize
ext = Extension(name="wrap_fib", 
				sources=["wrap_fib.pyx"], 
				library_dirs=["."], 
				libraries=["fib"] )
setup(ext_modules=cythonize(ext))