from tkinter import *
from tkinter import filedialog
from tkinter import font
from tkinter import colorchooser
from tkinter.messagebox import showerror


root = Tk()
root.title("Ande_editor")

root.geometry("1200x660")


global open_status_name, selected
open_status_name = False
selected = False


def all_text_color():
  my_color = colorchooser.askcolor()[1]
  if my_color:
    my_text.config(fg=my_color)


def bg_color():
  my_color = colorchooser.askcolor()[1]
  if my_color:
    my_text.config(bg= my_color)


def text_color():
  my_color = colorchooser.askcolor()[1]
  if my_color:

      color_font = font.Font(my_text, my_text.cget('font'))


      my_text.tag_configure("colored", font=color_font, foreground = my_color)
      current_tags = my_text.tag_names("sel.first")
      if 'colored' in current_tags:
        my_text.tag_remove("colored", "sel.first", 'sel.last')
      else:
        my_text.tag_add("colored", "sel.first", "sel.last")



def Bold_it():
  bold_font= font.Font(my_text, my_text.cget('font'))
  bold_font.configure(weight='bold')

  my_text.tag_configure("bold", font=bold_font)
  current_tags= my_text.tag_names("sel.first")
  if 'bold' in current_tags:
    my_text.tag_remove("bold", "sel.first", 'sel.last')
  else:
    my_text.tag_add("bold", "sel.first", "sel.last")

def italics_it():
  italic_font = font.Font(my_text, my_text.cget('font'))
  italic_font.configure(slant='italic')

  my_text.tag_configure("italic", font=italic_font)
  current_tags = my_text.tag_names("sel.first")
  if 'italic' in current_tags:
    my_text.tag_remove("italic", "sel.first", 'sel.last')
  else:
    my_text.tag_add("italic", "sel.first", "sel.last")

def cut_text(e):
  global selected
  if e:
    selected = root.clipboard_get()
  else:

    if my_text.selection_get():
      selected = my_text.selection_get()
      my_text.delete("sel.first", "sel.last")
      root.clipboard_clear()
      root.clipboard_append(selected)


def copy_text(e):
  global selected

  if e:
    selected = root.clipboard_get()

  if my_text.selection_get():
    selected = my_text.selection_get()
    root.clipboard_clear()
    root.clipboard_append(selected)


def paste_text(e):
  global selected
  if e:
     selected = root.clipboard_get()
  else:
    if selected:
      position = my_text.index(INSERT)
      my_text.insert(position, selected )


def save_file():
  global open_status_name
  if open_status_name:
    text_file = open(open_status_name, 'w')
    text_file.write(my_text.get(1.0, END))
    text_file.close()
    status_bar.config(text= "Saved "+ open_status_name)


  else:
    save_as_file()




def save_as_file():
  text_file = filedialog.asksaveasfilename( title ="Save file", filetypes=(("Text file","*.txt"),("HTML files ", "*.html"),("python ", "*.py"),("All files ","*.*")))
  if text_file:
    p=text_file.split("/")[-1]

    status_bar.config(text= f'{p}   Ande_editor')
    root.title(f'{p} Ande_editor')
    text_file = open(text_file, 'w')
    text_file.write(my_text.get(1.0,END))
    text_file.close()



def new_file():
  my_text.delete("1.0", END)
  status_bar.config(text= "New File         ")

def open_file():
  my_text.delete("1.0", END)
  text_file= filedialog.askopenfilename( title= "Open file ", filetypes=  (("Text file","*.txt"),("HTML files ", "*html"),("python ", "*.py"),("All files ","*.*")))
  if text_file:

    global open_status_name
    open_status_name = text_file

  name= text_file
  p= name.split('/')[-1]
  root.title(f'{p} Ande_editor')
  status_bar.config(text=p)
  text_file= open(text_file , 'r')
  stuff = text_file.read()
  my_text.insert(END, stuff)
  text_file.close()

toolbar_frame = Frame(root)
toolbar_frame.pack(fill=X)


my_frame= Frame(root)
my_frame.pack(pady=5)


text_scroll =Scrollbar(my_frame )

text_scroll.pack(side=RIGHT , fill=Y)


my_menu= Menu(root)
root.config(menu=my_menu)
status_bar =Label(root, text='Ready  ', anchor=E)
status_bar.pack(fill=X, side =BOTTOM , ipady=5)
my_text= Text(my_frame, width = 180 , height=48, font=("helvetica" , 16), selectbackground= "yellow", selectforeground="black", undo = True , yscrollcommand = text_scroll.set)
my_text.pack()


file_menu =Menu(my_menu)
my_menu.add_cascade(label="File", menu= file_menu)
file_menu.add_command(label="New", command= new_file)
file_menu.add_command(label="Open" , command= open_file)
file_menu.add_command(label="Save", command = save_file)
file_menu.add_command(label="Save_As", command= save_as_file)

file_menu.add_separator()
file_menu.add_command(label="Exit", command= root.quit)

edit_menu = Menu(my_menu)
my_menu.add_cascade(label="Edit", menu= edit_menu)
edit_menu.add_command(label="Cut" , command = lambda:cut_text(False), accelerator = "Cntrl+x" )
edit_menu.add_command(label="Copy", command = lambda:copy_text(False), accelerator = "Cntrl+c")
edit_menu.add_command(label='Paste', command = lambda:paste_text(False), accelerator = "Cntrl+v")
edit_menu.add_command(label="Redo", command = my_text.edit_redo, accelerator="Cntrl+y" )
edit_menu.add_command(label="Undo", command= my_text.edit_undo , accelerator = "Cntrl+z")


color_menu = Menu(my_menu)
my_menu.add_cascade(label="Colors", menu= color_menu)
color_menu.add_command(label="Change selected text color" , command = text_color)
color_menu.add_command(label="All text", command = all_text_color)
color_menu.add_command(label="background", command = bg_color )





text_scroll.config(command= my_text.yview)

root.bind('<Control-Key-x>', cut_text)
root.bind('<Control-Key-c>', copy_text)
root.bind('<Control-Key-v>', paste_text)

bold_button = Button(toolbar_frame, text="Bold", command = Bold_it)
bold_button.grid(row=0, column =0 , sticky=W)

italics_button = Button(toolbar_frame, text="Italics", command = italics_it)
italics_button.grid(row=0, column =1 )

color_text_button = Button(toolbar_frame, text= "Text Color", command = text_color)
color_text_button.grid(row=0 , column =2 )

root.mainloop()