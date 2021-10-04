#include <bits/stdc++.h> 
using namespace std;

int egg,floor;
int **table= NULL;
int min_probes=0;

void input()
{
	cin>>egg;
	cin>>floor;
	table=new int*[floor+1];		//Initializing memory for DP Table
	for(int i = 0; i <= egg; ++i)
      table[i] = new int[floor+1];

}
int find_min_probes(int e,int f)
{   

	if(e==1)
		return f;

    if(f==0||f==1)
		return  f;

    int probes=INT_MAX;
    for(int k=1;k<=f;k++)
    {
		int temp=1+max(find_min_probes(e-1,k-1),find_min_probes(e,f-k));
        probes=min(probes,temp);
    }
   	return probes;
}

void display()
{
	cout<<endl<<"Number of eggs are: "<<egg;
	cout<<endl<<"Number of floors are: "<<floor<<endl;
	cout<<"Minimum number of trials in worst case with "<<egg<<" eggs and "<<floor<<" floors are: "<<min_probes<<endl<<endl;
}

int main() 
{ 
    input(); 
    min_probes = find_min_probes(egg,floor);
	  display();
	  return 0;
} 
