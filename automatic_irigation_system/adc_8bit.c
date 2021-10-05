#include<reg51.h>

#include "delay.h"
#include "adc.h"


#define adc_databus P1

sbit adc_Start = P3^1;   // ADC START CONVERSION PIN
sbit adc_EOC   = P2^4;  // ADC EOND OF CONVERSION
sbit adc_OE    = P3^3;  //ADC OUTPUT ENABLE PIN
sbit adc_ALE   = P3^4;   // ADC LATCH EABLE
sbit adc_A0    = P3^5;  
sbit adc_A1    = P3^6;     // THIS THREE PIN ARE THE ADRESS LINE PINS
sbit adc_A2    = P3^7;
 
void ADC_init()
{
	adc_Start = 0;        //INITIALIZE ALL THE CONTORL PINS TO ZERO
	adc_ALE = 0;       
	adc_OE = 0; 
	adc_EOC = 1;           // CONFIGURE THE EOC PIN AS I/P
	adc_databus = 0xff;   //  CONFIGURE adc_databus as I/P
}

//compiler ----sourav
unsigned char ADC_StartConversion(char channel)
{
	 unsigned char adc_result; // to store the adc converted value
	
	// THIS IS DONE FOR SELECTING THE APPROPIATE CHANNEL TO BY GETTING THE CHANNEL ADDRESS
	adc_A0 = ((channel>>0) & 0x01 );   
	adc_A1 = ((channel>>1) & 0x01 );               
	adc_A2 = ((channel>>2) & 0x01 );          



	
	adc_ALE = 1; // LATCH THE ADDRESS BY MAKING ALE 1
	delay_us(50);   // DELAY >50ns
	adc_Start = 1;
	delay_us(25);   // DELAY >25ns
	
	
	adc_ALE = 0;
	delay_us(50);
	adc_Start = 0; // PULL DOWN THE START LINE TO ZERO AFTER STARTING THE CONVERSION
	
	
	/*WAIT UNTIL THE CONVERSION IS COMPLETE 
	EOC WILL BE WILL BE AGIN PULLED TO HIGH BY THE HARDWARE ADC0808 ONCE THE CONVERSION IS COMPLETE*/
	
	while(adc_EOC==0);

	
	adc_OE = 1;   // OUTPUT ENABLKE HIGH TO BRING THE DATA TO PORT PINS
	delay_us(25);
	adc_result = adc_databus;  // READ DATA FROM THE ADC DATA BUS
	adc_OE = 0;  // AFTER READING THE DATA OUTPUT ENABLE IS AGAIN MADE 0
	
	
  return (adc_result);   //0x10
	
}

