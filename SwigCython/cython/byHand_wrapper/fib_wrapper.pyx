cdef extern from "fib.hpp":  
    cdef double cfib (int n)  
    
  
def pyfib(n):  
    print(n)  
    return cfib(n)