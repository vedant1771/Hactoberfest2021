from tkinter import *
import random,string ,pyperclip
screen= Tk()
screen.geometry("500x600")
screen.resizable(0,0)
screen.title("password generator")
Label(screen , text = 'PASSWORD GENERATOR' , font = 'arial 15 bold').pack()
Label(screen , text = 'BY Akash Gupta', font ='arial 15 bold').pack(side=BOTTOM)
pass_label=Label(screen, text ='PASSWORD LENGTH' , font = 'arial 10 bold').pack()
pass_len=IntVar()
length = Spinbox(screen, from_ = 8, to_ = 32 , textvariable = pass_len , width = 15).pack()
pass_str = StringVar()
def Generator():
    password = ''
    for y in range(pass_len.get()):
        password = password + random.choice(string.ascii_uppercase + string.ascii_lowercase + string.digits + string.punctuation)
    pass_str.set(password)
Button(screen, text = "GENERATE PASSWORD" , command = Generator ).pack(pady= 5)
pass_label=Label(screen, text ='GENERATED PASSWORD' , font = 'arial 10 bold').pack()
Entry(screen , textvariable = pass_str).pack()
def Copy_password():
    pyperclip.copy(pass_str.get())

Button(screen, text = 'COPY TO CLIPBOARD', command = Copy_password).pack(pady=5)
#complicated
