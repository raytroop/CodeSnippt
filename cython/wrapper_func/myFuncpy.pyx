cdef extern from "myFunc.hpp":  
    cdef int myFunc (int a, int b)  
    
  
def f(a,b):  
    print(a,b)  
    return myFunc(a,b)