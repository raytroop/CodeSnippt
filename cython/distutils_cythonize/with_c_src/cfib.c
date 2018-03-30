// g++ -std=c++11 -shared -fPIC fib.cpp -o libfib.so
#include "cfib.h"
double cfib(int n) {
	int i;
	double a=0.0, b=1.0, tmp;
	for (i=0; i<n; ++i) {
		tmp = a; a = a + b; b = tmp;
	}
	return a;
}