#include<bits/stdc++.h>
using namespace std;
int main()
{
	int n;
	cin>>n;
	int dp[n+1],i,j;
	dp[0]=1;
	dp[1]=1;
	for(i=2;i<=n;i++)
	dp[i]=0;
	for(i=2;i<=n;i++)
	{
		for(j=0;j<i;j++)
		{
			dp[i]+=(dp[j]*dp[i-j-1]);
		}
	}
	cout<<dp[n]<<" ";
}
