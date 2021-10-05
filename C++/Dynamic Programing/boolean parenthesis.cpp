/*
- parent question is matrix chain multiplication, you are given an string eg: T^F|F, and you need to find out total number  of ways to put parenthesis such that resulting string gives true output
- we use matrix chain mutiplication concept, and for memoization we use dp[n+1][n+1][2] array
*/
class Solution {
  int memo[202][202][2];

  public:
    Solution()
    {
      memset(memo, -1, sizeof(memo));
    }
    int countWays(int N, string & S)
    {
    // code here
    return func(S, 0, S.size() - 1, true);
    }

    int func(string & S, int i, int j, bool isTrue)
    {
    if (memo[i][j][isTrue] == -1) {
        int count = 0;
        int res = INT_MIN;

        if (i > j)
        res = false;
        if (i == j) {
        if (isTrue == true)
            res = (S[i] == 'T');
        else
            res = (S[i] == 'F');
        }
        for (int k = i + 1; k < j; k += 2)
        {
        int lT = func(S, i, k - 1, true);
        int lF = func(S, i, k - 1, false);
        int rT = func(S, k + 1, j, true);
        int rF = func(S, k + 1, j, false);
        if (S[k] == '|') {
            if (isTrue == true)
            count += lT * rF + lF * rT + lT * rT;
            else
            count += lF * rF;
        }

        else if (S[k] == '&') {
            if (isTrue == true)
            count += lT * rT;
            else
            count += lF * rT + lT * rF + lF * rF;
        }
        else if (S[k] == '^') {
            if (isTrue == true)
            count += lT * rF + lF * rT;
            else
            count += lT * rT + lF * rF;
        }
        }
        res = (res == INT_MIN) ? count : res;
        memo[i][j][isTrue] = res % 1003;
    }
  return memo[i][j][isTrue] % 1003;
}

