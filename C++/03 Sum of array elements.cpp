/* Given an integer array arr of size n, you need to sum the elements of arr.

Example 1:

Input:
n = 3
arr[] = {3 2 1}
Output: 6
Example 2:

Input:
n = 4
arr[] = {1 2 3 4}
Output: 10
Your Task:
You need to complete the function sumElement() that takes arr and n and returns the sum. The printing is done by the driver code.

Expected Time Complexity: O(n).
Expected Auxiliary Space: O(1).

Constraints:
1 <= n <= 103
1 <= arri <= 104
*/
/*
Given an integer array arr of size n, you need to sum the elements of arr.

Example 1:

Input:
n = 3
arr[] = {3 2 1}
Output: 6
Example 2:

Input:
n = 4
arr[] = {1 2 3 4}
Output: 10
Your Task:
You need to complete the function sumElement() that takes arr and n and returns the sum. The printing is done by the driver code.

Expected Time Complexity: O(n).
Expected Auxiliary Space: O(1).

Constraints:
1 <= n <= 103
1 <= arri <= 104
*/
/*
    int sum=0;
    for (i=0;i<n;i++)
    sum+=arr[i];*/


#include <iostream> 
#include <numeric>     
using namespace std;
   
// User defined function that returns sum of
// arr[] using accumulate() library function.
int arraySum(int a[], int n) 
{
    int initial_sum  = 0; 
    return accumulate(a, a+n, initial_sum);
}
   
int main() 
{
    int a[] = {5 , 10 , 15} ;
    int n = sizeof(a)/sizeof(a[0]);
    cout << arraySum(a, n);
    return 0;
}
    return sum;
