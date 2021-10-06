import cv2
import numpy as np
from pyzbar.pyzbar import decode
from tkinter import *
from tkinter import messagebox
import pyqrcode
import webbrowser

def qr_code_maker():
    root = Tk()
    root.geometry("570x400")
    root.title('qr code reader')
    root.wm_iconbitmap('or code.ico')
    root.configure(bg='blue')

    ################################################ Fuctions
    def Generate_QR_code():
        QR_Id = my_qr_code_entry.get()
        QR_Name = my_qr_code_entry2.get()
        QR_Message = my_qr_code_entry3.get()
        Message_QR = 'Name :' + QR_Name + '\n' + 'Id :' + QR_Id + '\n' + 'Message :' + QR_Message
        url = pyqrcode.create(Message_QR)
        url.svg('qr_code7.svg', scale=20)

    def Clear():
        my_qr_code_entry.delete(0, END)
        my_qr_code_entry2.delete(0, END)
        my_qr_code_entry3.delete(0, END)

    def Quit():
        res = messagebox.askokcancel('Notification', 'are you sure you want to Quit ?')
        if (res == True):
            root.destroy()
        else:
            pass

    ################################################# Labels
    my_qr_code_machine_id_label = Label(master=root, text='Enter your Id :', bg='powder blue', fg='red', width=20,
                                        height=2,
                                        font=('times', 12, 'italic bold'))
    my_qr_code_machine_id_label.place(x=10, y=20)

    my_qr_code_machine_name_label = Label(master=root, text='Enter your Name :', bg='powder blue', fg='red', width=20,
                                          height=2,
                                          font=('times', 12, 'italic bold'))
    my_qr_code_machine_name_label.place(x=10, y=80)

    my_qr_code_machine_Message_label = Label(master=root, text='Enter your Message :', bg='powder blue', fg='red',
                                             width=20, height=2,
                                             font=('times', 12, 'italic bold'))
    my_qr_code_machine_Message_label.place(x=10, y=140)

    my_qr_code_machine_Notification_label = Label(master=root, text='Notification :', bg='powder blue', fg='red',
                                                  width=10, height=2,
                                                  font=('times', 15, 'underline bold'))
    my_qr_code_machine_Notification_label.place(x=10, y=350)

    my_qr_code_machine_Notification_Message_label = Label(master=root, text='', bg='powder blue', fg='red', width=30,
                                                          height=2,
                                                          font=('times', 15, 'bold'))
    my_qr_code_machine_Notification_Message_label.place(x=200, y=350)

    ################################################## Entrys
    my_qr_code_entry = Entry(master=root, width=25, bd=5, bg='red', font=('times', 17, 'italic bold'))
    my_qr_code_entry.place(x=250, y=20)

    my_qr_code_entry2 = Entry(master=root, width=25, bd=5, bg='red', font=('times', 17, 'italic bold'))
    my_qr_code_entry2.place(x=250, y=80)

    my_qr_code_entry3 = Entry(master=root, width=25, bd=5, bg='red', font=('times', 17, 'italic bold'))
    my_qr_code_entry3.place(x=250, y=140)

    ################################################### Buttons

    def enter_image_generator(e):
        qr_image_generator['bg'] = 'purple2'

    def leave_image_generator(e):
        qr_image_generator['bg'] = 'powder blue'

    def enter_clear(e):
        qr_clear_id['bg'] = 'purple2'

    def leave_clear(e):
        qr_clear_id['bg'] = 'powder blue'

    def enter_quit(e):
        qr_quit['bg'] = 'purple2'

    def leave_quit(e):
        qr_quit['bg'] = 'powder blue'

    qr_image_generator = Button(master=root, text='Generate Qr code', width=15, font=('times', 10, 'bold'), bd=10,
                                activebackground='blue', bg='powder blue', command=Generate_QR_code)
    qr_image_generator.place(x=10, y=250)

    qr_clear_id = Button(master=root, text='Clear', width=15, font=('times', 10, 'bold'), bd=10,
                         activebackground='blue', bg='powder blue', command=Clear)
    qr_clear_id.place(x=210, y=250)

    qr_quit = Button(master=root, text='Quit', width=15, font=('times', 10, 'bold'), bd=10, activebackground='blue',
                     bg='powder blue', command=Quit)
    qr_quit.place(x=410, y=250)

    qr_image_generator.bind("<Enter>", enter_image_generator)
    qr_image_generator.bind("<Leave>", leave_image_generator)

    qr_clear_id.bind("<Enter>", enter_clear)
    qr_clear_id.bind("<Leave>", leave_clear)

    qr_quit.bind("<Enter>", enter_quit)
    qr_quit.bind("<Leave>", leave_quit)
    root.mainloop()

def scan_qr_code():
    cap = cv2.VideoCapture(0)



    while True:
        success,img = cap.read()
        for barcode in decode(img):
            myData = barcode.data.decode('utf-8')
            pts = np.array([barcode.polygon],np.int32)
            print([pts])
            print([barcode.polygon])
            cv2.polylines(img,pts,False,(2,255,0),2)
            pts2 = barcode.rect
            print(pts2[0])
            cv2.putText(img,myData,(pts2[0],pts2[1]),cv2.FONT_HERSHEY_COMPLEX,0.7,(255,0,255),2)
            try:
                with open("qr_code_data.txt",'w') as f:
                    f.write(myData)
                    f.close()
            except:
                with open("qr_code_data.txt", 'x') as f:
                    f.close()


        cv2.putText(img, "please show the QR CODE to scan", (10, 20), cv2.FONT_HERSHEY_COMPLEX, 0.9,(0,255,0),2)
        cv2.imshow('Result',img)
        if cv2.waitKey(1) == 27:
            break
        if cv2.waitKey(1) & 0xFF == ord('a'):
            webbrowser.open(myData)

root = Tk()
root.geometry("470x300")
root.configure(bg="Powder Blue")
Button(root,text="make qr code",command=qr_code_maker,bd=5,width=30,bg="POWDER BLUE").pack()
Button(root,text="scan qr code",command=scan_qr_code,bd=5,width=30,bg="POWDER BLUE").pack(pady=20)
root.mainloop()
