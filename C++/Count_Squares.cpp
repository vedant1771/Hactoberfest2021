#include<iostream>
#include<cmath>

using namespace std;
 int countSquares(int n) {
   if(n<=0){
       return -1;
   }
   else{
       int x= sqrt(n);
       cout<<"x = "<<x<<endl;
       if(x*x==n)
       return x-1;
       else 
       return x;
   }

    }

int main(){
int n=5;
cout<<countSquares(n);
    return 0;
}
