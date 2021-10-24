//C program to create a spanning tree from a given graph using DFS algorithm.
#include<stdio.h>  //including the standard input-output header file

int top=-1,a[20][20],vis[20],stack[20];
//declaring global variables

//to add the element to the maintained Stack
void push(int item)
{
    if(top==19)
        printf("STACK OVERFLOW");
    else
        stack[++top]=item;
}
//to delete the element from the maintained Stack
int pop()
{
    int k;
    if(top==-1)     //condition to check for Empty Queue
        return(0);
    else
    {
        k=stack[top--];
        return(k);
    }
}
//Depth First Search recursive algorithm
void dfs(int s,int n)
{
    int i,k;
    push(s);
    vis[s]=1;
    k=pop();
    if(k!=0)
        printf(" %c", (k + 64));
    while(k!=0)
    {
        for(i=1;i<=n;i++)
            if((a[k][i]!=0)&&(vis[i]==0))
            {
                push(i);
                vis[i]=1;
            }
        k=pop();
        if(k!=0)
            printf(" %c ", (k + 64));
    }
    for(i=1;i<=n;i++)
        if(vis[i]==0)
            dfs(i,n);   //invoking the function recursively
}

//the main() function from where execution begins
void main()
{
    int n, i, j;
    char s;
    //declaring local variables
    printf("Total Number Of Vertices: ");
    scanf("%d", &n); //accepting the total number of vertices

    printf("Enter The ADJACENCY MATRIX:\n");
    for (i = 1; i <= n; i++)
    {
        for (j = 1; j <= n; j++)
        {
            scanf("%d", &a[i][j]);
        }
    }

    for (i = 1; i <= n; i++)
        vis[i] = 0;
    scanf("%c");
    printf("\nStarting Vertex: ");
    scanf("%c", &s); //accepting the vertex from where traversal starts
    printf("\nAfter DFS, the SPANNING TREE : ");
    dfs(((int)s - 64), n); //invoking the BFS function
}
//end of program
