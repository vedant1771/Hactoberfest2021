#include<reg51.h>

#include "lcd.h"
#include "delay.h"


void delay_us(unsigned int us_count)
 {  
    while(us_count!=0)
      {
         us_count--;
       }
   }
 
	 void delay_ms(unsigned int ms_count)
 {
        while(ms_count!=0)
         {
            delay_us(112);   //delay_us is called to generate 1ms delay
             ms_count--;
            }
   }
 
	 void delay_sec(unsigned char sec_count)
 {
 
 
     while(sec_count!=0)
      {
         delay_ms(1000);    //delay_ms is called to generate 1sec delay
         sec_count--;
        }
 }