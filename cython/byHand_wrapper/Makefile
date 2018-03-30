wrapper:
	cython fib_wrapper.pyx
	g++ -std=c++11 -shared -fPIC fib_wrapper.c fib.cpp -o fib_wrapper.so -I. `python-config --includes` `python-config --libs`
cppLib:
	g++ -std=c++11 -shared -fPIC fib.cpp -o libfib.so
.PHONY: clean
clean:
	-rm *.so *.so *.c *.out
