
#include <stdio.h>
#include<time.h>
#include<stdlib.h>
void swap(int *xp, int *yp)
{
	int temp = *xp;
	*xp = *yp;
	*yp = temp;
}


void bubbleSort(int arr[], int n)
{
int i, j;
for (i = 0; i < n-1; i++)	

	// Last i elements are already in place
	for (j = 0; j < n-i-1; j++)
		if (arr[j] > arr[j+1])
			swap(&arr[j], &arr[j+1]);
}


int main()
{
    clock_t start,end;
    int i, n, lower=-65536, upper=65536;
    
    printf("Enter total no.of elements: ");
    scanf("%d",&n);
    int a[n];
    for(i=0;i<n;i++)
    {
        a[i]=(rand()%(upper-lower+1))+lower;
    }

    start=clock();
	bubbleSort(a, n);
    end=clock();

    double diff=end-start;
    double time=(double)diff/(CLOCKS_PER_SEC);
    printf("\n The time to execute this program is %lf",time);
    return 0;
}
