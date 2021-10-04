
#include<stdio.h>
int main() 
{ 
    int i, j, n, m, k, temp;
    printf("Enter no of rows: ");
    scanf("%d", &n);
    printf("Enter no of columns: ");
    scanf("%d", &m);
    int a[n][m], b[n][m];
    for (i = 0; i < n; i++)
    {
        for (j = 0; j < m; j++)
        { 
            scanf("%d", &a[i][j]);
        }
    }

     printf("Original matrix is\n");
    for (i = 0; i < n; i++)
    {
        for (j = 0; j < m; j++)
        {
            printf("%d  ", a[i][j]);

        }
        printf("\n");
    }
    
    /transpose/
    for (i = 0; i < n; i++)
    {
        for (j = 0; j < m; j++)
        { 
            b[j][i] = a[i][j];
        }
    }
    
    /reverse columns/
    for(i=0; i<n; i++)
    {
        k = n-1;
        for(j=0; j<k; j++)
        {
            temp = b[j][i];
            b[j][i] = b[k][i];
            b[k][i] = temp;
            k--;
        }
    }
    
    printf("Matrix after 90 anticlockwise rotation\n");

    for(int i = 0; i < n; i++) 
    {
        for(int j = 0; j < m; j++)
           printf("%d ", b[i][j]);
        printf("\n");
    }
    return 0; 
}

