#include <iostream>
using namespace std;

int main()
{
	int n,i,j,k;
	int temp;

	//read total number of elements to read
	cout<<"Enter total number of elements to read: ";
	cin>>n;

	int arr[n];

	//read n elements
	for(i=0;i<n;i++)
	{
		cout<<"Enter "<<i+1<<"th element ";
		cin>>arr[i];
	}

	cout<<"Enter value of K: ";
	cin>>k;
	//sorting - ASCENDING ORDER
	for(i=0;i<n;i++)
	{		
		for(j=i+1;j<n;j++)
		{
			if(arr[i]>arr[j])
			{
				temp  =arr[i];
				arr[i]=arr[j];
				arr[j]=temp;
			}
		}
	}

	cout<<"Kth largest number:"<<arr[n-k];
	return 0;

}
