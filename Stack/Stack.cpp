#include<bits/stdc++.h>
#define size 200
using namespace std;
class stacks
{
    public:
    
    int arr[size];
    int top;
    
    stacks()
    {
        top = -1;
    }

    void push(int x)
    {
        if (top + 1 < size)
        {
            top += 1;
            arr[top] = x;
        }
        else
        {
            cout << "The Stack is under overflow condition :";
            cout << "\n Kindly pop out some elements :";
        }
    }

    void pop()
    {
        if (top <= -1)
        {
            cout << "The stack is under underflow condition :";
            cout << "Kindly insert some elements :";
        }
        else
        {
            top = top - 1;
        }
    }

    void top_element()
    {
        cout<<arr[top];
    }
};

int main()
{
    stacks s;
    s.push(5);
    s.push(6);
    s.push(8);
    s.top_element();
    s.pop();
    s.top_element();
    s.pop();
    s.top_element();
    
    return 0;
}