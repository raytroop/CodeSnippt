#include <iostream>
#include <cstring>
using namespace std;

// OK,  const and pointer
// string constant work with `const char*` rather than `char*`
const char* Func()
{
	const char *ptr = "hello world";	// `字符串常量`存放在程序的`静态数据区`
	cout << sizeof(ptr) << endl;		// 4
	cout << strlen(ptr) << endl;		// 11
	return ptr;		// 返回字符串常量的地址
}

int main()
{
	const char *ptr = Func();	
	return 0;
}


// array 
// Still work but
//  warning: address of local variable 'str' returned [-Wreturn-local-addr]
// char* Func_heap()
// {
// 	char str[] = "hello world";		// str数组创建在函数堆栈上， 并用字符串
// 	cout << sizeof(str) << endl;	// 常量初始化， 在末尾自动添加"\0"
// 	cout << strlen(str) << endl; 
// 	return str;		// 该语句存在隐患， str指向的内存单元将被释放
// }

// int main()
// {
// 	char *p = Func_heap();
// 	return 0;
// }


// const array
// Still warning 
// warning: address of local variable 'str' returned [-Wreturn-local-addr]
// const char* Func_heap()
// {
// 	const char str[] = "hello world";		
// 	cout << sizeof(str) << endl;	
// 	cout << strlen(str) << endl; 
// 	return str;		
// }

// int main()
// {
// 	const char *p = Func_heap();
// 	return 0;
// }


// Still warning
// warning: ISO C++ forbids converting a string constant to 'char*' [-Wwrite-strings]
// char* Func()
// {
// 	char *ptr = "hello world";	// warning: ISO C++ forbids converting a string constant to 'char*' [-Wwrite-strings] 
// 	cout << sizeof(ptr) << endl;		// 4
// 	cout << strlen(ptr) << endl;		// 11
// 	return ptr;		// 返回字符串常量的地址
// }

// int main()
// {
// 	char *ptr = Func();	
// 	return 0;
// }