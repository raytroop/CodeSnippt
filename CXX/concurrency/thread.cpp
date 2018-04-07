#include <thread>
#include <iostream>
#include <unistd.h>
using namespace std;


void hello()
{
	sleep(2);
	cout << "hello world, 2s" << endl;
	sleep(3);
	cout << "hello world, 5s" << endl;
}

class threadGuard
{
private:
	thread& t;
public:
	explicit threadGuard(thread& t_): t(t_) {}
	threadGuard(const threadGuard&) = delete;
	threadGuard& operator=(const threadGuard&)=delete;
	void operator()(){ hello();}
	~threadGuard()
	{
		if(t.joinable())
		{	
			cout << t.joinable() << endl;
			t.join();
			cout << t.joinable() << endl;
		}
	}
};

// int main()
// {
// 	thread t(hello);
// 	t.join();	// this will hold following code in `main()`
// 	cout << "Main thread" << endl;
// 	return 0;
// }

// rtp@ubuntu:~/test$ g++ -std=c++11 thread.cpp -lpthread
// rtp@ubuntu:~/test$ ./a.out 
// hello world, 2s
// hello world, 5s
// Main thread


int main()
{
	thread t(hello);
	threadGuard g(t);
	cout << "Main thread" << endl;
	return 0;
}

// rtp@ubuntu:~/test$ g++ -std=c++11 thread.cpp -lpthread
// rtp@ubuntu:~/test$ ./a.out 
// Main thread   // the local objects begin to be destroyed in reverse order of construction. 
// 1	// invoke `threadGuard` destructor, `t` is `joinable` for the moment
// hello world, 2s	// wait for the thead `t`(`hello`) to complete
// hello world, 5s
// 0	// `join()` can be called only ONCE for a given thread of execution


// ***************************************************************************
// If we comment `t.join()` at `class threadGuard` will raise error in runtime
// rtp@ubuntu:~/test$ g++ -std=c++11 thread.cpp -lpthread
// rtp@ubuntu:~/test$ ./a.out 
// Main thread
// 1
// 1
// terminate called without an active exception
// Aborted (core dumped