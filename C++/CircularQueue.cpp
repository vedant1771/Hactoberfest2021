#include<iostream>
using namespace std;

class QNode{
    public:
        int data;
        QNode* next;

        QNode(int val){
            data=val;
            next=NULL;
        }
};

class Queue{
    public:
        QNode* front;
        QNode* rear;

        Queue(){
            front=NULL;
            rear=NULL;
        }

    bool isEmpty(){
        return(front==NULL);
    }

    void enQueue(int val){
        QNode* newNode = new QNode(val);
        if(isEmpty()){
            rear=newNode;
            front=newNode;
            rear->next=front;
            return;
        }

        rear->next=newNode;
        rear=rear->next;
        rear->next=front;
    }

    void deQueue(){
        if(isEmpty()){
            cout<<"Queue empty"<<endl;
            return;
        }
        QNode* toFree = front;
        front=front->next;
        rear->next=front;
        free(toFree);
    }

    void printElements(){
        if(isEmpty()){
            cout<<"Queue empty"<<endl;
            return;
        }
        QNode* temp=front;
        cout<<"Queue elements are: ";
        do{
            cout<<temp->data<<" ";
            temp=temp->next;
        } while(temp!=front);  
        cout<<endl;  
    }
};

int main(){
    Queue q;
    q.enQueue(1);
    q.enQueue(2);
    q.enQueue(3);
    q.enQueue(4);
    q.printElements();

    q.deQueue();
    q.deQueue();
    q.printElements();
    return 0;
}
