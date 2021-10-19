#include <stdio.h>


int main()
{
    char str[]="Alami Ahmad";
    int n=11;
  printf("BEFORE SWAP:%s\n",str);
    swap(str,n);
    
    return 0;
}

void swap(char* str, int n)
{
    char ch;
    int i;
    if(n%2==0){
     for(i=0;i<(n/2);i++){
         ch=*(str+i);
         *(str+i)= *(str+i+(n/2));
         *(str+i+(n/2))=ch;
        
     }
    }
    else{
    
         for(i=0;i<(n/2);i++){
         ch=*(str+i);
         *(str+i)= *(str+i+1+(n/2));
         *(str+i+1+(n/2))=ch;
    }
    }
     printf("AFTER SWAP:%s",str);
}
