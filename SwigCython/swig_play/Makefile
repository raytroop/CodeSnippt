all:
	swig -python example.i
	python setup.py build_ext --inplace
clean:
	rm *.so  example.py *wrap.c
	rm -r build
	rm -r __pycache__
