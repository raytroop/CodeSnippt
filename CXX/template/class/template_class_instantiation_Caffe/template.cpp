#include "template.h"
#include <iostream>
using namespace std;


template<typename T>
Blob<T>::Blob():_a(0) {}

template<typename T>
Blob<T>::Blob(T a):_a(a)  {}

template<typename T>
void Blob<T>::read()
{
	cout << _a << endl;
}

// explicit instantiate class 
template class Blob<int>;
template class Blob<float>;
