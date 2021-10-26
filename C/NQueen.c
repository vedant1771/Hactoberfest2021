#include <stdio.h>
#include <stdlib.h>
#include <conio.h>
#include <math.h>
int x[20],count =0;

void writeQ(int n){
    int i,j;
    printf("\n\nsolution: %d \n:",++count);
    for(i=1;i<=n;++i){
        printf("\n");
        for(j=1;j<=n;j++){
            if(x[i]==j)
            printf("\tQ");
            else
            printf("\t-");
        }
    }
}
int place(int k,int i){
    for(int j=1;j<=k-1;++j){
        if (x[j]==i || abs(x[j]-i)==abs(j-k))
        return 0;
    }
    return 1;
}
void Nqueen(int k,int n){
    for(int i =1;i<=n;i++){
        if(place(k,i)){
            x[k]=i;
            if(k==n)
            writeQ(n);
            else 
            Nqueen(k+1,n);
        }
    }
}
int main()
{
    int n;
    printf("no of Queen:");
    scanf("%d",&n);
    Nqueen(1,n);
    if(count==0)
    printf("sorry no solution");

    return 0;
}
