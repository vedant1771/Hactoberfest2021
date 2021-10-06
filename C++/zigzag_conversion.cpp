#include <bits/stdc++.h>
using namespace std;

    string convert(string s, int nRows) {
        if(nRows == 1)
            return s;
        int row =0;
        bool flag = false;
        string sarray[nRows];
        for(int i=0;i<nRows;i++){
            sarray[i] = "";
        }
        for(int i=0;i<s.length();i++){
            sarray[row] += s[i];
            
            if(row == 0 || row == nRows - 1)
                flag =!(flag);
            if(flag == true)
                row+=1;
            else
                row-=1;
        }
        string res = "";
        for(int i=0;i<nRows;i++){
            res += sarray[i];
        }
        return res;
}

int main(){
    string str;
    cin>>str;
    int nrows;
    cin>>nrows;
    cout<<"ZIGZAG CONVERSIONS RESULT:"<<(convert(str,nrows));
    return 0;
 }
