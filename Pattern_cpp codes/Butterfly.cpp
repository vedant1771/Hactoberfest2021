// Solid star Butterfly pattern program 
// print Butterfly by taking input value of user
#include<iostream>
using namespace std;

int main()
{
    int row,a,b;
    cout<<"Input the value"<<endl;
    cin>>row;
//rectangle show with  input values
    for(a=1; a<=row; a++)
    {

        for(b=1; b<=a; b++)
        {
             cout<<"* ";
        }

        int space = 2*(row-a);

         for(int b=1; b<=space; b++)
        {
             cout<<"  ";
        }
         for(int b=1; b<=a; b++)
        {
             cout<<"* ";
        }

        cout<<endl;
    }

     for(a=row; a>=1; a--)
    {

        for(b=1; b<=a; b++)
        {
             cout<<"* ";
        }

        int space = 2*(row-a);

         for(int b=1; b<=space; b++)
        {
             cout<<"  ";
        }
         for(int b=1; b<=a; b++)
        {
             cout<<"* ";
        }

        cout<<endl;
    }


    return 0;
}


