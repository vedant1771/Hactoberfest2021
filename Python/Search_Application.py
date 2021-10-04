from tkinter import *
from tkinter import messagebox
import wikipedia as wp




class search:
    def __init__(self, root):
        self.root = root
        self.root.title("Search Application |   Developed by Mufaddal Bharmal")
        self.root.config(bg="#6755E3")
        self.root.geometry("1500x700+0+0")
        self.root.resizable(False, True)

        title = Label(self.root, text="Wikipedia Search Application", font=("arial", 40, "bold"), fg="#6755E3",
                      bg="#00FF66").place(x=0, y=0, relwidth=1)

        lbl_sch = Label(self.root, text="Search Word", font=("arial", 30, "bold"), fg="#262626", bg="#6755E3").place(
            x=20, y=100)

        self.store=StringVar()
        self.entry_sch = Entry(self.root, font=("times new roman", 25),textvariable=self.store)
        self.entry_sch.place(x=300, y=105)

        Btn_search = Button(self.root, text="Search", font=("calibri", 30),command=self.word).place(x=690, y=103, width=130, height=50)
        Btn_clear = Button(self.root, text="Clear", font=("calibri", 30),command=self.clear).place(x=910, y=103, width=130,height=50)
        Btn_enab = Button(self.root, text="Enable", font=("calibri", 30), command=self.en).place(x=1130, y=103,width=130,height=50)
        Btn_disab = Button(self.root, text="Disable", font=("calibri", 30), command=self.dis).place(x=1350, y=103, width=130, height=50)

        self.Mode=Label(self.root,bg="#E7A9FE",text="MODE - ")
        self.Mode.place(x=20,y=170)

        Developer = Label(self.root, bg="#6755E3" ,fg="white", font=("CALIBRI",20,"bold"),text="Developed By - Mufaddal Bharmal").place(x=1080, y=160)

        Frame1 = Frame(self.root)
        Frame1.place(x=20, y=200, width=1400, height=500)

        scrolly = Scrollbar(Frame1, orient=VERTICAL)
        scrolly.pack(side=RIGHT, fill=Y)

        self.result_sch = Text(Frame1, bg="pink",bd=3, relief=RIDGE, yscrollcommand=scrolly.set)
        self.result_sch.pack(fill=BOTH, expand=1)

        scrolly.config(command=self.result_sch.yview)

    def en(self):
        self.result_sch.config(state=NORMAL)
        self.Mode.config(text="MODE - "+ "ENABLED")

    def dis(self):
        self.result_sch.config(state=DISABLED)
        self.Mode.config(text="MODE - "+ "DISABLED")

    def clear(self):
        self.result_sch.delete('1.0',END)
        self.Mode.config(text="MODE - ")
        self.store.set("")

    def word(self):
        if self.store.get()=="":
            messagebox.showerror("Error","Enter the word to search")
        else:
            fetch_data=wp.summary(self.store.get())
            self.result_sch.insert('1.0',fetch_data)

root = Tk()
ob = search(root)
root.mainloop()
