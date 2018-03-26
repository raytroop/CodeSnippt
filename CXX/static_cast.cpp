#include <iostream>
using namespace std;


int main()
{
	int a = 11;
	void *vp = &a;
	int *ip = static_cast<int*>(vp);
	cout << *ip << endl;

	const int b = 21;
	const void *cvp = &b;
	// const int *ip2 = static_cast<int*>(cvp);	// error: static_cast from type ‘const void*’ to type ‘int*’ casts away qualifiers
	// int *ip2 = static_cast<int*>(cvp);		// error: static_cast from type ‘const void*’ to type ‘int*’ casts away qualifiers
	// int *ip2 = static_cast<const int*>(cvp);	// error: invalid conversion from ‘const int*’ to ‘int*’ [-fpermissive]
	const int *ip2 = static_cast<const int*>(cvp);	// OK
	cout << *ip2 << endl;
	const char *ip3 = static_cast<const char*>(cvp);	// syntax is right, but `char` is not same with original `int`
	cout << *ip3 << endl;
	return 0;
}

// rtp@ubuntu:~/test$ g++ -std=c++11 static_cast.cpp 
// rtp@ubuntu:~/test$ ./a.out 
// 11
// 21
// 
