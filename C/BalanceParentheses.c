#include <stdio.h>
#include <stdlib.h>
#include <string.h>
int size = 100;
int top = -1;
char stack[100];
int IsEmpty()
{
    if(top==-1)
        return 1;
return 0;
}
int check(char ch)
{
    if(ch=='(' || ch==')')
    {
        return 1;
    }
    else if(ch=='['|| ch==']')
    {
        return 2;
    }
    else if(ch=='('|| ch==')')
    {
        return 3;
    }
    else
    {
        return 0;
    }
}
void push(char ch)
{
    if(top>size-1)
    {
        printf("STACK OVERFLOW\n");
        return ;
    }
    else
    {
        top++;
        stack[top] = ch;
    }
}
void pop()
{
    if(top==-1)
    {
        printf("STACK UNDERFLOW\n");
    }
    else
    {
        top--;
    }
}
void solve(char s[100])
{
    int n = strlen(s), i;
    for(i = 0; i<n; i++)
    {
        if(s[i]=='('||s[i]=='['||s[i]=='{')
            {
                push(s[i]);
            }
        else if(s[i]=='}'||s[i]==']'||s[i]==')')
        {
            if(check(stack[top])==check(s[i]))
            {
                pop();
            }
            else
            {
                break;
            }
        }

    }
    if(IsEmpty()==1)
    {
        printf("YES\n");
    }
    else
    {
        printf("NO\n");
    }
}
int main()
{
    char s[100];
    printf("ENTER THE BRACKETS : ");
    gets(s);
    solve(s);
    return 0;
}
