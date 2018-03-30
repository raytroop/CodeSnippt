#include "template.h"

extern template class Blob<int>;
extern template bool compare(const int&, const int&);
// -rw-rw-r-- 1 rtp rtp 2.6K Mar 27 19:27 templateApplication.o, using `extern template`
// -rw-rw-r-- 1 rtp rtp 3.3K Mar 27 19:28 templateApplication.o, comment 'extern template`'

int main()
{	
	int a=1, b=2;
	float c=3.1, d=4.2;
	Blob<int> obji(a);
	Blob<float> objf(c);
	bool i = compare(a, b);
	bool j = compare(c, d);
	return 0;
}

