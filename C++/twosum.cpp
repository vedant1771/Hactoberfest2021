#include <iostream>
 
using namespace std;
 
// Function to find and print pair
bool chkPair(int A[], int size, int x) {
    for (int i = 0; i < (size - 1); i++) {
        for (int j = (i + 1); j < size; j++) {
            if (A[i] + A[j] == x) {
                cout << "Pair with a given sum " << x << " is (" << A[i] << ", " << A[j] << ")"
                  << endl;
 
                return 1;
            }
        }
    }
 
    return 0;
}
 
int main(void) {
    int A[] = {0, -1, 2, -3, 1};
    int x = -2;
    int size = sizeof(A) / sizeof(A[0]);
 
    if (chkPair(A, size, x)) {
        cout << "Valid pair exists" << endl;
    }
    else {
        cout << "No valid pair exists for " << x << endl;
    }
 
    return 0;
}
