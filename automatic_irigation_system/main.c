#include<reg51.h>

#include "lcd.h"
#include "delay.h"
#include "adc.h"

unsigned char adc_result = 0;
unsigned int adc_temp = 0;
sbit adc_clk   = P3^0;     // THIS IS FOR THE CLOCK FREQUENCY PROVIDED  TO THE ADC
sbit relay_pin = P2^3;


void timer_0() interrupt 1
{
	adc_clk = ~ adc_clk;
}


void main()
{
	relay_pin = 0;

	TMOD = 0x02;
	TH0 = 0xFD;
	LCD_init();  //INITIALISE THE LCD
	
	LCD_DisplayString("AUTOMATIC");
	
	// GO TO LINE TWO
	LCD_GoToXY(1,0);
	LCD_DisplayString("IRRIGATION SYSTEM");
	
	delay_ms(500);
	
	LCD_Clear();  // CLEAR THE LCD SCREEN
	LCD_GoToLINEone();
	
	// INITILAISING THE ADC

		ADC_init();
  LCD_DisplayString("TEMRETURE : ");
		
	IE=0x82;
	
	TR0 = 1;  // START THE TIMER;

	
	while(1)
	{
		
		//compiler ---- sourav
		// GET THE ADC VALUE OF CHANNEL 8
		adc_result = ADC_StartConversion(7);   // 0x10
		
		// GO TO THE LINE TWO AND DISPLAY THE ADC VALUE
		LCD_GoToLINEtwo();
		//LCD_DisplayNumber(adc_result);
 
   adc_temp = (adc_result);   //0x20
		
		
			
		
		if((adc_temp)<50)
		{
			relay_pin =  0;
		}
		else
		{
			relay_pin = 1;
		}

   LCD_DisplayNumber(adc_temp);		
	}
}