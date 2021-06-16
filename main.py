from tkinter import *
import math
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 0.1
SHORT_BREAK_MIN = 0.1
LONG_BREAK_MIN = 20
CHECK_MARK = "✔"
reps = 0
timer = None

# ---------------------------- TIMER RESET ------------------------------- # 


def reset_timer():
    global reps
    reps = 0
    window.after_cancel(timer)
    canvas.itemconfig(timer_text, text="00:00")
    label.config(text="Timer", fg=GREEN, bg=YELLOW, font=(FONT_NAME, 40))
    check_label.config(text="")


# ---------------------------- TIMER MECHANISM ------------------------------- # 


def start_timer():
    global reps
    reps += 1

    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60

    if reps % 8 == 0:
        count_down(long_break_sec)
        label.config(text="Break", fg=RED, bg=YELLOW, font=(FONT_NAME, 40))
    elif reps % 2 == 0:
        count_down(short_break_sec)
        label.config(text="Break", fg=PINK, bg=YELLOW, font=(FONT_NAME, 40))
    else:
        count_down(work_sec)
        label.config(text="Work", fg=GREEN, bg=YELLOW, font=(FONT_NAME, 40))

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 


def count_down(count):

    count_min = math.floor(count / 60)
    count_sec = count % 60

    if count_sec < 10:
        count_sec = f"0{count_sec}"

    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
    if count > 0:
        global timer
    # 1000 milisecond
        timer = window.after(1000, count_down, count - 1)
    else:
        start_timer()
        marks = ""
        work_sessions = math.floor(reps / 2)
        for _ in range(work_sessions):
            marks += CHECK_MARK
        check_label.config(text=marks)

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro")
# bg: change the background color
window.config(padx=100, pady=50, bg=YELLOW)

# Time Label
label = Label(text="Timer", fg=GREEN, bg=YELLOW, font=(FONT_NAME, 40))
label.grid(column=1, row=0)

# bg: background color of the picture
# highlightthickness = 0: get rid of the border between the background and picture
canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato_img)
timer_text = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(column=1, row=1)


# Start Button
start_button = Button(text="Start", highlightthickness=0, bg=YELLOW, command=start_timer)
start_button.grid(column=0, row=2)

# Reset Button
start_button = Button(text="Reset", highlightthickness=0, bg=YELLOW, command=reset_timer)
start_button.grid(column=2, row=2)

# Check Mark Label
check_label = Label(fg=GREEN, bg=YELLOW)
check_label.grid(column=1, row=3)

window.mainloop()
