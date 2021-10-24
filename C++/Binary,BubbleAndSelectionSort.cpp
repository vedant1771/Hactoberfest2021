#include <iostream>
using namespace std;
int BinSearch(int arr[], int value, int low, int hi)
{
	
	int mid = (low + hi)/ 2;
	if (arr[mid] == value)
		return mid;
	else if (value >arr[mid])
	{
		low = mid + 1;
		BinSearch(arr, value, low, hi);
	}
	else if (value < arr[mid])
	{
		hi = mid - 1;
		BinSearch(arr, value, low, hi);
	}
	else
	{
		return 0;
	}
}
void Bubbsort(int arr1[], int size)
{
	for (int i = size - 1; i > 0; i--)
	{
		for (int j = 0; j < size; ++j)
		{
			if (arr1[j] > arr1[j + 1])
				swap(arr1[j], arr1[j + 1]);
		}
	}
	for (int i = 0; i < 10; i++)
		cout << arr1[i] << endl;
}
void swap(int a, int b)
{
	int temp = a;
	a =b;
	b = temp;
}
void selectionSort(int arr[], int size)
{
	int i, j, min_idx;
  
	for (i = 0; i < size - 1; ++i)
	{
		min_idx = i;
		for (j = i + 1; j < size; j++)
			if (arr[j] < arr[min_idx])
				min_idx = j;
 
		swap(arr[min_idx], arr[i]);
	}
	for (i = 0; i < size - 1; ++i)
		cout << arr[i] << endl;
}

int main()
{
	int value = 0,index=0,low=0,hi=10;
	int arr[10] = {0, 1,2,3,4,6,10,11,12,23 };
	int arr1[15] = { 23,45,12,67,46,89,14,56,76,10,45,23,45,68,90 };
	cout << "************************************\n";
	for (int i = 0; i < 10; ++i)
	{
		cout << arr[i] << endl;
	}
	cout << "************************************\n";
	cout << "Please Input the value to search\n";
	cin >> value;
	index = BinSearch(arr, value, low, hi);
	if (index != 0)
		cout << "Given value is at " << index + 1 << endl;
	else
		cout << "Not present in the array\n";
	cout << "Before sorting array is\n";
	for (int i = 0; i < 10; ++i)
	{
		cout << arr1[i] << endl;
	}
	cout << "After sorting by using Bubble Sort array is \n";
	Bubbsort(arr1, hi);
	cout << "After sorting by using Selection sort  array is \n";
	selectionSort(arr1, hi);
	return 0;
}
