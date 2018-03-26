#include <iostream>
#include <string>
using namespace std;


int main()
{	
	char c = 'a';
	const char *pc = &c;
	// *pc = 'b';	// error: assignment of read-only location ‘* pc’ 
	char *p = const_cast<char*>(pc);	//  cast away the const
	cout << *pc << endl;
	*p = 'z';	// change original low-level const
	cout << *pc << endl;

	const char *cp;
	static_cast<string>(cp);	// OK, cast type char* to type string
	// const_cast<string>(cp);	// Error, const_cast can NOT cast type but const properity
	const_cast<char*>(cp);	// OK
	return 0;
}