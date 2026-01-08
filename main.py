from tkinter import *

BACKGROUND_COLOR = "#B1DDC6"

window = Tk()
window.title("Flashy")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

CARD_FRONT_IMG = PhotoImage(file="images/card_front.png")
CARD_BACK_IMG = PhotoImage(file="images/card_back.png")
RIGHT_IMAGE = PhotoImage(file="images/right.png")
WRONG_IMAGE = PhotoImage(file="images/wrong.png")

canvas = Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
canvas.create_image(400, 263, image=CARD_FRONT_IMG)
canvas.grid(column=0, row=0, columnspan=2)

canvas.create_text(400, 150, text="Deutsch", fill="black", font=("Arial", 40, "italic"))
canvas.create_text(400, 263, text="Wort", fill="black", font=("Arial", 60, "bold"))

wrong_button = Button(highlightthickness=0, image=WRONG_IMAGE)
wrong_button.grid(column=0, row=1)

right_button = Button(highlightthickness=0, image=RIGHT_IMAGE)
right_button.grid(column=1, row=1)

window.mainloop()