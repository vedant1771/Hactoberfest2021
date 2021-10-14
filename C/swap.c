#include <stdio.h>

void swap(int a, int b) //function to swap two numbers
{
    int temp;
    temp = a;
    a = b;
    b = temp;
}
int main()
{
    printf("Enter two numbers: \n");
    int m,n;
    printf("m=");
    scanf("%d",&m);
    printf("n=");
    scanf("%d",&n);

    swap(m, n);    //Function call
    printf("Numbers after Swapping:\n\n");
    printf("m = %d\n", m);
    printf("n = %d", n);
    return 0;
}
