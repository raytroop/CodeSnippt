#include <iostream>
#include <vector>
#include <sstream>
#include <fstream>
using namespace std;

// phonebook.txt
// morgan  464641313 4646121445
// drew	955512444
// lee		625514588	455545458	1256485478

struct PersonInfo
{
	string name;
	vector<string> phone;
};

int main()
{
	ifstream infile("phonebook.txt");
	string line, word;
	vector<PersonInfo> people;
	while(getline(infile, line))
	{
		PersonInfo info;
		istringstream record(line);
		record >> info.name;
		while(record >> word)
			info.phone.push_back(word);
		people.push_back(info);

	}

	for(auto info: people)
	{
		cout << info.name << endl;
	}

	return 0;
}

