#include <iostream>
using namespace std;


class myclass
{
private:
  int a;

public:
  myclass():a(0) 
  { cout << "default constructor" << endl;}
  myclass(int x):a(x) 
  { cout << "one argument constructor" << endl;}
  myclass(const myclass &cls)
  {
  	a = cls.a;
  	cout << "copy constructor" << endl;
  }

  myclass &operator=(const myclass& cls)
  {
  	a = cls.a;
  	cout << "assignment = operator" << endl;
  }
  int get()
  {
  	return a;
  }
};

int main()
{
	myclass obj;		// default constructor
	cout << obj.get() << endl;

	myclass obj2(11);	// one argument constructor	
	cout << obj2.get() << endl;

	myclass obj3(obj2);	// copy constructor
	cout << obj3.get() << endl;

	myclass obj4=obj3;	// copy constructor 		
	cout << obj4.get() << endl;

	// one argument constructor
	// but `error: conversion from ‘int’ to non-scalar type 
	// ‘myclass’ requested` if myclas(int x) declared as `explicit`
	myclass obj5 = 21;	
	cout << obj5.get() << endl;

}

// rtp@ubuntu:~/test$ g++ -std=c++11 copy_assign.cpp 
// rtp@ubuntu:~/test$ ./a.out 
// default constructor
// 0
// one argument constructor
// 11
// copy constructor
// 11
// copy constructor
// 11
// one argument constructor
// 21

