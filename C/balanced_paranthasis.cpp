#include <iostream>
#include <string>
#include <stack>
using namespace std;
void solve(string a){
    stack<char> b;
    int len=a.size();
    for(int i=0;i<len;i++){
        if(a[i]=='('){
            b.push('(');
        }
        if(a[i]==')'){
            if(b.empty()){
                cout<<"0"<<endl;
                return;
            }
            b.pop();
        }
    }
    if(b.empty())
    cout<<"1"<<endl;
    else
    cout<<"0"<<endl;
}

int main(){
    string a;

    getline (cin,a);
    cout<<a[7]<<endl;
    solve(a);

    return 0;
}