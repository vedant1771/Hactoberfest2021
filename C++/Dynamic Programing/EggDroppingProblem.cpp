#include <bits/stdc++.h> 
using namespace std;

int egg,floor;
int **table= NULL;
int min_probes=0;

void input()
{
	cin>>egg;
	cin>>floor;
	table=new int*[floor+1];		//Initializing memory for DP Table
	for(int i = 0; i <= egg; ++i)
      table[i] = new int[floor+1];

}
int find_min_probes(int n,int k)
{   

	int dp[n+1][k+1];
        int ans;
        for(int i = 0;i<=n;i++){
            for(int j = 0;j<=k;j++){
                if(i == 0 or j == 0) dp[i][j] = 0;
                else if(i == 1 or j == 1) dp[i][j] = j;
                else {
                    dp[i][j] = INT_MAX;
                    for(int x = 1;x<=j;x++){
                        ans = 1+max(dp[i][j-x],dp[i-1][x-1]);
                        dp[i][j] = min(dp[i][j],ans);}
                }
            }
        }
        return dp[n][k];
}

void display()
{
	cout<<endl<<"Number of eggs are: "<<egg;
	cout<<endl<<"Number of floors are: "<<floor<<endl;
	cout<<"Minimum number of trials in worst case with "<<egg<<" eggs and "<<floor<<" floors are: "<<min_probes<<endl<<endl;
}

int main() 
{ 
    input(); 
    min_probes = find_min_probes(egg,floor);
	  display();
	  return 0;
} 
