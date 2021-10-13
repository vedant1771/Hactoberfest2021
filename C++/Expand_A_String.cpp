#include <bits/stdc++.h>
using namespace std;
void expandString(string str, string &res) {
char c,count=1,i,j=0,k=0;
  int n=str.length();
  for(i=0;i<n;i++)
  {
     char temp[50];
    k=0;
    count=1;
    c=str[i];
    while(str[i+1]>='0' && str[i+1]<='9')
    {
     temp[k]=str[i+1];
      i++;
      k++;
    }
       temp[k] = '\0';
    if(strlen(temp)>0)
    {
      count=atoi(temp);
    }
    while(count--)
    {
      res=res+c;
    }
  }
  }
int main() {
    string str;
    cin >> str;
    string res;
    expandString(str, res);
    cout << res;
    return 0;
}
