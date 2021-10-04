
from pygame import mixer
from tkinter import *
import os

def playsong():
    currentsong=playlist.get(ACTIVE)
    print(currentsong)
    mixer.music.load(currentsong)
    songstatus.set("Playing")
    mixer.music.play()

def pausesong():
    songstatus.set("Paused")
    mixer.music.pause()

def stopsong():
    songstatus.set("Stopped")
    mixer.music.stop()

def resumesong():
    songstatus.set("Resuming")
    mixer.music.unpause()    

root=Tk()
root.title('Ankys Music player')

mixer.init()
songstatus=StringVar()
songstatus.set("choosing")

#playlist--------------->>>>>>>>>>

playlist=Listbox(root,selectmode=SINGLE,bg="black",fg="white",font=('arial',15),width=40)
playlist.grid(columnspan=5)
# add your play list here
os.chdir(r'C:\Users\Sacred Student\Desktop\StudyTonight\songs')   # add here
songs=os.listdir()
for s in songs:
    playlist.insert(END,s)

playbtn=Button(root,text="PLAY",command=playsong)
playbtn.config(font=('arial',20),bg="DodgerBlue2",fg="white",padx=7,pady=7)
playbtn.grid(row=1,column=0)

pausebtn=Button(root,text="PAUSE",command=pausesong)
pausebtn.config(font=('arial',20),bg="yellow",fg="black",padx=7,pady=7)
pausebtn.grid(row=1,column=1)

stopbtn=Button(root,text="STOP",command=stopsong)
stopbtn.config(font=('arial',20),bg="Red",fg="white",padx=7,pady=7)
stopbtn.grid(row=1,column=2)

Resumebtn=Button(root,text="RESUME",command=resumesong)
Resumebtn.config(font=('arial',20),bg="orange",fg="white",padx=7,pady=7)
Resumebtn.grid(row=1,column=3)

mainloop()