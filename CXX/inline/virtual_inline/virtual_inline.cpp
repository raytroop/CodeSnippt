#include <iostream>
using namespace std;


class A
{
public:
	A(int x): data(x) 
	{ cout << "construted" << endl;}
	// virtual inline void get()	// 1 `g++ -std=c++11 virtual_inline.cpp  -S -o virtual_inline.inline.s`
	virtual void get()				// 2 `g++ -std=c++11 virtual_inline.cpp  -S -o virtual_inline.noinline.s`
	{
		cout << "data output:" << data<< endl;
	}
private:
	int data;
};


int main()
{
	A obj(365);
	obj.get();
	return 0;
}

