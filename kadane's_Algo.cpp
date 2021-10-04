#include<bits/stdc++.h>
#define pb push_back
using namespace std;
 
int maxSubArraySum(int a[], int size)
{
   int maxi = a[0];
   int curx = a[0];
 
   for (int i = 1; i < size; i++)
   {
        curx = max(a[i], curx+a[i]);
        maxi = max(maxi, curx);
   }
   return maxi;
}
 int main()
{
   int a[] =  {-2, -3, 4, -1, -2, 1, 5, -3};
   int n = sizeof(a)/sizeof(a[0]);
   int max_sum = maxSubArraySum(a, n);
   cout << "Maximum contiguous sum is " << max_sum;
   return 0;
}
