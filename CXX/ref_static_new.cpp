#include <iostream>
#include <map>
#include <string>
using namespace std;

typedef map<string, int> intRegistry;

intRegistry& Registry()
{
	static intRegistry* g_registry = new intRegistry;
	return *g_registry;
}

int main()
{
	intRegistry& registry_1 = Registry();
	registry_1["Queen"] = 167;
	intRegistry& registry_2 = Registry();
	registry_2["Stella"] = 168;
	auto map_it = registry_1.cbegin();
	while(map_it != registry_1.cend())
	{
		cout << map_it->first <<": " 
		<< map_it->second << endl;
		++map_it;
	}

	cout << "Add more" << endl;
	registry_2["Victoria"] = 170;
	map_it = registry_1.cbegin();
	while(map_it != registry_1.cend())
	{
		cout << map_it->first <<": " 
		<< map_it->second << endl;
		++map_it;
	}
	return 0;
}

// rtp@ubuntu:~/test$ g++ -std=c++11 ref_static_new.cpp 
// rtp@ubuntu:~/test$ ./a.out 
// Queen: 167
// Stella: 168
// Add more
// Queen: 167
// Stella: 168
// Victoria: 170