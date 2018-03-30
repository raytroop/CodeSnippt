def fib(int n):
	"""
	Returns the nth Fibonacci number.
	"""
	cdef int i
	cdef double a=0.0, b=1.0
	for i in range(n):
		a, b = a + b, a
	return a