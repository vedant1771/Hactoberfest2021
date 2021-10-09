#include <iostream>

using namespace std;


class Node
{
private:
    int data;
    Node *left;
    Node *right;
    //Node *prev;
public:

    Node (int d)
    {
        data=d;
        left=NULL;
        right=NULL;
    }
    void setData(int a)
    {
        data=a;
    }
    void setRight(Node *temp)
    {
        right=temp;
    }
    void setLeft(Node *temp)
    {
        left=temp;
    }
    int getData()
    {
        return data;
    }
    Node *getRight()
    {
        return right;
    }
    Node *getLeft()
    {
        return left;
    }

};
class Bst
{
public:
    Node *root=NULL;


    void insertV(int x)
    {
        Node *temp;
        Node *newNode= new Node(x);
        temp = root;
        //int check=0;
        if(root==NULL)
        {
            root=newNode;
            return;
        }
        else
        {
            while(1)
            {
                /* if(check==bsearch(x)){
                 cout<<"Can't enter same value!"<<endl;
                 break;
                 }//checking same value..
                */
                if(x>=temp->getData())
                {

                    if(temp->getRight()==NULL)
                    {
                        temp->setRight(newNode);
                        break;

                    }
                    temp=temp->getRight();
                }
                if(x<temp->getData())
                {
                    if(temp->getLeft()==NULL)
                    {
                        temp->setLeft(newNode);
                        break;

                    }
                    temp=temp->getLeft();
                }

            }

        }


    }//insert value using loop...
    void insertRecursion(int z)
    {
        Node *temp=root;
        Node *newNode=new Node(z);
        if(temp==NULL)
        {
            root=newNode;
        }
        else
        {
            add(temp,z,newNode);
        }
    }
    void add(Node *temp,int d,Node *temp2)
    {
        if(d<temp->getData())
        {
            if(temp->getLeft()==NULL)
            {
                temp->setLeft(temp2);
                return;
            }
        }
        else if(d>=temp->getData())
        {
            if(temp->getRight()==NULL)
            {
                temp->setRight(temp2);
                return;
            }
        }
        if(d<temp->getData())
        {
            add(temp->getLeft(),d,temp2);
        }
        else
            add(temp->getRight(),d,temp2);



    }

    void displayIn(Node *temp)
    {

        if(temp==NULL)
        {
            cout<<"NO Data in the tree!"<<endl;
            return;
        }
        else
        {

            if(temp->getLeft()!=NULL)
                displayIn(temp->getLeft());
            cout<<temp->getData()<<endl;
            if(temp->getRight()!=NULL)
                displayIn(temp->getRight());
        }

    }//display in inorder...
    void displayPre(Node *temp)
    {
        if(temp==NULL)
        {
            //  cout<<"No data in the Tree!"<<endl;
            return;
        }
        else
        {
            //temp->getLeft()!=NULL;
            cout<<temp->getData()<<endl;
            displayPre(temp->getLeft());
            //temp->getRight()!=NULL;
            displayPre(temp->getRight());
        }


    }//displaying in preorder...
    void displayPost(Node *temp)
    {
        if(temp==NULL)
            return;
        else
        {
            //temp->getLeft()!=NULL;
            displayPost(temp->getLeft());
            //temp->getRight()!=NULL;
            displayPost(temp->getRight());
            cout<<temp->getData()<<endl;
        }


    }//display post order..
    int bsearch(int v)
    {
        Node *temp=root;
        while(1)
        {
            if(temp==NULL)
            {
                cout<<"NO Matching Value!"<<endl;
                break;
            }
            if(temp->getData()==v)
            {
                cout<<"It has been found!"<<endl;
                cout<<temp->getData()<<endl;
                break;
            }
            else if(v<temp->getData())
            {
                temp=temp->getLeft();

            }
            else if(v>temp->getData())
            {
                temp=temp->getRight();
            }

        }
    }//search by loop...
    void searchR(Node *temp,int y)
    {
        if(temp==NULL)
        {
            cout<<"NO match Found...."<<endl;
            return;
        }
        if(y==temp->getData())
        {
            cout<<"Match Found..."<<endl;
            cout<<temp->getData()<<endl;
            return;
        }
        else if(y<temp->getData())
        {
            searchR(temp->getLeft(),y);
            return;
        }
        else if(y>=temp->getData())
        {
            searchR(temp->getRight(),y);
            return;
        }


    }
    void removeR(int a)
    {

        Node *left;
        Node *right;
        Node *temp=root;
        if(root==NULL)
        {
            cout<<"No Data!"<<endl;
            return;
        }
        if(a==root->getData())
        {
            if(root->getRight()==NULL && root->getLeft()==NULL)
            {
                root=NULL;
                return;
            }
            if(root->getLeft()!=NULL)
            {
                left=root->getLeft();
                if(left->getRight()==NULL)
                {
                    root->setData(left->getData());
                    root->setLeft(left->getLeft());
                    return;
                }
                if(left->getRight()!=NULL)
                {
                    while(left->getRight()->getRight()!=NULL)
                    {
                        left=left->getRight();
                    }
                    root->setData(left->getRight()->getData());

                    if(left->getRight()->getLeft()!=NULL)
                    {
                        left->setRight(left->getRight()->getLeft());
                    }

                    else
                        left->setRight(NULL);
                }

            }
            else if(root->getRight()!=NULL)
            {
                right=root->getRight();

                if(right->getLeft()==NULL)
                {
                    root->setData(right->getData());
                    root->setRight(right->getRight());
                    return;
                }
                if(right->getLeft()!=NULL)
                {
                    while(right->getLeft()->getLeft()!=NULL)
                    {
                        right=right->getLeft();
                    }
                    root->setData(right->getLeft()->getData());

                    if(right->getLeft()->getRight()!=NULL)
                    {
                        right->setLeft(right->getLeft()->getRight());
                    }

                    else
                        right->setLeft(NULL);


                }

            }
        }
        else
        {
            removeV(a);
        }

    }
    void removeV(int x)
    {
        Node *temp = root;
        Node *temp2;
        Node *temp3;
        if(temp==NULL)
        {
            cout<<"No Value In the Tree!"<<endl;
        }
        while(temp!=NULL)
        {
            if(x==temp->getData())
            {
                if(temp->getLeft()== NULL && temp->getRight()== NULL)
                {
                    cout<<"leaf is:"<<temp->getData()<<endl;
                    cout<<"Removing....."<<temp->getData()<<endl;
                    temp2->setLeft(NULL);
                    temp2->setRight(NULL);
                    return;
                }//removing leaf..
                if(temp->getLeft()==NULL && temp->getRight()!=NULL)
                {
                    cout<<"Value is:"<<temp->getData()<<endl;
                    cout<<"Removing....."<<temp->getData()<<endl;
                    temp2->setRight(temp->getRight());
                    return;
                }//removing value which has no left..
                if(temp->getLeft()!=NULL && temp->getRight()==NULL)
                {
                    cout<<"Value is:"<<temp->getData()<<endl;
                    cout<<"Removing....."<<temp->getData()<<endl;
                    temp2->setRight(temp->getLeft());
                    return;
                }//removing value which has no right..
                if(temp->getLeft()!=NULL && temp->getRight()!=NULL)
                {
                    cout<<"Value is :"<<temp->getData()<<endl;
                    cout<<"Removing....."<<temp->getData()<<endl;
                    temp3=temp->getRight();
                    temp=temp->getLeft();
                    temp2->setRight(temp);
                    while(temp->getRight()!=NULL)
                    {
                        temp=temp->getRight();
                    }
                    temp->setRight(temp3);
                    return;
                }//removing value having both left and Right

            }

            if(x<temp->getData())
            {
                temp2=temp;
                temp=temp->getLeft();
            }
            if(x>temp->getData())
            {
                temp2=temp;
                temp=temp->getRight();
            }
            if(temp==NULL)
            {
                cout<<"NO matching value found!"<<endl;
                return;

            }
            //shifting..
        }

    }
    void recursiveS(int value)
    {
        Node *temp=root;
        if(root==NULL)
        {
            cout<<"no Data!"<<endl;
            return;
        }
        else
            deleteViaRecursion(temp,value);
            return;
        }
    void deleteViaRecursion(Node *temp,int value)
    {

        Node *temp2;
        if(temp==NULL){
            cout<<"NO Data found!"<<endl;
            return;
        }
        if(value==temp->getData())
        {
            cout<<"Data has been Found!"<<endl;
            removeTR(temp,temp2);
            return;
        }
        if(value<temp->getData())
        {
            temp2=temp;
            deleteViaRecursion(temp->getLeft(),value);
            return;
        }
        if(value>temp->getData())
        {
            temp2=temp;
            deleteViaRecursion(temp->getRight(),value);
            return;

        }

    }
   void removeTR(Node *temp,Node *temp2)
    {
        if(temp->getLeft()==NULL && temp->getRight()==NULL)
        {

            if(temp2->getRight()==temp)
            {
                temp2->setRight(NULL);
                return;
            }
            if(temp2->getLeft()==temp)
            {
                temp2->setLeft(NULL);
                return;
            }
        }
        if(temp->getLeft()!=NULL && temp->getRight()==NULL)
        {


            if(temp2->getRight()==temp)
                temp2->setRight(temp->getLeft());
            else
                temp2->setLeft(temp->getLeft());
            return;
        }
        if(temp->getLeft()==NULL && temp->getRight()!=NULL)
        {

            if(temp2->getRight()==temp)
                temp2->setRight(temp->getRight());
            else
                temp2->setLeft(temp->getRight());
            return;
        }
        if(temp->getLeft()!=NULL && temp->getRight()!=NULL)
        {

            if(temp->getLeft()->getRight()!=NULL)
            {
                Node *extreme_right=rightmost(temp->getLeft());
                temp->setData(extreme_right->getRight()->getData());
                if(extreme_right->getRight()->getLeft()!=NULL)
                    extreme_right->setRight(extreme_right->getRight()->getLeft());
                else
                    extreme_right->setRight(NULL);
                return;
            }
            else
            {
                temp->setData(temp->getLeft()->getData());
                temp->setLeft(temp->getLeft()->getLeft());
            }
            return;
        }
    }

    Node * rightmost(Node *right)
    {

        if(right->getRight()->getRight()==NULL)
            return(right);
        else
            return(rightmost(right->getRight()));
    }







};




int main()
{
    Bst b;
    b.insertV(10);
    b.insertV(7);
    b.insertV(17);
    b.insertV(27);
    b.insertV(37);
    b.insertV(70);
    b.insertV(9);
    b.insertV(23);
    b.insertV(12);
    b.insertV(157);
    b.insertV(15);
    b.recursiveS(12);
    b.displayIn(b.root);
    cout<<"-----------------------------------------------"<<endl;
    b.displayIn(b.root);
    cout<<"-----------------------------------------------"<<endl;

    b.displayIn(b.root);
    cout<<"-----------------------------------------------"<<endl;

    b.displayIn(b.root);
    cout<<"-----------------------------------------------"<<endl;



    //b.searchR(b.root,8);

    int s=0;
    int x;

    do
    {
        cout<<"------------MENU~BINARY SEARCH TREE------------"<<endl;
        cout<<"press 1 to Add using Loop"<<endl;
        cout<<"press 2 to Add using Recursion"<<endl;
// cout<<"press 3 to Remove value from Root!"<<endl;
        cout<<"press 3 to Remove Value in the Tree!"<<endl;
        cout<<"press 4 to Search any Value"<<endl;
        cout<<"press 5 to Display in In Order"<<endl;
        cout<<"press 6 to Display in Pre Order"<<endl;
        cout<<"press 7 to Display in Post Order"<<endl;
        cin>>s;
        switch (s)
        {
        case 1:
            cout<<"Enter the value you want to Add!"<<endl;
            cin>>x;
            b.insertV(x);

            break;
        case 2:

            cout<<"Enter the value you want to Add!"<<endl;
            cin>>x;
            b.insertRecursion(x);
            break;
        case 3:
            cout<<"Enter The value you want to remove from the Tree!"<<endl;
            cin>>x;
            b.removeR(x);
            break;
        case 4:
            /*cout<<"Enter the Value you want to remove from Tree"<<endl;
            cin>>t;
            b.removeV(t);*/
            cout<<"Enter the Value you want to search!"<<endl;
            cin>>x;
            b.bsearch(x);
            break;
        case 5:

            b.displayIn(b.root);
            break;
        case 6:
            b.displayPre(b.root);
            break;
        case 7:

            b.displayPost(b.root);
            break;
        default:
            cout<<"Unkown Command!!!"<<endl;
            break;
        }
        cout<<"If you want to close the program press 0 otherwise press 1!"<<endl;
        cin>>s;
    }
    while(s!=0);





    return 0;
}
