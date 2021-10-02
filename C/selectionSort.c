#include<time.h>
#include<stdio.h>
#include<math.h>
#include<stdlib.h>
void swap(int *xp, int *yp)
{
	int temp = *xp;
	*xp = *yp;
	*yp = temp;
}
void selectionSort(int arr[], int n)
{
	int i, j, min_idx;

	// One by one move boundary of unsorted subarray
	for (i = 0; i < n-1; i++)
	{
		// Find the minimum element in unsorted array
		min_idx = i;
		for (j = i+1; j < n; j++)
		if (arr[j] < arr[min_idx])
			min_idx = j;

		// Swap the found minimum element with the first element
		swap(&arr[min_idx], &arr[i]);
	}
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
    selectionSort(a, n);
    end=clock();

    double diff=end-start;
    double time=(double)diff/(CLOCKS_PER_SEC);
    printf("\n The time to execute this program is %lf",time);
    return 0;
}
