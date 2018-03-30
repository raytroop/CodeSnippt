extern "C" {
#include <cblas.h>
}
#include <iostream>
using namespace std;
// void caffe_cpu_gemv<float>(	const CBLAS_TRANSPOSE TransA, 			
//								const int M,
//     							const int N, 
// 								const float alpha, 
// 								const float* A, 
// 								const float* x,
//     							const float beta, 
// 								float* y) 
// 功能： y=alpha*A*x+beta*y 
// 其中X和Y是向量，A 是矩阵 
// M：A 的行数 
// N：A 的列数 


void caffe_cpu_gemv(const CBLAS_TRANSPOSE TransA, const int M,
    const int N, const float alpha, const float* A, const float* x,
    const float beta, float* y) {
  cblas_sgemv(CblasRowMajor, TransA, M, N, alpha, A, N, x, 1, beta, y, 1);
}

int main()
{
	int M = 3;
	int N = 2;
	float alpha = 1;
	float beta = 1;
	float A[M*N] = {0,1,2,3,4,5};
	float x[N] = {1, 1};
	float y[M] = {1, 1, 1};

	caffe_cpu_gemv(CblasNoTrans, M, N, alpha, A, x, beta, y);

	for(int i=0; i<M*N; ++i){
		cout << A[i] << " ";
	}
	cout << endl;

	for(int i=0; i<M; ++i){
        cout << y[i] << " ";
  	}
  	cout << endl;

    return 0;
}

// rtp@ubuntu:~/CodeSnippt/CXX/blas/caffe_cpu_gemv$ make
// g++ -std=c++11 caffe_cpu_gemv.cpp -lcblas
// rtp@ubuntu:~/CodeSnippt/CXX/blas/caffe_cpu_gemv$ ./a.out 
// 0 1 2 3 4 5 
// 2 6 10