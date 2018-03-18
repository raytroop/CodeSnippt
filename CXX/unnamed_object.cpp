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
  int get()
  {
  	return a;
  }
};

myclass myfunc_0()
{
  return myclass(); // default constructor
}

myclass myfunc_1()
{
  return myclass(11); // one argument constructor
}

myclass myfunc_2()  // same with myfunc_0
{
  return {};
}

myclass myfunc_3()  
{
  return {11};  // same with `return 11;`, one argument constructor
}

myclass myfunc_4()  
{
  myclass temp; // default constructor
  return temp;  
}

int main()
{
  myfunc_0();
  myfunc_1();
  myfunc_2();
  myfunc_3();
  myfunc_4();
  myclass obj(myfunc_4());  // just default constructor
  myclass obj2(obj);  // copy constructor
  return 0;
}

// rtp@ubuntu:~/test$ g++ -std=c++11 return_nameless.cpp 
// rtp@ubuntu:~/test$ ./a.out 
// default constructor
// one argument constructor
// default constructor
// one argument constructor
// default constructor
// default constructor
// copy constructor