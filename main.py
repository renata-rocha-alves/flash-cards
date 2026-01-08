import random
from pandas import read_csv, DataFrame
from tkinter import *

try:
    with open("data/words_to_learn.csv", "r") as file:
        words_list_csv = read_csv(file)
except FileNotFoundError:
    words_list_csv = read_csv("data/german_portuguese_words.csv")
finally:
    words_to_learn = words_list_csv.to_dict(orient="records")

current_word = {}

def change_word():
    global flip_timer, current_word
    window.after_cancel(flip_timer)

    current_word = random.choice(words_to_learn)

    canvas.itemconfig(card, image=CARD_FRONT_IMG)
    canvas.itemconfig(language, text="German", fill="black")
    canvas.itemconfig(word, text=current_word["German"], fill="black")

    flip_timer = window.after(3000, flip_card)

def flip_card():
    global current_word

    canvas.itemconfig(card, image=CARD_BACK_IMG)
    canvas.itemconfig(language, text="Portuguese", fill="white")
    canvas.itemconfig(word, text=current_word["Portuguese"], fill="white")

def update_words_to_learn():
    global words_to_learn

    data = DataFrame(words_to_learn)
    data.to_csv("data/words_to_learn.csv", index=False)

def right_guess():
    global current_word

    words_to_learn.remove(current_word)
    update_words_to_learn()

    change_word()

# UI config
BACKGROUND_COLOR = "#B1DDC6"

window = Tk()
window.title("Flashy")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

flip_timer = window.after(3000, flip_card)

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

right_button = Button(highlightthickness=0, image=RIGHT_IMAGE, command=right_guess)
right_button.grid(column=1, row=1)

change_word()

window.mainloop()