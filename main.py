import random
from pandas import read_csv
from tkinter import *

words_csv = read_csv("data/german_portuguese_words.csv")
words_dict = words_csv.to_dict(orient="records")

def get_random_word_dict():
    return words_dict[random.randint(0, len(words_dict) - 1)]

def change_word():
    global flip_timer
    window.after_cancel(flip_timer)

    word_dict = get_random_word_dict()

    canvas.itemconfig(card, image=CARD_FRONT_IMG)
    canvas.itemconfig(language, text="German", fill="black")
    canvas.itemconfig(word, text=word_dict["German"], fill="black")

    flip_timer = window.after(3000, flip_card, word_dict)

def flip_card(word_dict: dict):
    canvas.itemconfig(card, image=CARD_BACK_IMG)
    canvas.itemconfig(language, text="Portuguese", fill="white")
    canvas.itemconfig(word, text=word_dict["Portuguese"], fill="white")

# UI config
BACKGROUND_COLOR = "#B1DDC6"

window = Tk()
window.title("Flashy")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

flip_timer = window.after(3000, flip_card, get_random_word_dict())

CARD_FRONT_IMG = PhotoImage(file="images/card_front.png")
CARD_BACK_IMG = PhotoImage(file="images/card_back.png")
RIGHT_IMAGE = PhotoImage(file="images/right.png")
WRONG_IMAGE = PhotoImage(file="images/wrong.png")

canvas = Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
card = canvas.create_image(400, 263, image=CARD_FRONT_IMG)
canvas.grid(column=0, row=0, columnspan=2)

language = canvas.create_text(400, 150, fill="black", font=("Arial", 40, "italic"))
word = canvas.create_text(400, 263, fill="black", font=("Arial", 60, "bold"))

wrong_button = Button(highlightthickness=0, image=WRONG_IMAGE, command=change_word)
wrong_button.grid(column=0, row=1)

right_button = Button(highlightthickness=0, image=RIGHT_IMAGE, command=change_word)
right_button.grid(column=1, row=1)

change_word()

window.mainloop()