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
    
    printf("Martix after 180 rotation\n");
   for (int i = n - 1; i >= 0; i--) 
   {
        for (int j = n - 1; j >= 0; j--)
            printf("%d ", a[i][j]);
 
        printf("\n");
   }
    return 0; 
}
