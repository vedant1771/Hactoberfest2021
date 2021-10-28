#include <iostream>
using namespace std;
int main(){
  int n,j=0,k=0;
  cout<<"enter the numbers of element";
  cin>>n;
  int a[n],c[n];
  cout<<"\nenter the element of optimal pattern in sorted order\n";
  for(int i=0;i<n;i++){
    cin>>a[i];
  }
  int i=0;
  c[k]=a[i]+a[i+1];
  i=2;
  while(i<n){
    k++;
    if((c[k-1]+a[i])<=(a[i]+a[i+1])){
      c[k]=c[k-1]+a[i];
    }
    else{
      c[k]=a[i]+a[i+1];
      i=i+2;
      while(i<n){
        k++;
        if((c[k-1]+a[i])<=(c[k-2]+a[i])){
          c[k]=c[k-1]+a[i];
        }
        else{
          c[k]=c[k-2]+a[i];
        }
        i++;
      }
    }
    i++;
  }
  k++;
  c[k]=c[k-1]+c[k-2];
  cout<<"\nthe sum are:-";
  for(i=0;i<n-1;i++){
    cout<<c[i]<<"\t";
  }
  int s=0;
  cout<<"\nthe total sum is=";
  for(i=0;i<n-1;i++){
    s=s+c[i];
  }
  cout<<s<<"\t";
  return 0;
}
