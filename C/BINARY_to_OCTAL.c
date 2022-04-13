#include <stdio.h>
#include <math.h>
int convert(long long bin);
int main()
{
    long long bin;
    printf("Enter a binary number: ");
    scanf("%lld", &bin);
    printf("%lld in binary = %d in octal", bin, convert(bin));
    return 0;
}
int convert(long long bin)
{
    int oct = 0, dec = 0, i = 0;
    while (bin != 0)
    {
        dec += (bin % 10) * pow(2, i);
        ++i;
        bin /= 10;
    }
    i = 1;
    while (dec != 0)
    {
        oct += (dec % 8) * i;
        dec /= 8;
        i *= 10;
    }
    return oct;
}