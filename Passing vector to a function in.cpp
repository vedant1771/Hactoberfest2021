// C++ program to demonstrate that when vectors
// are passed to functions without &, a copy is
// created.
#include<bits/stdc++.h>
using namespace std;

// The vect here is a copy of vect in main()
void func(vector<int> vect)
{
vect.push_back(30);
}

int main()
{
	vector<int> vect;
	vect.push_back(10);
	vect.push_back(20);

	func(vect);

	// vect remains unchanged after function
	// call
	for (int i=0; i<vect.size(); i++)
	cout << vect[i] << " ";

	return 0;
}
