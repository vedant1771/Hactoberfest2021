#include<bits/stdc++.h>
#define pb push_back
using namespace std;
 
int maxSubArraySum(int a[], int size)
{
	int max_so_far = 0, curr_max = Integer.MIN_VALUE;
    for(int i: arr){
    	max_so_far += i;
        if(max_so_far<0) max_so_far = 0;
        if(max_so_far>curr_max) curr_max = max_so_far;
    }
    return curr_max;
}
 int main()
{
   int a[] =  {-2, -3, 4, -1, -2, 1, 5, -3};
   int n = sizeof(a)/sizeof(a[0]);
   int max_sum = maxSubArraySum(a, n);
   cout << "Maximum contiguous sum is " << max_sum;
   return 0;
}
