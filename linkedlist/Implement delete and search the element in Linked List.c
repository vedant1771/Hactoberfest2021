#include <stdio.h>
#include <stdlib.h>
struct node{
 int a;
 struct node *next;
};
struct node *head = NULL;
struct node *newnode,*temp;
void input(){
 newnode = (struct node*)malloc(sizeof(struct node));
 printf("Enter element : ");
 scanf("%d",&newnode->a);
 newnode->next=NULL;
 if(head==NULL){
 head=temp=newnode;
 }
 else{
 temp->next=newnode;
 temp=newnode;
 }
}
void display(){
 temp=head;
 while(temp!=0){
 printf("%d\t",temp->a);
 temp=temp->next;
 }
}
void delete_beg(){
 temp=head;
 if(temp==NULL){
 printf("Empty list");
 }
 else if(temp->next==0){
 head=0;
 }
 else{
 head=head->next;
 }
 free(temp);
}
void delete_last(){
 struct node *second_last;
 temp=head;
 while(temp->next!=0){
 second_last=temp;
 temp=temp->next;
 }
 if(temp==head){
 head=0;
 }
 else{second_last->next=0;}
 free(temp);
}
void delete_pos(int pos){
 struct node *next_node;
 temp=head;
 for(int i=0;i<pos;i++){
 temp=temp->next;
 }
 next_node=temp->next;
 temp->next=next_node->next;
 free(next_node);
}
void search(int find){
 temp=head;
 while(temp!=0){
 if(temp->a==find){
 printf("Element found : %d",temp->a);
 break;
 }
 temp=temp->next;
 }printf("Element found : %d",temp->a);
}
int main(){
 system("cls");
 head = 0;
 int choice, position, element;
 do{
 printf("\n\n** MENU **");
 printf("\n1. Input Element");
 printf("\n2. Diplay List");
 printf("\n3. Delete from Begining");
 printf("\n4. Delete from Last");
 printf("\n5. Delete from position");
 printf("\n6. Search from position");
 printf("\n7. EXIT\nEnter Choice : ");
 scanf("%d",&choice);
 switch(choice){
 case 1: input();
 break;
 case 2: display();
 break;
 case 3: delete_beg();
 break;
 case 4: delete_last();
 break;
 case 5: printf("Enter position of node to delete : ");scanf("%d",&position);
 delete_pos(position);
 break;
 case 6: printf("Enter element to find : ");scanf("%d",&element);
 search(element);
 break;
 case 7: exit(1);
 break;
 }
 printf("\nContinue?\t1.YES\t0. NO\t:");
 scanf("%d",&choice);
 }while(choice);
 return 0;
}
