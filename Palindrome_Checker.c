#include<stdio.h>
void main()
{
    char p[25];
    int i=0,j,flag =0;
    printf("Enter String\n");
    gets(p);
    printf("your string is :%s\n",p);
    j=strlen(p);
    while(i<j){
        if(p[i]!=p[j-i-1])
        {
            flag=1;
            break;
        }
        ++i;
    }
    if(flag==1){
        printf("String is not Palindrome");
    }
    else {
        printf("String is Palindrome");
    }
}
