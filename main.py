from tkinter import *
import time
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
CHECKMARK = "✅"


# ---------------------------- TIMER RESET ------------------------------- #

# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_timer():
    count_down(5 * 60)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def count_down(count):
    count_minutes = math.floor(count / 60)
    count_secs = count % 60

    canvas.itemconfig(timer_text, text=f'{count_minutes}:{count_secs}')
    if count > 0:
        window.after(1000, count_down, count - 1)


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("POMODORO")
window.config(padx=100, pady=50, bg=YELLOW)
main_label = Label(text="Timer", font=("Roboto", 50, "bold"), bg=YELLOW, fg=GREEN)
main_label.grid(column=1, row=0)

canvas = Canvas(width=200, height=224, highlightthickness=0)
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato_img)
canvas.config(bg=YELLOW)
timer_text = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(row=1, column=1)

start_button = Button()
start_button.config(text="Start", fg="black", padx=10, pady=5, font=(FONT_NAME, 25, "bold"), command=start_timer)
start_button.grid(row=2, column=0)

check_label = Label(text=CHECKMARK)
check_label.grid(row=3, column=1)

end_button = Button()
end_button.config(text="Start", fg="black", padx=10, pady=5, font=(FONT_NAME, 25, "bold"))
end_button.grid(row=2, column=2)

window.mainloop()
