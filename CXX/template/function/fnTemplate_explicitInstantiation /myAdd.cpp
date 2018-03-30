#include "myAdd.h"


template<typename Dtype>
Dtype myAdd(Dtype a, Dtype b)
{
	return a + b;
}

template int myAdd<int>(int a, int b);
template float myAdd<float>(float a, float b);