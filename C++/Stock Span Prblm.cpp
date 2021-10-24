//please accept this as hacktoberfest-accepted label

//problem link

//https://leetcode.com/problems/online-stock-span/
//thanks

//HAPPY CODING

// StockSpan Problem solved using Stack

#include<bits/stdc++.h>
using namespace std;
#define ll long long

vector<int> stockSpan(vector<int>v){
    stack<pair<int,int>> st;
    vector<int> ans;
    for (int i = 0; i < v.size(); i++)
    {
        if (st.empty())
        {
            ans.push_back(-1);
        }else if (st.size()>0 && st.top().first>v[i])
        {
            ans.push_back(st.top().second);
        }else if (st.size()>0 && st.top().first<=v[i])
        {
            while (!st.empty() && st.top().first<=v[i])
            {
                st.pop();
            }
            if (st.empty())
            {
                ans.push_back(-1);
            }else{
                ans.push_back(st.top().second);
            }
        }
        st.push({v[i],i});
    }
    return ans;
}

int main(){
    int n;
    cin>>n;
    vector<int>v(n);
    for(auto &it: v) cin>>it;
    vector<int>ans=stockSpan(v);
    vector<int>result;
    for (int i = 0; i < v.size(); i++)
    {
        result.push_back(i-ans[i]);
    }
    for(auto it: result) cout<<it<<" ";

    return 0;
}
