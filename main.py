from tkinter import *
import math
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
timer = None

# ---------------------------- TIMER RESET ------------------------------- #
def reset_timer():
    global reps
    reps = 0
    window.after_cancel(timer)
    canvas.itemconfig(timer_text, text ="00:00")
    title_label.config(text = "Timer")


# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_timer():
    global reps
    reps += 1
    work_sec = WORK_MIN*60
    short_break_sec = SHORT_BREAK_MIN*60
    long_break_sec = LONG_BREAK_MIN*60

    if reps % 8 == 0:
        count_down(long_break_sec)
        title_label.config(text = "Break", fg =RED)
    elif reps % 2 ==0:
         count_down(short_break_sec)
         title_label.config(text="Break", fg=PINK)
    else:
         count_down(work_sec)
    title_label.config(text="Work", fg=GREEN)

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def count_down(count):

    count_min = math.floor(count/60)
    count_sec = count % 60
    if count_sec < 10:
        count_sec = f"0{count_sec}"
    canvas.itemconfig(timer_text,text = f"{count_min}:{count_sec}")
    if count > 0:
        global timer
        timer =window.after(1000,count_down,count-1)
    else:
        start_timer()



# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro")
window.config(padx = 100, pady = 50, bg= YELLOW)

title_label = Label(text ="Timer", fg = GREEN, font =(FONT_NAME, 30, "bold"))
title_label.grid(column = 1, row = 0)


canvas = Canvas(width = 200, height = 224, bg = YELLOW, highlightthickness = 0)
tomoto_image = PhotoImage(file = "tomato.png")
canvas.create_image(100,112,image = tomoto_image)
timer_text = canvas.create_text(100,130,text ="00:00", fill = "white", font = (FONT_NAME,28,"bold"))
canvas.grid(column = 1, row = 1)

start_button = Button(text = "Start", highlightthickness = 0, command = start_timer)
start_button.grid(column = 0, row = 3)

reset_button = Button(text = "Rest", highlightthickness = 0, command = reset_timer)
reset_button.grid(column = 3, row = 3)

check_mark = Label(text ="V", fg = GREEN, bg = YELLOW)
check_mark.grid(column = 1, row = 4)


window.mainloop()