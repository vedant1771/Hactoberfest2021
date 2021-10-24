#include<iostream>

using namespace std;

void find(int a[],int n,int x){
int first=-1,last=-1;
for(int i=0;i<n;i++){
    if(a[i]==x){
       if(first==-1){
           first=i; 
            }
      last=i;
         }
    }
 cout<<"last:"<<last;
       cout<<"first:"<<first;

}


int main(){
int a[]={7,1,2,3,7,4,5,6,7,7,0,7};
int x=7;
int n=sizeof(a)/sizeof(a[0]);
find(a,n,x);

    return 0;
}
