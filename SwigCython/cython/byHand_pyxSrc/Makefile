all:
	cython --cplus fib.pyx # --> outputs fib.cpp
	g++ -std=c++11 -shared -fPIC fib.cpp -o fib.so `python-config --includes` `python-config --libs`
clean:
	-rm *.so *.so *.c *.out

# cython
# --cplus 	Output a C++ rather than C file.
# -2 		Compile based on Python-2 syntax
# 				and code semantics.
# -3 		Compile based on Python-3 syntax
# 				and code semantics.