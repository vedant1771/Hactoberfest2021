#include<iostream>
#include<algorithm>
using namespace std;

bool cmp(pair<int,int> p1,pair<int,int> p2)
{
	return p1.second<p2.second;
}
int main() 
{
	int t;
	cin>>t;
	int n,a,b;

	pair<int,int> A[1000000];
	while(t--)
	{
		cin>>n;
		for(int i=0;i<n;i++)
	{
		cin>>a>>b;
		A[i]= make_pair(a,b);
	}
	sort(A,A+n,cmp);
	int ans=1;
	int j =0;
	for(int i=1;i<n;i++)
	{
		if(A[i].first>=A[j].second)
		{
			j=i;
			ans++;
		}		
	}	
	cout<<ans<<endl;
	}	
	return 0;
}
