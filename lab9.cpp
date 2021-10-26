#include<iostream>
using namespace std;
class Heap{
  int arr[10]={-1};
  int i=0;
public:
  void Add(int value)
  {
    if(i>=0 || i<10)
    {
      arr[i]=value;
      int k=i;
      check(k);
    }
    else
    cout << "Array is  Full:" << endl;
    i++;
  }
  void check(int k)
  {
    if(k==0)
    return;
    if(arr[k]>arr[(k-1)/2])
    {
      int temp=arr[(k-1)/2];
      arr[(k-1)/2]=arr[k];
      arr[k]=temp;
    }
    k--;
    check(k);
  }
  void remove()
  {
    int temp=0;
    int k=--i;
    arr[temp]=arr[k];
    arr[k]=-1;
    for( k=0; k<i; k++)
    {
      if(arr[2*k+1]<arr[2*k+2])
      {
          if(arr[k]<arr[2*k+2])
          {
            int temp2=arr[2*k+2];
            arr[2*k+2]=arr[k];
            arr[k]=temp2;
          }
      }
      else
      {
        if(arr[k]<arr[2*k+1])
        {
          int temp2=arr[2*k+1];
          arr[2*k+1]=arr[k];
          arr[k]=temp2;
        }
    }


    }

  }
  void heap_check()
  {
    for (int k=0; k<i; k++)
    {
      if(arr[k]!=-1)
      continue;
      else
      {
        cout << "It is not a heap:" << endl;
        break;
      }
      if(arr[(k-1)/2]>arr[k])
      continue;
      else
      {
        cout << "It is not a heap:" << ;
        break;

      }
    }
    cout << "It is a heap:" << ;
  }
  void Top()
  {
    cout << "Array Top:" << array[0]<<endl;
  }

    void Display()
        {
          for(int k=0; k<i; k++)
            {
              cout  <<"index:"<<k<< "  Value:" <<array[k]<<endl;
            }
          }

};
int main()
{
  Heap obj;
  int condition,data;
do {
    cout << "Press 1 to add value:" << endl;
    cout << "Press 2 to remove value:" << endl;
    cout << "Press 3 to Display:" << endl;
    cout << "Press 4 to check heap or not:" << endl;
    cout << "Press 5 to check Top of heap:" << endl;
    cin >> condition;
  switch (condition)
  {
  case 1:
      cout << "Give the value you want to add:" << endl;
      cin >> data;
      obj.Add(data);
      cout << "************************" << endl;
      obj.Display();
      cout << "************************" << endl;
      break;
  case 2:
        cout << "Removing......" << endl;
      obj.remove();
  case 3:
      cout << "************************" << endl;;
      obj.Display();
      cout << "************************" << endl;
      break;
  case 4:
      obj.heap_check();
      break;
  case 5:
  obj.Top();
      default:
      cout << "You have given a wrong input:" << endl;
      break;
    }
      std::cout << "If you want to continue Press any number else Press ..0.." << endl;
      std::cin >> condition;

} while(condition!=0);
  return(0);
}
