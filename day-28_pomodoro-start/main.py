import tkinter
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
marks = "✔"
timer = None

# ---------------------------- TIMER RESET ------------------------------- #

def reset_timer():
    window.after_cancel(timer)
    main_label.config(text="Timer")
    canvas.itemconfig(timer_text, text="00:00")
    checkmarks.config(text="")
    global reps
    reps=0

# ---------------------------- TIMER MECHANISM ------------------------------- #

def start_timer():
    global reps
    reps += 1
    long_sec = LONG_BREAK_MIN * 60
    short_sec = SHORT_BREAK_MIN * 60
    work_sec = WORK_MIN * 60
    if reps % 8 == 0:
        count_down(long_sec)
        main_label.config(text="Break", fg=RED)
    elif reps % 2 == 0:
        count_down(short_sec)
        main_label.config(text="Break", fg=PINK)
    else:
        count_down(work_sec)
        main_label.config(text="Work", fg=GREEN)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #

def count_down(count):
    count_min = math.floor(count / 60)
    count_sec = count % 60

    if count_sec < 10:
        count_sec = f"0{count_sec}"
    if count_min < 10:
        count_min = f"0{count_min}"

    if count > 0:
        global timer
        canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
        timer = window.after(2, count_down, count - 1)
    else:
        start_timer()
        if reps % 2 == 0:
            global marks
            checkmarks.config(text=marks)
            marks += "✔"

# ---------------------------- UI SETUP ------------------------------- #

window = tkinter.Tk()
window.title("Pomodoro")
window.config(padx=100, pady=100, bg=YELLOW)

canvas = tkinter.Canvas()
image = tkinter.PhotoImage(file="tomato.png")
canvas.config(width=200, height=224, bg=YELLOW, highlightthickness=0)
canvas.create_image(100, 112, image=image)
timer_text = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 28, "bold"))
canvas.grid(column=1, row=1)

main_label = tkinter.Label()
main_label.config(text="Timer", bg=YELLOW, fg=GREEN, font=(FONT_NAME, 25, "bold"))
main_label.grid(column=1, row=0)

button_start = tkinter.Button(text="Start", bg=GREEN, highlightthickness=0, command=start_timer)
button_start.grid(column=0, row=2)

button_reset = tkinter.Button(text="Reset", bg=GREEN, highlightthickness=0, command=reset_timer)
button_reset.grid(column=2, row=2)

checkmarks = tkinter.Label(bg=YELLOW, fg=GREEN, font=(FONT_NAME, 15, "bold"))
checkmarks.grid(column=1, row=3)

window.mainloop()
