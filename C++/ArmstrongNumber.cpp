/*
Armstrong number is a number that is equal to the sum of cubes of its digits
*/
#include<iostream>
#include<math.h>
using namespace std;
int main()
{
    int n,sum=0;
    cout<<"Enter a number\n";
    cin>>n;
    int original_no=n;
    while(n>0)
    {
        int last_digit=n%10;
        sum+=pow(last_digit,3);
        n=n/10;
        
    }
    if(original_no==sum)
    {
        cout<<"Armstrong number";
    }
    else{
        cout<<"Not Armstrong Number";
    }
}

