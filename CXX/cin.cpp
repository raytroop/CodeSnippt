#include<iostream>  
using namespace std;  
int main()  
{  
    int currVal = 0 , val = 0;  
    if(cin >> currVal)  
    {  
        int cnt=1;//统计次数  
        while(cin >> val)  
        {  
            if(currVal == val)  
            {  
                cnt++;  
            }  
            else{  
                cout << currVal <<" occurs "<<cnt<<" times "<<endl;  
                currVal = val;  
                cnt=1;//重新计算另一个   
            }  
        } //while循环结束   
        cout << currVal <<" occurs "<<cnt<<" times "<<endl;//打印最后一个数   
    }//if循环结束   
    return 0;  
} 
// 首先cin>>a返回的是左操作数，也就是返回cin。
// cin的条件状态中: cin.eof()    判断流是否到达文件的结束符

// 　　　　　　　　 cin.fail()    判断IO操作是否失败

// 在while（cin>>a）中看流是否还能用，主要是判断 cin.fail()  的取值。事实上，无论是否用于while循环，流必须处于无错误状态才能用于输入和输出 ，也就是cin.fail() 必须为0值，程序以下的cin操作才能正常执行。

// 导致cin.fail() 为1的操作有：输入坏值 或 遇到文件结束符（ctrl+z)
// while（cin）中有个缓冲机制规定，只有收到回车键，才会将所有输入的
// 数据一次提交到输入处理函数cin里，而这个输入过程，在按下回车之前，是不受cin控制的。
// 在windows系统中，输入文件结束符的方法是先按Ctrl+Z，然后再按Enter；
// 在UNIX系统中，包括Mac OS X系统中，文件结束输入为Ctrl+D;