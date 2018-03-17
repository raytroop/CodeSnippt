#include <iostream>
using namespace std;


int main()
{
	int ia[] = {0, 1, 2, 3, 4, 5, 6, 7, 8, 9};
	cout << sizeof(ia) << endl;

	decltype(ia) ib = {0, 1, 2};		// 维度是数组类型的一部分， ib也是维度为10的数组
	cout << sizeof(ib) << endl;	

	return 0;
}

// 40
// 40
