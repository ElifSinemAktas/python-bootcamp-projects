from tkinter import *
import pandas
import random

BACKGROUND_COLOR = "#B1DDC6"
TITLE_FONT = ("Arial", 40, "italic")
WORD_FONT = ("Arial", 60, "bold")

try:
    with open("is_not_learned.csv") as file:
        data = pandas.read_csv(file)
        print(len(data))
except FileNotFoundError:
    with open("./data/french_words.csv") as file:
        data = pandas.read_csv(file)
        to_learn = data.to_dict(orient="records")
else:
    to_learn = data.to_dict(orient="records")
finally:
    CURRENT_CARD = random.choice(to_learn)


# TODO 2. Create a function to change card image and word


def flip():
    global CURRENT_CARD
    canvas.itemconfig(title_text, text="English", fill="white")
    canvas.itemconfig(word_text, text=CURRENT_CARD["English"], fill="white")
    canvas.itemconfig(card_color, image=back_image)


def new_word():
    global CURRENT_CARD, TIMER
    CURRENT_CARD = random.choice(to_learn)
    window.after_cancel(TIMER)
    canvas.itemconfig(title_text, text="French", fill="black")
    canvas.itemconfig(word_text, text=CURRENT_CARD["French"], fill="black")
    canvas.itemconfig(card_color, image=front_image)
    TIMER = window.after(3000, flip)


def is_learned():
    new_word()
    to_learn.remove(CURRENT_CARD)
    print(len(to_learn))
    is_not_learn = pandas.DataFrame(to_learn)
    is_not_learn.to_csv("is_not_learned.csv")


# TODO 1. Create User Interface

window = Tk()
window.title("Flash Cards")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

canvas = Canvas()
back_image = PhotoImage(file="./images/card_back.png")
front_image = PhotoImage(file="./images/card_front.png")
canvas.config(width=800, height=530, highlightthickness=0, bg=BACKGROUND_COLOR)

# The image will be changed...
card_color = canvas.create_image(400, 265, image=front_image)

# The text will be changed..


title_text = canvas.create_text(400, 130, text="", font=TITLE_FONT)
word_text = canvas.create_text(400, 265, text="", font=WORD_FONT)

canvas.grid(column=0, row=0, columnspan=2)

right_image = PhotoImage(file="./images/right.png")
wrong_image = PhotoImage(file="./images/wrong.png")
right_button = Button(image=right_image, highlightthickness=0, command=is_learned)
wrong_button = Button(image=wrong_image, highlightthickness=0, command=new_word)
right_button.grid(column=1, row=1)
wrong_button.grid(column=0, row=1)

TIMER = window.after(3000, flip)
new_word()

window.mainloop()
