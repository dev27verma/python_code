import random
from tkinter import Tk, Canvas, Button, PhotoImage
from random import randint, choice
import pandas

current_card = {}
to_learn = {}
BACKGROUND_COLOR = "#B1DDC6"
FONT = ("Ariel", 40, "italic")

try:
    data = pandas.read_csv("words_to_learn.csv")
except FileNotFoundError:
    original_data = pandas.read_csv("french_words.csv")
    to_learn = original_data.to_dict(orient="records")
else:
    to_learn = data.to_dict(orient="records")

# if we print the above line print(to_learn) without orient 0/p first all english word then french word dict{english: dev } {english: word}....... {french: dev } {french: dev}
# if we use orient="record" it will give O/P dict{english: dev, french: dev} in the order

def next_card():
    global current_card, flip_timer
    window.after_cancel(flip_timer)
    current_card = random.choice(to_learn)
    canvas.itemconfig(card_title, text="French", fill="black")
    canvas.itemconfig(card_word, text=current_card["French"], fill="black")
    canvas.itemconfig(card_background, image=image_card_front)
    flip_timer = window.after(3000, func=flip_card)


def flip_card():
    canvas.itemconfig(card_title, text="English", fill="white")
    canvas.itemconfig(card_word, text=current_card["English"], fill="white")
    canvas.itemconfig(card_background, image=image_card_back)


def is_known():
    to_learn.remove(current_card)
    data = pandas.DataFrame(to_learn)
    data.to_csv("words_to_learn.csv", index=False)
    next_card()


# ----------------------------------Design--------------------------------------------#
window = Tk()
window.title("Flash Card")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

flip_timer = window.after(3000, func=flip_card)

canvas = Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
image_card_front = PhotoImage(file="card_front.png")
image_card_back = PhotoImage(file="card_back.png")
card_background = canvas.create_image(400, 263, image=image_card_front)

card_title = canvas.create_text(400, 150, text=" ", font=FONT)
card_word = canvas.create_text(400, 263, text=" ", font=FONT)
canvas.grid(column=0, row=0, columnspan=2)

cross_image = PhotoImage(file="wrong.png")
unknown_button = Button(image=cross_image, bg=BACKGROUND_COLOR, highlightthickness=0, command=next_card)
unknown_button.grid(column=0, row=1)

right_image = PhotoImage(file="right.png")
right_button = Button(image=right_image, bg=BACKGROUND_COLOR, highlightthickness=0, command=is_known)
right_button.grid(column=1, row=1)

# we are using next_card so that while we run, it shows the first random french word and title as French instead of  Title and Word,
# also we removed text=Title and text=Word from above create text canvas, as it is no more required
next_card()
window.mainloop()
