// Sample Test Case 
// Input: 4
// Output:
// 
//        * *       
//        * *       
//      * * * *     
//      * * * *     
//    * * * * * *   
//    * * * * * *   
//  * * * * * * * * 
//  * * * * * * * * 


#include<iostream>
using namespace std;

int main(){

    int n;
    cin>>n;

    for(int i=0; i<n; i++){

        for(int k=0;k<2;k++){

            for(int j=0; j<2*(n-i-1); j++){

                cout<<" ";
            }

            for(int j=0; j<i+1; j++){
                cout<<"* * ";
            }

            

            for(int j=0; j<2*(n-i-1); j++){

                cout<<" ";
            }

            cout<<endl;
        }

        
    }

    return 0;
}