#include <limits.h>
#include <iostream>
#include <cmath>
using namespace std;

// INT_MAX = 2147483647
// INT_MIN = -2147483648
class Solution {
public:
    int divide(int dividend, int divisor) {
        if (!divisor || (dividend == INT_MIN && divisor == -1))
            return INT_MAX;
        if (dividend == INT_MIN && divisor == 1)
            return INT_MIN;
        int sign = (dividend>0 && divisor >0) || (dividend<0 && divisor<0) ? 1 : -1;
        int result=0;
        int shift=31;
        long long dividend_a = abs(dividend);
        long long divisor_a = abs(divisor);
        cout << dividend_a << endl;
        while(shift >= 0){
        // 100 / 9 ==>  9 *  (2^3) + 9 * (2^1) + 9 * (2^0), then  
        // result = 2^3 + 2^1 + 2^0 = 11  
            if(dividend_a >= (divisor_a<<shift)){
                dividend_a -= divisor_a<<shift;
                result += 1<<shift;
            }
            --shift;
        }
        return min(max(INT_MIN, result*sign), INT_MAX); 

    }
};


int main()
{
    Solution solver;
    cout << solver.divide(-2147483648, 2) << endl;
    // cout << solver.divide(7, -3) << endl;
    // cout << (3<<2) << endl;

}