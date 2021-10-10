#include <iostream>
#include <vector>
#include <stack>
#include <algorithm>
using namespace std;
void solve(vector<int>q,int n){
    //NSL
    vector<int>ans1;
    stack<pair<int,int>>st;
    for (int i = 0; i < n; i++)
    {
        if (st.empty())
        {
            ans1.push_back(-1);
        }
        else if (!st.empty() && q[i]>st.top().first)
        {
            ans1.push_back(st.top().second);
        }
        else if (!st.empty() && q[i]<=st.top().first)
        {
            while (!st.empty() && q[i]<=st.top().first)
            {
                st.pop();
            }
            if (st.empty())
            {
                ans1.push_back(0);
            }
            else if (q[i]>st.top().first)
            {
                ans1.push_back(st.top().second);
            }
            
        }
        st.push({q[i],i});
        
    }
    
    //NSR
    vector<int>ans2;
    stack<pair<int,int>>st2;
    for (int i = n-1; i>=0; i--)
    {
        if (st2.empty())
        {
            ans2.push_back(7);
        }
        else if (!st2.empty() && q[i]>st2.top().first)
        {
            ans2.push_back(st2.top().second);
        }
        else if (!st2.empty() && q[i]<=st2.top().first)
        {
            while (!st2.empty() && q[i]<=st2.top().first)
            {
                st2.pop();
            }
            if (st2.empty())
            {
                ans2.push_back(7);
            }
            else if (q[i]>st2.top().first)
            {
                ans2.push_back(st2.top().second);
            }
            
        }
        st2.push({q[i],i});
        
    }
    reverse(ans2.begin(),ans2.end());
    int count=0,max=0;
    cout<<"NSL"<<endl;
     for (int i = 0; i < n; i++)
    {
        cout<<ans1[i]<<" ";
    }
    cout<<endl;
    cout<<"NSR"<<endl;
    for (int i = 0; i < n; i++)
    {
        cout<<ans2[i]<<" ";
    }
    cout<<endl;
    cout<<"Answer"<<endl;
    for (int i = 0; i < n; i++)
    {
        count=ans2[i]-ans1[i]-1;
        count=count*q[i];
        if (count>max)
        {
            max=count;
        }
        
    }
    cout<<max<<" ";
    
}

int main(){
    int n,k;
    cin>>n;
    vector<int>q;

    for (int i = 0; i < n; i++)
    {
        cin>>k;
        q.push_back(k);
    }
    solve(q,n);
    
}