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
reps = 0
timer = None


# ---------------------------- TIMER RESET ------------------------------- #
def reset_time():
    global reps
    reps = 0
    window.after_cancel(timer)
    timer_label.config(text="Timer", fg=GREEN, font=(FONT_NAME, 35))
    canvas.itemconfig(timer_text, text="00:00")
    check_label.config(text="")


# ---------------------------- TIMER MECHANISM ------------------------------- #
def start_timer():
    global reps
    reps += 1

    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60

    if reps % 2 == 1:
        count_down(work_sec)
        timer_label.config(text="Work", fg=GREEN)
    elif reps % 8 == 0:
        count_down(long_break_sec)
        timer_label.config(text="Break", fg=RED)
    else:
        count_down(short_break_sec)
        timer_label.config(text="Break", fg=PINK)
        check_count = reps // 2 * "☑"
        check_label.config(text=check_count)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def count_down(count_timer):
    count_min = count_timer // 60
    count_second = count_timer % 60

    canvas.itemconfig(timer_text, text=f"{count_min:02d}:{count_second:02d}")
    global timer
    if count_timer > 0:
        timer = window.after(1000, count_down, count_timer - 1)
    elif count_timer == 0:
        start_timer()


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)

canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_png = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato_png)
timer_text = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(row=2, column=2)

timer_label = Label(text="Timer", font=(FONT_NAME, 35), fg=GREEN, background=YELLOW)
timer_label.grid(row=1, column=2)

check_label = Label(text="", font=(FONT_NAME, 15), fg=GREEN, background=YELLOW)
check_label.grid(row=4, column=2)

start_button = Button(text="start", command=start_timer)
start_button.grid(row=3, column=1)

reset_button = Button(text="Reset", command=reset_time)
reset_button.grid(row=3, column=3)

window.mainloop()
