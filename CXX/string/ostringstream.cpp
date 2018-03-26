#include <string>
#include <sstream>
#include <iostream>
using namespace std;

string shape_string() {
    ostringstream stream;
    for (int i = 0; i < 4; ++i) {
      stream << i << " ";
    }
    return stream.str();
}


int main()
{
	string my_str(shape_string());
	cout << my_str << endl;
}

