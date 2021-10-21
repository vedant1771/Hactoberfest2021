#include<stdio.h>
#include <stdlib.h>
struct stack
{
	int size;
	int top;
	int *s;
};

void Display(struct stack st)
{
 int i;
 for(i=st.top;i>=0;i--)
 printf("%d ",st.s[i]);
 printf("\n");
 
}

void push(struct stack *st, int x)
{
	if(st->top==st->size-1)
	  printf("Stack is full ");
	else
	{
	 st->top++;
	 st->s[st->top]=x;
}
}

int pop(struct stack *st)
{   int x=-1;
	if(st->top==-1)
	  printf("Stack is empty ");
	else
	{
     x=st->s[st->top];
	 st->top--;
	 
}
    return x;
}

int Peep(struct stack *st)
{
	int x;
		if(st->top==-1)
	  printf("Stack is empty ");
	else
	{
			x=st->s[st->top];
			//sp->top--;
			return x;
	}	
}

int main(){
	
	struct stack st;
	int ch,ele;
	printf("Enter size you want for stack :");
	scanf("%d",&st.size);
    st.top=-1;
	st.s=(int *)malloc(st.size*sizeof(int));

   do
	{
		printf("\n 1 For PUSH");
		printf("\n 2 For POP");
		printf("\n 3 For PEEP");
		printf("\n 4 For DISPLAY");
		printf("\n 5 For QUIT");
		
		printf("\n Enter your choice:");
		scanf("%d", &ch);
		
		switch(ch)
		{
			case 1: printf("\n Enter the elements to be pushed");
					scanf("%d", &ele);
					push(&st,ele);
					break;
			case 2: ele = pop(&st);
					if(ele == -1)
						printf("\n The stack is empty");
					else
						printf("\n The poped element is =%d", ele);
					break;
			case 3: ele = Peep(&st);
					if(ele == -1)
						printf("\n The stack is empty");
					else
						printf("\n The peeped element is =%d", ele);
					break;
			case 4: Display(st);
					break;
	
			default: printf("\n Wrong choice! Try again");
					 break;									
		} 
	} while(ch!=st.size); 
	return 0;
	
}
