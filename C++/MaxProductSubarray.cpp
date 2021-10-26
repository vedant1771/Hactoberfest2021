//CPP Program to find Maximum Product Subarray.

#include<bits/stdc++.h>
using namespace std;


//Function to find maximum product subarray of given array of size n.

long long maxProduct(vector<int> nums, int n) {

	    long long max_overall = nums[0];
        long long  max_ending_here = nums[0], min_ending_here = nums[0];

        for(int i = 1; i < nums.size(); ++i){

            long long tmp = max_ending_here;

            max_ending_here = max({1ll*nums[i], nums[i]*max_ending_here, nums[i]*min_ending_here}); //Maximum product till this point
            min_ending_here = min({1ll*nums[i], nums[i]*tmp, nums[i]*min_ending_here}); //Minimum Product till this point

            max_overall = max(max_overall, max_ending_here); //Update maximum product subarray
        }
        return max_overall;
}

int main() {

    int t;
    cout << "Enter number of test cases: ";
    cin >> t;

    while(t--) {
        int n;
        cout << "Enter length of array : ";
        cin >> n;
        vector<int> arr(n);
        cout << "Enter elements of array : ";
        for(int i = 0; i < n; i++) {
            cin >> arr[i];
        }

        long long ans = maxProduct(arr, n);

        cout << "Maximum Product Subarray is : " << ans << endl;
    }

}


