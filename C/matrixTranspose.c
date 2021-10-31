// transpose matrix

#include <stdio.h>
int main()
{
    int mtr[3][3];
    int trns[3][3];
    printf("Enter the 3*3 matrix : \n");
    for(int i=0;i<3;i++)
    {
        for(int j=0;j<3;j++)
        {
            printf("enter the value of [%d][%d] : ", i, j);
            scanf("%d",&mtr[i][j]);
        }
    }
    printf("You entered the matrix\n");

    for(int i=0;i<3;i++)
    {
        for(int j=0;j<3;j++)
        {
            printf("%d",mtr[i][j]);
        }
        printf("\n");
    }

        printf("Transpose of the matrix\n");

    for(int i=0;i<3;i++)
    {
        for(int j=0;j<3;j++)
        {
            
            printf("%d",mtr[j][i]);
            trns[i][j] = mtr[j][i];
        }
        printf("\n");
    }
}
