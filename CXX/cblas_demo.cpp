// g++ -std=c++11 cblas_demo.cpp -lcblas
#include <iostream>

#ifdef __cplusplus
extern "C"
{
#endif   
#include <cblas.h>
#ifdef __cplusplus
}
#endif
using namespace std;  


int main() {  
    const int M=4;  
    const int N=2;  
    const int K=3;  
    const float alpha=1;  
    const float beta=0;  
    const int lda=K;  
    const int ldb=N;  
    const int ldc=N;  
    const float A[M*K]={1,2,3,4,5,6,7,8,9,8,7,6};  
    const float B[K*N]={5,4,3,2,1,0};  
    float C[M*N];  
      
    cblas_sgemm(CblasRowMajor, CblasNoTrans, CblasNoTrans, M, N, K, alpha, A, lda, B, ldb, beta, C, ldc);  
       
    for(int i=0;i<M;i++)  
    {  
       for(int j=0;j<N;j++)  
       {  
           cout<<C[i*N+j]<<" ";  
       }     
       cout<<endl;  
    }    
}

// rtp@ubuntu:~/test$ g++ -std=c++11 cblas_demo.cpp -lcblas
// rtp@ubuntu:~/test$ ./a.out 
// 14 8 
// 41 26 
// 68 44 
// 67 46

// cblas_sgemm(order,transA,transB,M,N,K,ALPHA,A,LDA,B,LDB,BETA,C,LDC);

// 函数作用：C=alpha*A*B+beta*C 

// alpha =1,beta =0 的情况下，等于两个矩阵相成。

// 第一参数 oreder 候选值 有ClasRowMajow 和ClasColMajow 这两个参数决定一维数组怎样存储在内存中,

// 一般用ClasRowMajow

// 参数 transA和transB ：表示矩阵A，B是否进行转置。候选参数 CblasTrans 和CblasNoTrans.

// 参数M：表示 A或C的行数。如果A转置，则表示转置后的行数

// 参数N：表示 B或C的列数。如果B转置，则表示转置后的列数。

// 参数K：表示 A的列数或B的行数（A的列数=B的行数）。如果A转置，则表示转置后的列数。

// 参数LDA：表示A的列数，与转置与否无关。

// 参数LDB：表示B的列数，与转置与否无关。

// 参数LDC：始终=N
