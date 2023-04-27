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
cancel = None

# ---------------------------- TIMER RESET ------------------------------- # 


def reset_timer():
    window.after_cancel(cancel)
    canvas.itemconfig(timer_text, text="00:00")
    my_label.config(text="Timer")
    checkmark.config(text="")
    global reps
    reps = 0


# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_timer():
    global reps
    reps += 1

    work_sec = WORK_MIN * 60
    short_break = SHORT_BREAK_MIN * 60
    long_break = LONG_BREAK_MIN

    if reps % 8 == 0:
        countdown(long_break)
        my_label.config(text="Long Break", fg=RED)
    elif reps % 2 == 0:
        countdown(short_break)
        my_label.config(text="Short Break", fg=PINK)
    else:
        countdown(work_sec)
        my_label.config(text="Work", fg=GREEN)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #

def countdown(count):

    count_min = math.floor(count / 60)
    count_sec = count % 60

    if count_sec < 10:
        count_sec = f"0{count_sec}"

    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
    if count > 0:
        global cancel
        cancel = window.after(1000, countdown, count -1)
    else:
        start_timer()
        marks = ""

        for _ in range(math.floor(reps / 2)):
            marks += f"{mark}"
        checkmark.config(text=marks)


# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Pomodoro Tehnique")
window.config(padx=130, pady=80, bg=YELLOW)

fg = GREEN
mark = "✔"

my_label = Label(text="Timer", fg=GREEN, bg=YELLOW, highlightthickness=0, font=(FONT_NAME, 40, "bold"))
my_label.grid(column=2, row=1)

start_button = Button(text= "Start", highlightthickness=0, font=("Montserrat", 10, "bold"), command=start_timer)
start_button.grid(column=1, row=3)

stop_button = Button(text="Reset", highlightthickness=0, font=("Montserrat", 10, "bold"), command=reset_timer)
stop_button.grid(column=3, row=3)

checkmark = Label(fg=GREEN, bg=YELLOW, highlightthickness=0)
checkmark.grid(column=2, row=4)


canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato)
timer_text = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 30, "bold"))
canvas.grid(column=2, row=2)


window.mainloop()















