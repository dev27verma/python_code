from tkinter import Tk, PhotoImage, Canvas, Button

BACKGROUND_COLOR = "#B1DDC6"
FONT = ("Ariel", 40, "italic")

def on_hit_cross_button():
    pass
def on_hit_right_button():
    pass

window = Tk()
window.title("Flash Card")
window.config(padx=50, pady=50,bg=BACKGROUND_COLOR)

flip_timer = window.after(3000, func=flip_card)

canvas = Canvas(width=800,height=526,bg=BACKGROUND_COLOR, highlightthickness=0)
card_front_img = PhotoImage(file="card_front.png")
card_back_img = PhotoImage(file="card_back.png")
canvas.create_image(400,263,image=card_front_img)
canvas.create_text(400,150, text=" ", font=FONT)
canvas.create_text(400,263, text=" ", font=FONT)
canvas.grid(row=0, column=0, columnspan=2)

wrong_img = PhotoImage(file="wrong.png")
cross_button = Button(image=wrong_img, bg=BACKGROUND_COLOR, highlightthickness=0,command=on_hit_cross_button)
cross_button.grid(row=2,column=0)

right_img = PhotoImage(file="right.png")
right_button = Button(image=right_img, bg=BACKGROUND_COLOR, highlightthickness=0,command=on_hit_right_button)
right_button.grid(row=2,column=1)

window.mainloop()