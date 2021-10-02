#include <iostream>
using namespace std;
int main()
{
int num[50], n, i, j, k, temp;
cout<<"Enter the size of an array: ";
   cin >>n;
   cout<<"Enter the elements in an array \n";
   for (i = 0; i <= n - 1; i++)
    {
        cin>>num[i];
    }
	for(j=0;j<n-1;j++)
	{
		for(k=j+1;k<n;k++)
			if(num[j]>num[k])
			{
				temp=num[k];
				num[k]=num[j];
				num[j]=temp;
			}
	}
/*	
cout<<"sorted ";
for (i = 0; i <= n-1 ; i++)
    {
        cout<<num[i]<<" ";
    }
    */
cout<<"\n2nd largest number in the array: "<<num[n-2];
return 0;
}
