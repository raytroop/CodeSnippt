// g++ -std=c++11 myAdd_demo.cpp myAdd.cpp
#include "myAdd.h"
#include <iostream>
using namespace std;


int main()
{
	int a=1;
	int b=2;
	float c=3.1, d=4.2;
	cout << myAdd(a, b) << endl;

	cout << myAdd(c, d) << endl;
	// If we comment `template float myAdd<float>(float a, float b);` in `myAdd.cpp` 
	// undefined reference to `float myAdd<float>(float, float)'
	// collect2: error: ld returned 1 exit status
	// In this function template orgnization, we can just use that type function instantiated in `myAdd.cpp` 
	// I think so do class template
	return 0;
}