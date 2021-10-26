// A CPP program to demonstrate application of quick select algorithm (randomized)
// to find kth smallest element in a given array

#include<bits/stdc++.h>
using namespace std;

// main function to find kth smallest elemnt recursively
int quick_sort(int a[], int l, int r, int k)
{
	int index = l + rand() % (r - l + 1);
	int x = a[index];
	if (index == k - 1)
	{
		return x;
	}
	int m = l;
	for (int i = l; i < r; ++i)
	{
		if (a[i] < x)
		{
			swap(a[i], a[m]);
			m += 1;
		}
	}
	if (k - 1 < m)
	{
		quick_sort(a, l, m, k);
	}
	else {
		quick_sort(a, m , r, k);
	}
}

int main()
{
	int arr[1000]; int n, k;
	// taking values of n and k as user input
	cout << "Enter size of array to be entered (n) and kth position that is to be searched,separated by space: \n";
	cin >> n >> k;
    cout<<"\nNow, Enter the array: ";
	for (int i = 0; i < n; ++i)
	{
		cin >> arr[i];
	}
	// printing the kth smallest element value
	cout << "The kth smallest element is: " << quick_sort(arr, 0, n, k);


	return 0;
}
