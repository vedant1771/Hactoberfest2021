#include<stdio.h>  
int main(){    
  int n,r,sum=0,x;    
  printf("enter the number=");    
  scanf("%d",&n);        
  x=n;
//   with the help of while statement in the starting you do not have to press run button again and again
//   just type 0 to exit the loop
  while(n!=0)
  while(n>0){
    r=n%10;
    sum=(sum*10)+r;
    n=n/10;
  }
  if(temp==sum)    
    printf("palindrome number ");    
  else    
    printf("not palindrome");   
  
  printf("enter the number=");    
  scanf("%d",&n);        
  x=n;
  
  return 0;   
}
