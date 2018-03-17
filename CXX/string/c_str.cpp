#include <iostream>
#include <string>
#include <cstring>
using namespace std;

int main()
{
	string s("Hello World");
	cout << s.size() << endl;
	const char *str = s.c_str();		// str是指向数组首元素的指针
	cout << strlen(str) << endl;
	// const char *str2 = "Hello World";
	// cout << strlen(str2[0]) << endl;
	return 0;
}