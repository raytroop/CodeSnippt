//from problem solving with C++

#include <iostream>
using namespace std;

typedef int* IntArrayPtr;


int main()
{
    int d1, d2;
    cout << "Enter the row and column dimensions of the array:\n";
    cin >> d1 >> d2;
    IntArrayPtr m[d1];
    for(int i=0; i<d1;i++)
        m[i] = new int[d2];
    cout << "Enter " << d1 << " rows of " << d2 << " integers each:\n";
    for(int i=0; i<d1;i++)
        for(int j=0; j<d2;j++)
            cin >>m[i][j];
    cout << "Echoing the two-dimensional array:\n";
    for(int i=0; i<d1;i++)
    {
        for (int j = 0; j < d2; j++)
            cout << m[i][j] << " ";
        cout << endl;
    }

    for (int i = 0; i < d1; i++)

            delete[] m[i];

    delete[] m;

    return 0;
}

