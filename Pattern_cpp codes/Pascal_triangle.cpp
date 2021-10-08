//pascal triangle code
// print pascal triangle pattern by taking input value of user
#include<iostream>
using namespace std;

int fact(int i)
{
    int factorial=1;
    for(int j=2; j<=i; j++)
    {
        factorial = factorial*j;
    }
    return factorial;
}

int main()
{
    int n;
    cout<<"Enter the n for print pascal triangle"<<endl;
    cin>>n;



    for(int i=0; i<n; i++)
    {
        for(int k=1; k<(n-i);k++){
            cout<<" ";
        }
        for(int j=0; j<=i; j++)
        {
            int ans = fact(i)/(fact(j)*fact(i-j));
            cout<<ans<<" ";
        }
        cout<<endl;
    }
    return 0;
}

