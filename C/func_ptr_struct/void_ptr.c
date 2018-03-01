#include<stdio.h>

typedef struct _test
{
	void (*ptr_func)();
} STest;

void display()
{
	printf("hello function\n");
}

void main()
{
	STest test;
	test.ptr_func = display;
	test.ptr_func();
}