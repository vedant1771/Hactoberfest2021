#include <stdio.h>
#include <string.h>

int main()
{

  char S[30];

  printf("Input String: ");
  scanf("%s",&S);


  int length= strlen(S);


  for(int i=0; i<length; i++){


    for(int j=i+1; j<length; j++){
      if(S[i] == S[j]){

        for(int k=j; k<length; k++){
          S[k] = S[k+1];
        }
        length--;
      }
    }
  }


  printf("After remove duplicates:  %s",S);

  return 0;
}
