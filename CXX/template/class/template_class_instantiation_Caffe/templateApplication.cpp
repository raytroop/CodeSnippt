#include "template.h"


int main()
{	
	int a=1;
	float c=3.1;
	Blob<int> obji(a);
	Blob<float> objf(c);
	obji.read();
	objf.read();
	return 0;
}

