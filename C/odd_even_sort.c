/**
 * Date: 07-09-2021
 * by eddybruv
 **/

#include <stdio.h>
#include <stdbool.h>

void swap(int *, int *);
void odd_even(int *, int);

int main(void)
{
    int size;
    printf("How many numbers do you wish to sort: ");
    scanf("%d", &size);

    int numbers[size];
    printf("Enter numbers: ");
    for (int i = 0; i < size; i++)
        scanf("%d", &numbers[i]);

    odd_even(numbers, size);

    printf("Sorted array: ");
    for(int i = 0; i < size; i++)
        printf("%d ", numbers[i]);

    return 0;
}

void swap(int *first, int *second)
{
    int temp = *first;
    *first = *second;
    *second = temp;
}

void odd_even(int *numbers, int size)
{
    bool is_sorted = false;

    while(!is_sorted)
    {
        is_sorted = true;
        for(int i = 0; i <= size - 2; i += 2){
            if(numbers[i] > numbers[i + 1]){
                swap(&numbers[i], &numbers[i+1]);
                is_sorted = false;
            }    
        }

        for(int i = 1; i < size; i += 2){
            if(numbers[i] > numbers[i + 1]){
                swap(&numbers[i], &numbers[i+1]);
                is_sorted = false;
            }
        }    
    }
}