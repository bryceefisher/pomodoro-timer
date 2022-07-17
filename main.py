from tkinter import *
import math

# ---------------------------- GLOBAL VAR ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 1
SHORT_BREAK_MIN = 1
LONG_BREAK_MIN = 1
reps = 0
timer = None


# ---------------------------- TIMER RESET ------------------------------- #

def reset_timer():
    global timer_text
    global reps
    reps = 0
    window.after_cancel(timer)
    timer_label.config(text="Timer")
    canvas.itemconfig(timer_text, text="00:00")
    check_label.config(text="")


# ---------------------------- TIMER MECHANISM ------------------------------- #


def start_timer():
    global timer_label
    global reps
    reps += 1
    work_sec = WORK_MIN * 60
    short_break_secs = SHORT_BREAK_MIN * 60
    long_break_secs = SHORT_BREAK_MIN * 60
    print(reps % 2)
    if reps % 8 == 0:
        count_down(long_break_secs)
        timer_label.config(text="Break", fg="RED")
    elif reps % 2 == 0:
        count_down(short_break_secs)
        timer_label.config(text="Break", fg="PINK")
    else:
        count_down(work_sec)
        timer_label.config(text="Work", fg="GREEN")


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #

def count_down(count):
    global timer
    global reps
    count_min = math.floor(count / 60)
    count_sec = count % 60
    if count_min < 10:
        for min in range(0, 10):
            if count_min == min:
                count_min = f"0{min}"
    for num in range(0, 10):
        if count_sec == num:
            count_sec = f"0{num}"
    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
    if count > 0:
        timer = window.after(1000, count_down, count - 1)
    else:
        start_timer()
        check = ""
        work_sessions = math.floor(reps / 2)
        for _ in range(work_sessions):
            check += "✔"
        check_label.config(text=check)


# ---------------------------- UI SETUP ------------------------------- #
# Setup Window

window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)

# Setup Canvas

canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato_img, )
timer_text = canvas.create_text(100, 130, text="25:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(column=1, row=1)

# Timer Label

timer_label = Label(text="Timer", font=(FONT_NAME, 45, "normal"), bg=YELLOW, fg="GREEN")
timer_label.grid(column=1, row=0)

# Start Button

start_button = Button(text="Start", highlightbackground=YELLOW, command=start_timer)
start_button.grid(column=0, row=2)

# Checkmark Label
check_label = Label(text="", font=(FONT_NAME, 20, "normal"), bg=YELLOW, fg="GREEN")
check_label.grid(column=1, row=3)

# Reset Button

reset_button = Button(text="Reset", highlightbackground=YELLOW, command=reset_timer)
reset_button.grid(column=2, row=2)

window.mainloop()
