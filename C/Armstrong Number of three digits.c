#include <stdio.h>

// return if a number is armstong or not
int is_armstrong(int num) {
    int originalNum, remainder, result = 0;
    originalNum = num;

    while (originalNum != 0) {
       // remainder contains the last digit
        remainder = originalNum % 10;

       result += remainder * remainder * remainder;

       // removing last digit from the orignal number
       originalNum /= 10;
    }
    
    return num == result;
}
    
int main() {
    int num;
    printf("Enter a three-digit integer: ");
    scanf("%d", &num);
    
    if(is_armstrong(num))
        printf("%d is an Armstrong number.", num);
    else
        printf("%d is not an Armstrong number.", num);

    return 0;
}
