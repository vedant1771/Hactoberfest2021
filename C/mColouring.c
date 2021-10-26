#include <stdio.h>
#include <conio.h>
int m,n,co=0,count=0;
int g[50][50];
int x[50];

void writeGraph(){
    co=1;
    for(int i=1;i<=n;i++){
        printf("%d\t",x[i]);
    }
    count++;
    printf("\n");
}
void nextValue(int k){
    int j;
    while(1){
        x[k]=(x[k]+1)%(m+1);
        if(x[k]==0)
        return;
        for(j=1;j<=n;j++)
            if(g[k][j]!=0 && x[k]==x[j])
            break;
        if(j==(n+1))
        return;
    }
}
void mColoring(int k){
    while(1){
        nextValue(k);
        if (x[k]==0)
        return;
        if(k==n)
        writeGraph();
        else
        mColoring(k+1);
    }
}

int main()
{
    printf("no of vertics:");
    scanf("%d",&n);
    printf("enter the adjacency matrix:\n");
    for(int i=1;i<=n;i++)
        for(int j=1;j<=n;j++)
             scanf("%d",&g[i][j]);
    printf("solution\n");
    m=0;
    while(m<=n){
        m++;
        mColoring(1);
        if(co==1)
        break;
    }
    printf("\n no of solution: %d",count);
    printf("\n the chromatic number: %d",m);

    return 0;
}
