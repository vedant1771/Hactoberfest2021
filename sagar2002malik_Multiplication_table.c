# include<stdio.h>

int main()
{
    int num,l;
    printf("Enter the number: ");
    scanf("%d",&num);
    printf("Enter the length: ");
    scanf("%d",&l);
    for(int i=1;i<=l;i++)
    {
        printf("\n%d",num);
        printf(" x %d",i);
        printf(" = %d",(num*i));
    }
    return 0;
}
