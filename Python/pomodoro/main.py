from tkinter import *

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
TICK = "✔"
rep = 0
timer=None


# ---------------------------- TIMER RESET ------------------------------- #
def reset_timer():
    global rep
    window.after_cancel(timer)
    title_label.config(text="Timer",fg=GREEN)
    canvas.itemconfig(timer_text,text="00:00")
    check.config(text="")
    rep=0

# ---------------------------- TIMER MECHANISM ------------------------------- #
def start_timer():
    global rep
    rep += 1
    if rep % 8 == 0:
        count_down(LONG_BREAK_MIN * 60)
        title_label.config(text="Break",fg=RED)

    elif rep % 2 == 0:
        count_down(SHORT_BREAK_MIN * 60)
        title_label.config(text="Break",fg=RED)


    else:
        count_down(WORK_MIN * 60)
        title_label.config(text="Timer",fg=GREEN)



# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def count_down(count):
    minute = int(count / 60)
    seconds = count % 60
    if seconds < 10:
        seconds = "0" + str(seconds)
    canvas.itemconfig(timer_text, text=f"{minute}:{seconds}")
    if count > 0:
        global timer
        timer=window.after(1000, count_down, count - 1)
    else:
        if rep%2!=0:
            check.config(text=TICK+check.cget("text"))
        start_timer()



# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg='#f7f5dd')

title_label = Label(text="Timer", fg=GREEN, font=(FONT_NAME, 50), bg='#f7f5dd')
title_label.grid(row=0, column=1)

canvas = Canvas(width=200, height=224, bg="#f7f5dd")
photo = PhotoImage(file="tomato.png")
canvas.create_image(103, 112, image=photo)
timer_text = canvas.create_text(103, 130, text="00.00", fill="white", font=(FONT_NAME, 25, 'bold'))
canvas.grid(row=1, column=1)

start = Button(text="Start", highlightthickness=0, command=start_timer)
start.grid(row=2, column=0)

reset = Button(text="Reset", highlightthickness=0,command=reset_timer)
reset.grid(row=2, column=2)

check = Label(fg=GREEN, bg='#f7f5dd')
check.grid(row=3, column=1)

window.mainloop()
