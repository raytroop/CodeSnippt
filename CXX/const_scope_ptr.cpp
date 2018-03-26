#include <vector>
#include <iostream>
using namespace std;
// work around const object by ptr
// `const` apply to the whole object, but we can change val pointed by ptr contained in object

struct item
{
	int a;
	int b;
};

int main()
{
	item it1{1,2};
	cout << it1.a << ", " << it1.b << endl;
	item it2{3, 4};
	const vector<item> vIt{it1, it2};
	cout << vIt[0].a << endl;
	cout << vIt[1].b << endl;
	// vIt[0].a = 11;	// error: assignment of member ‘item::a’ in read-only object

	const vector<item>& rVit = vIt;	
	// rVit[0].a = 11;	// error: assignment of member ‘item::a’ in read-only object

	const vector<item*> vItPtr{&it1, &it2};
	cout << (vItPtr[0]->a) << endl;
	item it3{5, 6};
	// vItPtr.push_back(&it3);	// error: passing ‘const std::vector<item*>’ as ‘this’ argument discards qualifiers [-fpermissive]
	vItPtr[0]->a = 11;	// OK
	cout << (vItPtr[0]->a) << endl;
 	return 0;
}


// rtp@ubuntu:~/test$ g++ -std=c++11 const_scope.cpp 
// rtp@ubuntu:~/test$ ./a.out 
// 1, 2
// 1
// 4
// 1
// 11