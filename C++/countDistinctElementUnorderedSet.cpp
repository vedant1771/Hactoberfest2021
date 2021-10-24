#include<iostream>
#include<unordered_set>
using namespace std;
int distinctElement(int a[],int size){
unordered_set<int> s;
for(int i=0;i<size;i++){
    s.insert(a[i]);
}
return s.size();
}
int main(){
    int a[]={1,2,2,2,1,4,3};
    int size = sizeof(a)/sizeof(a[0]);
    cout<<distinctElement(a,size);
    return 0;
}
