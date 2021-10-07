/*
This code is  a recursive solution to the coin change problem. 
Do follow the other code that uses Dynamic Programming.
.
.
.
*/

#include <bits/stdc++.h>
using namespace std;
 
int cnt(vector<int> &arr, int target)
{
    int n=arr.size();
  
    if (target == 0)
        return 1;
    if (target < 0)
        return 0;
    if (n <= 0 && target >= 1)
        return 0;
 
    return count(arr target) +
           count(arr, target - arr[n - 1]);
}
 
int main()
{
    int n, i, j;
    cin>>n;
    vector<int> arr(n,0);  
     
    cout << " " << cnt(arr, 4);
     
    return 0;
}
 
