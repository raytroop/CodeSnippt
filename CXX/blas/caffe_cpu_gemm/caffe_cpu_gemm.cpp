extern "C" {
#include <cblas.h>
}
#include <iostream>
using namespace std;
// void caffe_cpu_gemm<float>(	const CBLAS_TRANSPOSE TransA,
//     							const CBLAS_TRANSPOSE TransB, 
//								const int M, 
//								const int N, 
//								const int K,
//     							const float alpha, 
//								const float* A, 
//								const float* B, 
//								const float beta,
//     							float* C)
// 功能： C=alpha*A*B+beta*C 
// A,B,C 是输入矩阵（一维数组格式） 
// CblasRowMajor :数据是行主序的（二维数据也是用一维数组储存的） 
// TransA, TransB：是否要对A和B做转置操作（CblasTrans CblasNoTrans） 
// M： A、C 的行数 
// N： B、C 的列数 
// K： A 的列数， B 的行数 

void caffe_cpu_gemm(const CBLAS_TRANSPOSE TransA,
    const CBLAS_TRANSPOSE TransB, const int M, const int N, const int K,
    const float alpha, const float* A, const float* B, const float beta,
    float* C) {
  int lda = (TransA == CblasNoTrans) ? K : M;
  int ldb = (TransB == CblasNoTrans) ? N : K;
  cblas_sgemm(CblasRowMajor, TransA, TransB, M, N, K, alpha, A, lda, B,
      ldb, beta, C, N);
}

int main()
{
	int M = 3;
	int N = 3;
	int K = 2;
	float alpha = 1;
	float beta = 1;
	int A_count = M*K;
	int B_count = K*N;
	float A[A_count] = {0,1,2,3,4,5};
	float B[B_count]  = {0,1,2,3,4,5};
	float C[M*N] = {1,1,1,1,1,1,1,1,1};

	caffe_cpu_gemm(CblasNoTrans, CblasNoTrans, M, N, K,
		alpha, A, B, beta, C);

	for(int i=0; i<A_count; ++i){
		cout << A[i] << " ";
	}
	cout << endl;

	for(int i=0; i<B_count; ++i){
		cout << B[i] << " ";
	}
	cout << endl;

	for(int i=0; i<M; ++i){
		for(int j=0; j<N; ++j)
          cout << (C[i*N + j]) << " ";
      	cout << endl;
  	}

    return 0;
}


// rtp@ubuntu:~/CodeSnippt/CXX/blas/caffe_cpu_gemm$ make
// g++ -std=c++11 caffe_cpu_gemm.cpp -lcblas
// rtp@ubuntu:~/CodeSnippt/CXX/blas/caffe_cpu_gemm$ ./a.out 
// 0 1 2 3 4 5 
// 0 1 2 3 4 5 
// 4 5 6 
// 10 15 20 
// 16 25 34 

