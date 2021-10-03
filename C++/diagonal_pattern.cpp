
#include <iostream>
using namespace std;

int main() {

    int t;
    cin>>t;

    while(t--)
    {
        int n;
        cin>>n;

        int Arr[n][n];

        int row=1;
        Arr[0][0]=1;
        for(int j=1;j<n;j++)
        {
            Arr[0][j]=j+row;
            row=Arr[0][j];
        }

        int col=Arr[0][n-1];
        for(int i=1,no=n;i<n;i++)
        {
            Arr[i][n-1]=col+no;
            no--;
            col=Arr[i][n-1];

        }


        for(int i=0,j=1;j<=n-1;j++)
        {
            int row_index=i;
            int col_index=j;
            while(col_index!=i and row_index!=j)
            {
                Arr[row_index+1][col_index-1]=Arr[row_index][col_index]+1;
                row_index++;
                col_index--;
            }
        }


        for(int j=n-1,i=0;i<=n-1;i++)
        {
            int row_index=i;
            int col_index=j;
            while(col_index!=i and row_index!=j)
            {
                Arr[row_index+1][col_index-1]=Arr[row_index][col_index]+1;
                row_index++;
                col_index--;
            }
        }


        for(int i=0;i<n;i++)
        {
            for(int j=0;j<n;j++)
            {
                cout<<Arr[i][j]<<" ";
            }
            cout<<endl;
        }
    }

    return 0;
}
