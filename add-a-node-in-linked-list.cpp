#include <bits/stdc++.h> 
using namespace std; 

struct Node
{
    int data;
    struct Node* next;

    Node(int x){
        data = x;
        next = NULL;
    }
};
class Solution{
  public:
    //Function to insert a node at the beginning of the linked list.
    Node *insertAtBegining(Node *head, int x) {
        Node *temp=new Node(x);
        temp->next=head;
        return temp;
        }

    //Function to insert a node at the end of the linked list.
    Node *insertAtEnd(Node *head, int x)  {
       if(head==NULL){return new Node(x);}
       Node *temp=head;
       while(temp->next!=NULL){
           temp=temp->next;
       }
       Node *y=new Node(x);
       temp->next=y;
       return head;
    }
};


int main() 
{ 
        int n;
        cin>>n;
        struct Node *head = NULL;
        for (int i = 0; i < n; ++i)
        {
            int data, indicator;
            cin>>data;
            cin>>indicator;
            Solution obj;
            if(indicator)
                head = obj.insertAtEnd(head, data); 
            else
                head = obj.insertAtBegining(head, data);
        }
        while (head != NULL) { //Print the list
        cout << head->data <<" "; 
        head = head->next;
        } 
} 
