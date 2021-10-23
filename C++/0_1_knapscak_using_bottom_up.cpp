#include <bits/stdc++.h>
using namespace std;

int KnapSack_recursion(int val[], int wt[], int W, int n)
{
    vector<vector<int>> t(n + 1, vector<int>(W + 1));
    for (int i = 0; i < n + 1; i++)
    {
        for (int j = 0; j < W + 1; j++)
        {

            if (i == 0 || j == 0)
                t[i][j] = 0;

            else if (wt[i - 1] <= j)
            {
                t[i][j] = max(val[i - 1] + t[i - 1][j - wt[i - 1]], t[i - 1][j]);
            }
            else
            {
                t[i][j] = t[i - 1][j];
            }
        }
    }
    return t[n][W];
}

int main()
{
    int val[] = {6, 10, 12};
    int wt[] = {1, 2, 3};
    int W = 5;
    int n = sizeof(val) / sizeof(val[0]);
    cout << KnapSack_recursion(val, wt, W, n);
    return 0;
}
