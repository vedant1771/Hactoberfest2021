#include <stdio.h>
#include <stdlib.h>
#include <stdbool.h>
int nodes=0;
struct node
{
    int data;
    struct node *next;
};
struct node *head1;
struct node *head2;
void push(int n,int a){
    struct node *tmp,*tmp1;
    tmp = (struct node *)malloc(sizeof(struct node));

    tmp->data=n;
    if(a==1){
        if(head1==NULL){
            head1=tmp;
            head1->next=NULL;
        }
        else{
            tmp1 = head1;
            while(tmp1->next != NULL){tmp1 = tmp1->next;}
            tmp1->next=tmp;
            tmp->next=NULL;

        }
    }
    if(a==2){
        if(head2==NULL){
            head2=tmp;
            head2->next=NULL;
        }
        else{
            tmp1 = head2;
            while(tmp1->next != NULL){tmp1 = tmp1->next;}
            tmp1->next=tmp;
            tmp->next=NULL;

        }
    }

}
int pop(int a){
    int b;
    if(a==1){

        if(head1==NULL){ printf("underflow\n");}
        else{
            if(head1->next==NULL){b=head1->data;free(head1);head1=NULL;return b;}
            else{
                struct node *tmp;
                tmp=head1;
                while(tmp->next->next != NULL){tmp = tmp->next;}
                b=tmp->next->data;
                free(tmp->next);
                tmp->next=NULL;
                return  b;



            }

        }
    }
    if(a==2){

        if(head2==NULL){ printf("underflow\n");}
        else{
            if(head2->next==NULL){b=head2->data;free(head2);head2=NULL;return b;}
            else{
                struct node *tmp;
                tmp=head2;
                while(tmp->next->next != NULL){tmp = tmp->next;}
                b=tmp->next->data;
                free(tmp->next);
                tmp->next=NULL;
                return  b;



            }

        }
    }

}
void enqueue(){
    int n;
printf("enter a number to enqueue\n");
scanf("%d",&n);
    push(n,1);
    nodes++;
    printf(" number  enqueued successfully\n");


}
void dequeue(){
    int a=nodes;
    if(a<1){ printf("queue is empty\n");return;}
    for (int i = 0; i < a; i++) {
        push(pop(1),2);
    }
    pop(2);
    a--;
    nodes--;
    for (int i = 0; i < a; i++) {
        push(pop(2),1);
    }

}
void display(){
    if(head1==NULL){printf(" queue is empty\n");}
    else{
        struct node *tmp;
        tmp=head1;
         printf("%d ",tmp->data);
        while(tmp->next != NULL){
            tmp = tmp->next;
            printf("%d ",tmp->data);
            }
    }
}
int main() {
    int a;

    while (true){
        printf("\nselect a option:\n (i) ENQUEUE\n (ii) DEQUEUE\n (iii)DISPLAY\n (iV)EXIT\n");
        scanf("%d",&a);
        switch(a){
            case 1:
                enqueue();
                break;
            case 2:
                dequeue();
                break;
            case 3:
                display();
                break;
            case 4:
                return 0;
            default:
                printf("please choose a valid option\n");
        }
    }
}
