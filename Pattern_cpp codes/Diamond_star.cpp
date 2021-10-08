//Diamond star pattern
#include<iostream>
using namespace std;

int main()
{

    int n, i,j;
    cout<<"Enter the number for diamond star pattern"<<endl;
    cin>>n;

       for( i=n; i>=1; i--)
    {
        for(j=1; j<=i; j++)
        {
            cout<<"*";
        }
        for(j=1; j<=(2*n-2*i); j++)
        {
            cout<<" ";
        }
        for(j=1; j<=i; j++)
        {
            cout<<"*";
        }
        cout<<endl;
    }

    for( i=1; i<=n; i++)
    {
        for(j=1; j<=i; j++)
        {
            cout<<"*";
        }
        for(j=1; j<=(2*n-2*i); j++)
        {
            cout<<" ";
        }
        for(j=1; j<=i; j++)
        {
            cout<<"*";
        }
        cout<<endl;
    }


    return 0;
}