from tkinter import *
from tkinter.messagebox import showinfo
from tkinter.filedialog import askopenfilename,asksaveasfilename
import os

root=Tk()
root.title("Untitled - Notepad")
root.geometry("430x540")

TextArea = Text(root, font="lucida 13")
file = None
TextArea.pack(expand=True, fill=BOTH)

# Menubar

def newfile():
    global file
    root.title("Untitled-Noptepad")
    file=None
    TextArea.delete(1.0,END)
def openfile():
    global file
    file = askopenfilename(defaultextension=".txt",filetypes=[("All Files","*.*"),("Text Document","*.txt")])
    if file == "":
        file=None
    else:
        root.title(os.path.basename(file) + " - Notepad")
        TextArea.delete(1.0,END)
        f=open(file,"r")
        TextArea.insert(1.0,f.read())
        f.close()

def save():
    global file
    if file==None:
        file=asksaveasfilename(initialfile='Untitled.txt',defaultextension=".txt",filetypes=[("All Files","*.*"),("Text Document","*.txt")])
        if file=="":
            file=None
        else:
            f=open(file,"w")
            f.write(TextArea.get(1.0,END))
            f.close()

            root.title(os.path.basename(file)+ " - Notepad")
            print("File Saved")
    else:
        f = open(file, "w")
        f.write(TextArea.get(1.0, END))
        f.close()


def quitapp():
    root.destroy()

def cut():
    TextArea.event_generate(("<<Cut>>"))
def copy():
    TextArea.event_generate(("<<Copy>>"))
def paste():
    TextArea.event_generate(("<<Paste>>"))
def help_():
    showinfo("Help","Search your query in Google or Contact Gaurav Gupta Mob no. 7055336297")
def credits_():
    showinfo("Notepad","Notepad created by Gaurav Gupta in Python GUI using Tkinter package supported by CodeWithHarry")
menubar=Menu(root)
# File menu
m1=Menu(menubar,tearoff=0)
m1.add_command(label="New",command=newfile)
m1.add_command(label="Open",command=openfile)
m1.add_command(label="Save",command=save)
m1.add_separator()
m1.add_command(label="Exit",command=quitapp)
menubar.add_cascade(label="File",menu=m1)

# Edit menu
m2=Menu(menubar,tearoff=0)
m2.add_command(label="Cut",command=cut)
m2.add_command(label="Copy",command=copy)
m2.add_command(label="Paste",command=paste)
menubar.add_cascade(label="Edit",menu=m2)

# Help menu
m1=Menu(menubar,tearoff=0)
m1.add_command(label="Help",command=help_)
m1.add_command(label="Credits",command=credits_)
menubar.add_cascade(label="Help",menu=m1)

root.config(menu=menubar)

Scroll = Scrollbar(TextArea)
Scroll.pack(side=RIGHT, fill=Y)
Scroll.config(command=TextArea.yview)
TextArea.config(yscrollcommand=Scroll.set)

root.mainloop()
