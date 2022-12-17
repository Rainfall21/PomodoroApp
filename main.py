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
my_timer = None
# ---------------------------- TIMER RESET ------------------------------- #


def reset():
    window.after_cancel(my_timer)
    check_marks.config(text="")
    canvas.itemconfig(timer_text, text="00:00")
    timer.config(text="Timer", foreground=GREEN)


# ---------------------------- TIMER MECHANISM ------------------------------- #
def start():

    global reps
    reps += 1

    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60

    if reps % 8 == 0:
        timer.config(text="Long break", foreground=RED)
        count_down(long_break_sec)
    elif reps % 2 == 0:
        timer.config(text="Short break", foreground=PINK)
        count_down(short_break_sec)
    else:
        count_down(work_sec)
        timer.config(text="Work", foreground=GREEN)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def count_down(count):

    count_min = math.floor(count / 60)
    count_sec = count % 60

    if count_sec < 10:
        count_sec = f"0{count_sec}"
    if count_min < 10:
        count_min = f"0{count_min}"
    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
    if count > 0:
        global my_timer
        my_timer = window.after(1000, count_down, count - 1)
    else:
        start()
        mark = ""
        for _ in range(math.floor(reps / 2)):
            mark += "✔"
        check_marks.config(text=mark)


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, background=YELLOW)

window.after(1000,)

canvas = Canvas(width=200, height=224, background=YELLOW, highlightthickness=0)
tomato_image = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato_image)
timer_text = canvas.create_text(100,130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(row=1,column=1)

start_button = Button(command=start, text="Start", highlightbackground=YELLOW)
start_button.grid(column=0,row=2)

reset_button = Button(command=reset, text="Reset", highlightbackground=YELLOW)
reset_button.grid(column=2,row=2)

timer = Label(text="Timer", font=(FONT_NAME, 35, "bold"), background=YELLOW, foreground=GREEN)
timer.grid(row=0,column=1)

check_marks = Label(background= YELLOW, foreground=GREEN)
check_marks.grid(row=2, column=1)


window.mainloop()











