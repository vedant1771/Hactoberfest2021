/* Date: 14-07-2021
    by eddybruv
    */


#include<stdio.h>


int main(void){

    int num;
    printf("Enter number: ");
    scanf("%d", &num);
    
    int number = num;

    int reverse,  count = 0;
    while (num != 0){
        reverse = num % 10;
        count = count * 10 + reverse;
        num /= 10;
    }

    if(number == count){
        printf("Number is a palindrome number\n");
    }
    else    
        printf("Number is not a palindrome number\n");
    return 0;
}
    
