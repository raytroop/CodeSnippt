#include <iostream>
#include <memory>
using namespace std;

int main()  
{  
    //Hey, pointers have a finite size, no matter the indirection level!
    cout << "sizeof(int*): " << sizeof(int*) << endl;
    cout << "sizeof(int**): " << sizeof(int**) << endl;
    cout << "sizeof(int***): " << sizeof(int***) << endl;
    int row=3,column=4;  
    //申请空间  
    int ** a = new int *[row];  
    for(int i = 0;i < row;i++)  
        a[i] = new int[column];  
  
    //使用空间  
    for(int i = 0;i < row;i++)  
        for(int j = 0;j< column;j++)  
            a[i][j] = i + j;  
    //输出测试
    for(int i = 0;i < row;i++)  
    {   
        for(int j = 0;j< column;j++)  
        {    
            cout<<a[i][j]<<"     ";  
        }
        cout<<endl;   
    } 
          
    //释放空间  
    for(int i = 0;i < row;i++)  
    {  
        delete [] a[i];  
        a[i] = NULL;  
    }  
    delete [] a;  
    a = NULL;     
  
    return 0;      
}


// raytroop@MyServer:~/CodeSnippt/CXX/array$ g++ -std=c++11 2dDynamic.cpp
// raytroop@MyServer:~/CodeSnippt/CXX/array$ ./a.out 
// sizeof(int*): 8
// sizeof(int**): 8
// sizeof(int***): 8
// 0     1     2     3     
// 1     2     3     4     
// 2     3     4     5