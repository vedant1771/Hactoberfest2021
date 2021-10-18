#include<iostream>
using namespace std;

int count_set_bit(int num){
	int count=0;

	while(num){
		count += (num&1);
		num>>=1;
	}

	return count;
}

int main(){
	int n=7;

	cout<<count_set_bit(n);
} 

