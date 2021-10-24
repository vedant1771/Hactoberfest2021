//cpp code


 /*problem statement : Given an array and a number k where k is smaller than the size of the array, we need to find the k’th largest 
                     element in the given array. It is given that all array elements are distinct.
   
 e.g-
   Input: n=7
   k = 4 
   arr[] = {2,8,3,10,14,16,4} 
  
   Output: 8 //{2,3,4,8,10,14,16}(after sorting)
*/


// method 1: simple solution using sorting , O(N log N) running time + O(1) memory

#include <bits/stdc++.h>
using namespace std;

// Function to return k'th largest element in a given array
int kthlargest(int arr[], int n, int k)
{
	sort(arr, arr + n); //sorting a given array

	// Return k'th element in the sorted array
	return arr[n-k];
}

// Driver code
int main()
{
  int n;//size of array
  cin>>n;
	int arr[n],k;
  cin>>k;
  for(int i=0;i<n;i++) cin>>arr[i];
	cout << "K'th largest element is " << kthlargest(arr, n, k);
	return 0;
}

//method 2: using min oriented priority queue ,  O(N) best case / O(N^2) worst case running time + O(1) memory


#include <bits/stdc++.h>
using namespace std;

int kthlargest(int nums[],int n, int k) {

    priority_queue<int,vector<int>,greater<int>>pq;
    for(int i=0;i<n;i++) {
        pq.push(nums[i]);

        if(pq.size() > k) {
            pq.pop();
        }
    }
    return pq.top();
}
// Driver program to test above methods
int main()
{
  int n;//size of array
  cin>>n;
	int arr[n],k;
  cin>>k;
  for(int i=0;i<n;i++) cin>>arr[i];
	cout << "K'th largest element is " << kthlargest(arr,n, k);
	return 0;
}

// method 3: using Quickselect method : O(N) running time + O(1) space


#include <bits/stdc++.h>
using namespace std;

int partit(int nums[],int n, int left,int right){
	int pivot = nums[left], l=left+1, r = right;
	while(l<=r){
		if(nums[l]<pivot && nums[r]>pivot) swap(nums[l++],nums[r--]);
		if(nums[l]>=pivot) ++l;
		if(nums[r]<=pivot) --r;
	}
	swap(nums[left], nums[r]);
	return r;
}


int findKthLargest(int nums[],int n, int k) {
	//partition rule: >=pivot   pivot   <=pivot
	int left=0,right=n-1,idx=0;
	while(1){
		idx = partit(nums,n,left,right);
		if(idx==k-1) break;
		else if(idx < k-1) left=idx+1;
		else right= idx-1;
	}
	return nums[idx];
}

// Driver program to test above methods
int main()
{
  int n;//size of array
  cin>>n;
	int arr[n], k;
  cin>>k;
 
  for(int i=0;i<n;i++) cin>>arr[i];
	cout << "K'th largest element is " << findKthLargest(arr,n, k);
	return 0;
}
