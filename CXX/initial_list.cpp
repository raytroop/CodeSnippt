#include <iostream>
using namespace std;


class A{
public:
	A():a_(365) {}		// if remove `a_(365)`, `a_` will hold a random value
	A(int x): a_(x) {}
	int a_;
};


class B
{
public:
	B() {}		// call `A obj` default constructor
	B(int x): obj(x) {}
	A obj;
};


int main()
{
	B obj1;
	B obj2(11);
	cout << obj1.obj.a_ << endl;
	cout << obj2.obj.a_ << endl;
}


// rtp@ubuntu:~/CodeSnippt/CXX$ g++ initial_list.cpp 
// rtp@ubuntu:~/CodeSnippt/CXX$ ./a.out 
// 365
// 11
