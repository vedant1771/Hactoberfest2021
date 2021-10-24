#include<stdio.h>
#include<stdlib.h>
#define MAX 5

struct circularqueue
{
    int q[MAX];
    int f,r;
}Q;

void init(){
    Q.f=Q.r=-1;
}

void enqueue(int ele){
    if(Q.f==-1 && Q.r==-1){
        Q.f=Q.r=0;
        Q.q[Q.r]=ele;
    }
    else if(Q.f==((Q.r+1)%MAX))
        printf("QUEUE IS OVERFLOW\n");
    else{
        Q.r=(Q.r+1)%MAX;
        Q.q[Q.r]=ele;
    }
}

int dequeue(){
    if((Q.f==-1) && (Q.r==-1)){
        printf("QUEUE IS UNDERFLOW\n");
        return 0;
    }
    else if(Q.f==Q.r){
        int ret=Q.q[Q.f];
        Q.f=Q.r=-1;
        return ret;
    }
    else
    {
        int ret=Q.q[Q.f];
        Q.f=(Q.f+1)%MAX;
        return ret;
    }

}
void display(){
    if(Q.f==-1 && Q.r==-1)
        printf("Queue Is Empty.");
    else
    {
        int i;
        for(i=Q.f;i!=Q.r;i=((i+1)%MAX)){
            printf(" %d",Q.q[i]);
        }
        printf(" %d",Q.q[i]);
    }
}

int main(){
    init();
    while (1)
    {
        int choice,n;
        printf("\n1. Enqueue\n");
        printf("2. Dequeue\n");
        printf("3. Display\n");
        printf("4. Exit\n");
        scanf("%d",&choice);
        switch (choice)
        {
        case 1:
            printf("\nEnter value: \n");
            scanf("%d",&n);
            enqueue(n);
            break;
        case 2:
            printf("\nPopped value: %d\n",dequeue());
            break;
        case 3:
            printf("\nDisplay is: ");
            display();
            break;
        case 4:exit(0);
        default:
            printf("\nWrong choice entered\n");
            break;
        }
    }
    return 0;
}
