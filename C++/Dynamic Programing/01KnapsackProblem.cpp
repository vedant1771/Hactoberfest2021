#include <iostream>
#include <bits/stdc++.h>
using namespace std;

// A utility function that returns
// maximum of two integers
int max(int a, int b)
{
    return (a > b) ? a : b;
}

// Prints the items which are put in a knapsack of capacity W
void printknapSack(int W, int wt[], int profit[], int n)
{
    int i, w;
    int dp[n + 1][W + 1];

    // Build table K[][] in bottom up manner
    for (i = 0; i <= n; i++) // i is for items
    {
        for (w = 0; w <= W; w++) // w is for wt
        {
            if (i == 0 || w == 0)
                dp[i][w] = 0;
            else if (wt[i - 1] > w) // i-1 is because weight array is starting from 0 as it will indicate the 1st items
            {
                dp[i][w] = dp[i - 1][w]; // Skip case  as i-1 will move to previous items
            }
            else
            {
                dp[i][w] = max(dp[i - 1][w], profit[i - 1] + dp[i - 1][w - wt[i - 1]]);
            }
        }
    }

    // stores the result of Knapsack
    int res = dp[n][W];
    printf("%d\n", res);
}

// Driver code
int main()
{
    int wt[] = {1, 2, 3};
    int profit[] = {2, 3, 5};
    int W = 4;
    int n = sizeof(profit) / sizeof(profit[0]);

    printknapSack(W, wt, profit, n);

    return 0;
}