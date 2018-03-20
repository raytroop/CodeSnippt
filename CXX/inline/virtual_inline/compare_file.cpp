// g++ -std=c++11 compare_file.cpp
#include <iostream>
#include <string>
#include <fstream>
using namespace std;


int main()
{
	ifstream file1("virtual_inline.inline.s"); 
	ifstream file2("virtual_inline.noinline.s");
	string line1, line2;
	bool same = true;
	while(getline(file1, line1) && getline(file2, line2))
	{
		if(line1 != line2)
		{
			same = false;
			break;
		}

	}
	file1.close();
	file2.close();

	cout << (same ? "They are same" : "They are different") << endl;

	return 0;
}

// rtp@ubuntu:~/test$ g++ -std=c++11 compare_file.cpp
// rtp@ubuntu:~/test$ ./a.out 
// They are same


// inline can be ommited in class 
