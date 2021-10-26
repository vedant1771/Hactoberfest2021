#include<stdio.h>
#define MAX 5
struct Stack
{
    int stack[MAX];
    int sp;
}s;

void init()
{
    s.sp=-1;
}

int isFull()
{
    if (s.sp==MAX-1)
        return 1;
    else
        return 0;
}

int isEmpty()
{
    if (s.sp==-1)
        return 1;
    else
        return 0;
}

void push(int value)
{
    if (isFull())
        printf("Overflow");
    else
        s.stack[++s.sp]=value;
}

int pop()
{
    if (isEmpty())
        printf("Underflow");
    else
        return (s.stack[s.sp--]);
}

void display()
{
    int tos=s.sp;
    printf("\nStack values \n");
    for (int i=tos;i>-1;i--)
        printf("  %d",s.stack[i]);
}

int main()
{
    int choice;
    init();
    while(1)
    {
        printf("\n1. PUSH");
        printf("\n2. POP");
        printf("\n3. IS FULL?");
        printf("\n4. IS EMPTY?");
        printf("\n5. DISPLAY");
        printf("\n6. EXIT");
        printf("\n\n");
    
        printf("ENTER YOUR CHOICE");
        scanf("%d",&choice);
        int value;

        switch (choice)
        {
        case 1 :printf("\nEnter value to be pushed ");
                scanf("%d",&value);
                push(value);
                break;

        case 2 :value=pop();
                printf("\nValue popped : %d",value);
                break;
        
        case 3 :if (isFull())
                    printf("\nyes");
                else
                    printf("\nno");
                break;
        
        case 4 :if (isEmpty())
                    printf("\nyes");
                else
                    printf("\nno");
                break;
        
        case 5 :display();
                break;
        
        case 6 : exit(0);

        default:printf("\nWrong choice");
        }
    } 
}
