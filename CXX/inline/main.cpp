// main.cpp

#include "A.h"
#include <iostream>

// if we comment the following inline block: 
// main.cpp:(.text+0x35): undefined reference to `A::max()'
// collect2: error: ld returned 1 exit status
inline int A::max()
{
	return a > b? a : b;
}

// // inline function only work in source file including its definition 
// // rather than just declaration
// // so, we had better merge A.cpp into A.h, in this way we need inline definition here

int main()
{
	A a(3, 5);
	std::cout << a.max() << std::endl;
	return 0;
}