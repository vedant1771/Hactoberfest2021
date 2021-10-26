#include<reg51.h>
#include "lcd.h"
#include "delay.h"

#define databus  P0        // LCD DATABUS IS CONNECTED TO PORT 0

sbit rs = P2^0;        //  REGISTER SELECT IS CONNECTED TO PORT 2.0
sbit rw = P2^1;       //  READ / WRITE PIN IS CONNECTED TO THE PORT 2.1
sbit en = P2^2;      // ENABLE PIN IS CONNECTED PORT 2.2

/* 16*2 LCD SPECIFICATIONS */

#define LCDMAXLINES 2
#define LCDMAXCHARS 16
#define LINEone 0x80
#define LINEtwo 0xc0
#define Blankspace ' '


void LCD_enablePulse()
{

	en = 1;
	delay_us(100);  // pulse width > 230nsec
	en = 0;
	delay_us(10);  // hold time
}

void LCD_init()
{
	
	delay_us(5000);
	databus = 0x00; // SET IT AS THE OUTPUT PORT;
	
	
	LCD_Cmdwrite(0x38);   // LCD 2 LINES , 5*7 MATRIX
	LCD_Cmdwrite(0x0E);   // DISPLAY ON CURSOR ON;
	LCD_Cmdwrite(0x01);    // clear the LCD
	LCD_Cmdwrite(LINEone);    // MOVE THE CURSOR T0 THE LINE FIRST POSITION
	
}


void LCD_Cmdwrite(unsigned char cmd )
{
	databus = cmd;   // SEND THE COMMAND TO THE LCD
	rs = 0;          // SELECT THE COMMAND REGISTER
	rw = 0;          //SELECTNG THR WRITE OPERATION
	
	LCD_enablePulse(); 
	
	delay_ms(1);
	
}

void LCD_Datawrite( unsigned char dat )  
{
	databus = dat;
	rs = 1; // to select the data register
	rw = 0;   // write operation
	LCD_enablePulse();
	
	delay_ms(1);
}


void LCD_Clear()
{
	LCD_Cmdwrite(0x01);     // CLEAR THE LCD AND GO TO FIRST LINE FIRST POSITION;
	LCD_Cmdwrite(LINEone);
	
}


void LCD_GoToLINEone()
{
	LCD_Cmdwrite(LINEone);    // MOVE THE CURSOR TO THE FIRST LINE FIRST POSITION
}

void LCD_GoToLINEtwo()
{
	LCD_Cmdwrite(LINEtwo);    // MOVE THE CURSOR TO THE LINE TWO
}


void LCD_GoToXY(char row, char col)
{
	char pos;    //THIS WILL HAVE THE COMPUTED HEXADECIMAL VALUE OF THE POSITION TO WHICH THE CURSOR IS TO BE MOVED
	
	if( row< LCDMAXLINES )
	{
		pos = LINEone | (row<<6);  // IF THE ROW->0 THEN THIS STATEMENT WILL MOVE IT TO THE POS = 0X80 AND IF ROW->1 THEN POS = 0XC0 
		
		if( col < LCDMAXCHARS)
		{
			 pos = pos + col;
		}
	}
	
	LCD_Cmdwrite(pos);
}


void LCD_DisplayString(unsigned char *string_ptr)
{
	while(*string_ptr!='\0')
	{
		LCD_Datawrite(*string_ptr);
		string_ptr++;
	}
}



void LCD_DisplayNumber(unsigned int num)
{                                             
     LCD_Datawrite((num/10000)+0x30);
	   num = num%10000; 
	
	   LCD_Datawrite((num/1000)+0x30);
	   num = num%1000;
	
	   LCD_Datawrite((num/100)+0x30);
	   num = num%100;
	
	   LCD_Datawrite((num/10)+0x30);
	   
	   LCD_Datawrite((num%10)+0x30);
	
}