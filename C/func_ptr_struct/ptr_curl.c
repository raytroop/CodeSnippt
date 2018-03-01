#include<stdio.h>

int main()
{
	int my_num = 911;
	int * a = &my_num; // OK
	int (*b) = &my_num;
	printf("a num:%d\n", *a);
	printf("b num:%d\n", *b);
	printf("a==b:%d\n", a==b);

	// ptr_curl.c:11:10: error: ‘c’ undeclared (first use in this function)
	// (int *) is "expicitly converting" to int pointer
	// (int *) c = &my_num;  // ERROR
}