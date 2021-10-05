#ifndef _LCD_H
#define _LCD_H
void LCD_init();
void LCD_Cmdwrite(unsigned char);
void LCD_Datawrite(unsigned char);
void LCD_Clear();
void LCD_GoToLINEone();
void LCD_GoToLINEtwo();
void LCD_GoToXY(char , char);
void LCD_DisplayString(unsigned char *);
void LCD_DisplayNumber(unsigned int);

#endif