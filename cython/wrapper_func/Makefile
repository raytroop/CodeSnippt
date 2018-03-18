all:
	cython myFuncpy.pyx		# generate myFuncpy.c
	g++ -g -O2 -fpic -c myFuncpy.c -o myFuncpy.o `python-config --includes`		# compile myFuncpy.c
	g++ -g -O2 -fpic -c myFunc.cpp -o myFunc.o   # compile our myFunc.cpp		
	g++ -g -O2 -shared -o myFuncpy.so myFuncpy.o myFunc.o `python-config --libs`  # generate shared lib myFuncpy.so
	# In the end, `myFuncpy.so` is what we need. 
  
clean:
	rm -f myFuncpy.c *.o *.so 