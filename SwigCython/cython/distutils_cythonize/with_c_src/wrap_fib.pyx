cdef extern from "cfib.h":  
    cdef double cfib (int n)  
    
  
def pyfib(n):  
    print(n)  
    return cfib(n)