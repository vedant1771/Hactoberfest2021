#include <stdio.h>
#include <stdlib.h>
struct frame
{
    int pgNum;
    int time;
};
int isEmpty(struct frame f[],int m)
{   int count=0,i;
     for(i=0;i<m;i++)
            if(f[i].pgNum==0)
                count++;
      if(count==m)
                return 1;
      else return 0;
}
int linearSearch(struct frame *f,int key,int size)
       {int i;
          for(i=0;i<size;i++)
           {
               if(key==f[i].pgNum)
                     return 1;
           }
           return 0;
        }
int min(struct frame *f,int m)
{           int min,i,index;
             min=f[0].time;
             for(i=0;i<m;i++)
                {    if(min>=f[i].time)
                    {min=f[i].time;
                       index=i;
                    }
                }
                return index;
}
int PageFault(int *a,int n)
{  int ind,count=0,i,m;
    printf("Enter Size of Frame\n");
    scanf("%d",&m);
    struct frame f1[m];
     for(i=0;i<m;i++)
    {
        f1[i].time=0;
        f1[i].pgNum=0;
    }
    for(i=0;i<n;i++)
    {
        if(linearSearch(f1,a[i],m)) {
           }
        else {
                      if(f1[i%m].time==0)
                     {  f1[i%m].pgNum=a[i];
                         f1[i%m].time=i+1;
                         count++; }
                    else  { ind=min(f1,m);
                               f1[ind].pgNum=a[i];
                               f1[ind].time=i+1;
                               count++;
                               }
            }
        }
       return count;
    }
int main()
{  int n,pgfault=0,i;
    printf("Enter Number of pages\n");
    scanf("%d",&n);
    int arr[n];
    printf("Enter Pages\n");
    for(i=0;i<n;i++)
        scanf("%d",&arr[i]);
    pgfault=PageFault(arr,n);
    printf("Number of page fault:%d\n",pgfault);
    return 0;
}
