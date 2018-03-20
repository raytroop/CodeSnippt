#include <iostream>
#include <string>
using namespace std;


string::size_type sumLength(const string& s1, const string& s2)
{
	return s1.size() + s2.size();
}

string::size_type largerLenth(const string& s1, const string& s2)
{
	return (s1.size() > s2.size()) ? s1.size() : s2.size();
}

decltype(sumLength) *getFcn(const string& sel)
{
	if(sel == "sum")
		return sumLength;	// or `&sumLength`
	else
		return largerLenth;	// or `&largerLength`
}

int main()
{
	string s1("Hello");
	string s2("boy");
	string::size_type sz_sum = sumLength(s1, s2);
	string::size_type sz_larger = largerLenth(s1, s2);

	cout << sz_sum << endl;
	cout << sz_larger << endl;

	auto fcn = getFcn("sum");
	cout << fcn(s1, s2) << endl;	// or `(*fcn)(s1, s2)`
	auto fcn2 = getFcn("larger");
	cout << fcn2(s1, s2) << endl;	// or `(*fcn2)(s1, s2)`
	return 0;
}

// rtp@ubuntu:~/test$ g++ -std=c++11 func_ptr.cpp 
// rtp@ubuntu:~/test$ ./a.out 
// 8
// 5
// 8
// 5