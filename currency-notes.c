#include <stdio.h>
void main()
{
 int amount=0,f_hund=0,hund=0,fifty=0,twenty=0,ten=0,five=0,two=0,one=0;
 printf("\nEnter amount=");
 scanf("%d",&amount);
 do
 {
 if(amount>=500)
 {
 f_hund=amount/500;
 amount=amount-(f_hund*500);
 }
 else if(amount>=100 && amount<500)
 {
 hund=amount/100;
 amount=amount-(hund*100);
 }
 else if(amount>=50 && amount<100)
 {
 fifty=amount/50;
 amount=amount-(fifty*50);
 }
 else if(amount>=20 && amount<50)
 {
 twenty=amount/20;
 amount=amount-(twenty*20);
 }
 else if(amount>=10 && amount<20)
 {
 ten=amount/10;
 amount=amount-(ten*10);
 }
 else if(amount>=5 && amount<10)
 {
 five=amount/5;
 amount=amount-(five*5);
 }
 else if(amount>=2 && amount<5)
 {
 two=amount/2;
 amount=amount-(two*2);
 }
 else if(amount>=1 && amount<2)
 {
 one=amount/1;
 amount=amount-(one*1);
 }
 }while(amount>0);

 printf("\nNumber of Five Hundred rupees(500) note=%d",f_hund);
 printf("\nNumber of Hundred rupees(100) note=%d",hund);
 printf("\nNumber of Fifty rupees(50) note=%d",fifty);
 printf("\nNumber of Twenty rupees(20) note=%d",twenty);
 printf("\nNumber of Ten rupees(10) note=%d",ten);
 printf("\nNumber of Five rupees(5) note=%d",five);
 printf("\nNumber of Two rupees(2) note=%d",two);
 printf("\nNumber of One rupee(1) note=%d",one);
}
