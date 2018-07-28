#include<iostream>
#include"add.h"

using namespace std;

int main()
{
  int a = 1,b = 2;
  int c = add(a,b);
  cout << a << " + " << b << " = " << c << endl;
  return 0;
}
