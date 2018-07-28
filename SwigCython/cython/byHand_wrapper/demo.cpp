#include "fib.hpp"
#include <iostream>
using namespace std;


int main(int argc, char **argv)
{	
	int n = atoi(argv[1]);
	double re = cfib(n);
	cout << re << endl;
	return 0;
}

// rtp@ubuntu:~/test$ g++ -std=c++11 demo.cpp -I. -L. -lfib
// rtp@ubuntu:~/test$ ./a.out 29
// 514229