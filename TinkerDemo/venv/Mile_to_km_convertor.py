from tkinter import *

window = Tk()
window.config(padx=20, pady=20,bg="white")
window.title("Mile to Km Converter")

entry = Entry(width=7)
entry.grid(column=1, row=0)

my_label1 = Label(text="Miles",bg="white")
my_label1.grid(column=2, row=0)

my_label2 = Label(text="is equal to",bg="white")
my_label2.grid(column=0, row=1)

my_label3 = Label(text="0",bg="white")
my_label3.grid(column=1, row=1)
my_label4 = Label(text="Km",bg="white")
my_label4.grid(column=2, row=1)


def button_clicked():
    num = float(entry.get())
    result = round((num * 1.609344), 2)
    my_label3.config(text=f"{result}")


new_button = Button(text="calculate", command=button_clicked)
new_button.grid(column=1, row=2)

window.mainloop()
