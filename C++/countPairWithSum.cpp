//Count pairs with given sum

// Given an array of N integers, and an integer K, find the number of pairs of elements in the array whose sum is equal to K.

// Example 1:
//
// Input:
// N = 4, K = 6
// arr[] = {1, 5, 7, 1}
// Output: 2
// Explanation:
// arr[0] + arr[1] = 1 + 5 = 6
// and arr[1] + arr[3] = 5 + 1 = 6.

class Solution{
public:
    int getPairsCount(int arr[], int n, int k) {
        unordered_map<int, int> m;

    for (int i = 0; i < n; i++)
        m[arr[i]]++;

    int twice_count = 0;
    for (int i = 0; i < n; i++) {
        twice_count += m[sum - arr[i]];
        if (sum - arr[i] == arr[i])
            twice_count--;
    }
    return twice_count / 2;
    }
}
