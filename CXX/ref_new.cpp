#include <iostream>
using namespace std;


int& func()
{
	int *intPtr = new int();
	return *intPtr;
}


int main()
{
	// [runtime error]
	// // *** Error in `./a.out': free(): invalid pointer: 
	// 0x00007ffc49b4cd94 ***
	// int a = func();
	// delete &a;

	int &b = func();	
	delete &b;	// OK


	return 0;
}