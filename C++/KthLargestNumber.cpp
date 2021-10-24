//A CPP program to find the Kth Largest element in a sequence

#include <iostream>
 
using namespace std;
 
// A function to heapify the array.
void MaxHeapify(int a[], int i, int n)
{
	int j, temp;
	temp = a[i];
	j = 2*i;
 
	while (j <= n)
	{
		if (j < n && a[j+1] > a[j])
			j = j+1;
		// Break if parent value is already greater than child value.
		if (temp > a[j])
			break;
		// Switching value with the parent node if temp < a[j].
		else if (temp <= a[j])
		{
			a[j/2] = a[j];
			j = 2*j;
		}
	}
	a[j/2] = temp;
	return;
}
 
// A function to build max heap from the initial array by checking all non-leaf node to satisfy the condition.
void Build_MaxHeap(int a[], int n)
{
	int i;
	for(i = n/2; i >= 1; i--)
		MaxHeapify(a, i, n);
}
 
int main()
{
	int n, i, temp, k;
	cout<<"\nEnter the number of data element to be sorted: ";
	cin>>n;
	n++;
	int arr[n];
	for(i = 1; i < n; i++)
	{
		cout<<"Enter element "<<i<<": ";
		cin>>arr[i];
	}
 
	cout<<"\nEnter the k value: ";
	cin>>k;
 
	Build_MaxHeap(arr, n-1);
 
	// Build max-heap k times, extract the maximum and store it in the end of the array.
	for(i = n-1; i >= n-k; i--)
	{
		temp = arr[i];
		arr[i] = arr[1];
		arr[1] = temp;
		MaxHeapify(arr, 1, i - 1);
	}
 
	// Printing the array state.
	cout<<"\nAfter max-heapify the given array "<<k<<" times the array state is: ";
	for(i = 1; i < n; i++)
		cout<<"->"<<arr[i];
 
	// The Kth largest element.
	cout<<"\n\nThe "<<k<<"th largest element is: "<<arr[n-k];
	return 0;
}