/*
This is the Dynamic Programming approach the coin change problem.
I have added the recursive method as well.
.
.
*/

#include<bits/stdc++.h>

using namespace std;

int cnt( vector<int> &v,  int target )
{
  int n=v.size();
	int table[target + 1][n];
	
	for (int i = 0; i < n; i++)
		table[0][i] = 1;

		for (int i = 1; i < target + 1; i++)
	{
		for (int j = 0; j < n; j++)
		{
				int x = (i-S[j] >= 0) ? table[i - S[j]][j] : 0;
					int y = (j >= 1) ? table[i][j - 1] : 0;

			table[i][j] = x + y;
		}
	}
  
	return table[target][n - 1];
}



int main()
{
  int n, target;
	
  cin>>n>>target;
  vector<int> arr(n,0);
  fo(i,n)
    cin>>arr[i];
	cout << cnt(arr,target);
	return 0;
}

// This code is contributed
// by Akanksha Rai(Abby_akku)
