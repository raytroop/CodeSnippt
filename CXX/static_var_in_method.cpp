#include <iostream>
using namespace std;


class A {
public:
   void foo() {
      static int i=0;
      i++;
      cout << i << endl;
   }
};


int main()
{
	A obj1, obj2, obj3;
	obj1.foo();
	obj1.foo();
	obj2.foo();
	obj3.foo();
}

// rtp@ubuntu:~/test$ g++ -std=c++11 static.cpp 
// rtp@ubuntu:~/test$ ./a.out 
// 1
// 2
// 3
// 4