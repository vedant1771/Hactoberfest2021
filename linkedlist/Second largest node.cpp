// Second largest node in linked list
#include <bits/stdc++.h>
using namespace std;

struct Node{
    int data;
    struct Node *next;
};

void create(struct Node *p,int arr[],int n){
    p->data = arr[0];
    p->next = NULL;
    Node *t,*last;
    last = p;
    for (int i = 1; i < n; i++) {
        t = new Node;
        t->data = arr[i];
        last->next = t;
        last = t;
    }
}

void display(struct Node *p){
    while(p != NULL){
        cout << p->data << " ";
        p = p->next;
    }
}

int secondlargest(struct Node *p){
    int first_max = INT_MIN;
    int second_max = INT_MIN;
    
    while(p != NULL){
        if(p->data > first_max){
            second_max = first_max;
            first_max = p->data;
        } else if(p->data > second_max && p->data != first_max){
            second_max = p->data;
        }
        p = p->next;
    }
    if(second_max == INT_MIN){
        return -1;
    }
    return second_max;
}


int main() {
    int n;
    cin >> n;
    int arr[n];
    for (int i = 0; i < n; i++) {
        cin >> arr[i];
    }
	Node *first = new Node;
	create(first,arr,n);
	cout << secondlargest(first);
	return 0;
}
