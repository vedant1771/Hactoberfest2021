#include <bits/stdc++.h>
using namespace std;
 

class node
{
    public:
    int data;
    node* lchild;
    node* rchild;
};
 

node* newNode(int data)
{
    node* Node = new node();
    Node->data = data;
    Node->lchild = NULL;
    Node->rchild = NULL;
         
    return(Node);
}
 
/* function to find the number of nodes in a tree. */
int sizeoftree(node* node)
{
    if (node == NULL)
        return 0;
    else
        return(sizeoftree(node->lchild) + 1 + sizeoftree(node->rchild));
}
 

int main()
{
    node *root = newNode(1);
    root->lchild = newNode(2);
    root->rchild = newNode(3);
    root->lchild->lchild = newNode(4);
    root->lchild->rchild = newNode(5);
     
    cout << "Size of the tree is " << sizeoftree(root);
    return 0;
}
