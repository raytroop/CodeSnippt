#include<stdio.h>

typedef struct _test
{
	int (*ptr_func)();
} STest;

int display()
{
	printf("hello function\n");
	return 911;
}

void main()
{
	STest test;
	test.ptr_func = display; // same with &display
	int dt = test.ptr_func();
	printf("number is %d\n", dt);
}