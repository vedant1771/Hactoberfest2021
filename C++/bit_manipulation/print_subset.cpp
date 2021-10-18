#include<iostream>
using namespace std;

void filterBit(char arr[], int n){
	int j = 0;

	while(n){
		if(n&1)
			cout<<arr[j];
		j++;
		n>>=1;
	}
	cout<<endl;
}

// TC: O(n * 2^n), SC: O(1)
void print_subset(char arr[], int n){
	for(int i=0; i<(1<<n); i++)
		filterBit(arr, i);
}

int main(){
	char arr[] = "abcdefg";    // size is 4. bcz: (a,b,c,'/0')
	int n = sizeof(arr)/sizeof(arr[0])-1;
	print_subset(arr, n);
}