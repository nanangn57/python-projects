from tkinter import *
import pandas as pd
import random

BACKGROUND_COLOR = "#B1DDC6"

# ---- Function -----
try:
    list_word = pd.read_csv('data/to_learn.csv')
except FileNotFoundError:
    list_word = pd.read_csv('data/japanese_words.csv')

list_word = list_word.to_dict(orient="records")
random_word = random.choice(list_word)


def correct_word():
    list_word.remove(random_word)
    pd.DataFrame(list_word).to_csv("data/to_learn.csv", index=False)
    gen_word()


def gen_word():
    global random_word, flip_timer
    window.after_cancel(flip_timer)
    random_word = random.choice(list_word)
    ja_word = random_word['word']
    canvas.itemconfig(language_text, text="Japanese", fill="#808D7C")
    canvas.itemconfig(card_img, image=front_card_img)
    canvas.itemconfig(word_text, text=ja_word, fill="black")
    flip_timer = window.after(5000, flip_card_en)


def flip_card_en():
    en_word = random_word['meaning']
    canvas.itemconfig(card_img, image=card_back_img)
    canvas.itemconfig(word_text, text=en_word, fill="white",
                      font=("Ariel", 30, "bold"))
    canvas.itemconfig(language_text, text="English", fill="white")


# ---- UI set up ----
window = Tk()
window.title("Flash Card")
window.config(padx=50, pady=50, background=BACKGROUND_COLOR)

flip_timer = window.after(5000, flip_card_en)

# Canvas
canvas = Canvas(width=800, height=526, highlightthickness=0, background=BACKGROUND_COLOR)
front_card_img = PhotoImage(file='images/card_front.png')
card_back_img = PhotoImage(file='images/card_back.png')
card_img = canvas.create_image(400, 263, image=front_card_img)
canvas.grid(row=1, column=1, columnspan=2)

language_text = canvas.create_text(400, 100, text="Japanese", font=("Ariel", 30, "italic"), fill="#808D7C")
word_text = canvas.create_text(400, 270, text="", font=("Ariel", 50, "bold"), width=500)
gen_word()


# Button
wrong_img = PhotoImage(file='images/wrong.png')
wrong_button = Button(image=wrong_img, command=gen_word)
wrong_button.config(borderwidth=0, background=BACKGROUND_COLOR)
wrong_button.grid(row=2, column=1, padx=20, pady=20)

right_img = PhotoImage(file='images/right.png')
right_button = Button(image=right_img, command=correct_word)
right_button.config(borderwidth=0, background=BACKGROUND_COLOR)
right_button.grid(row=2, column=2, padx=20, pady=20)

window.mainloop()
