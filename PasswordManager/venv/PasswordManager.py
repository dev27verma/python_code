from tkinter import Tk, Button, PhotoImage, Canvas, Entry, Label, messagebox, END
from random import choice, randint, shuffle
import json
import pyperclip

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
           'w', 'x', 'y', 'z',
           'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V',
           'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']


# ---------------------------- Find Password ------------------------------------ #
def on_click_exit():
    exit()

def on_click_search():
    website = entry_website.get()
    try:
        with open("data.json", "r") as data_file:
            data = json.load(data_file)
    except FileNotFoundError:
        messagebox.showerror(title="Error", message="No data file found")
    else:
        if website in data:
            email = data[website]["email"]
            password = data[website]["password"]
            messagebox.showinfo(title=website, message=f"Email: {email}\nPassword: {password}")
            on_click_clear()
        else:
            messagebox.showerror(title=website, message=f"No details for {website} present")
            on_click_clear()


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def on_click_generate():
    password_letters = [choice(letters) for _ in range(randint(8, 10))]
    password_numbers = [choice(numbers) for _ in range(randint(2, 4))]
    password_symbols = [choice(symbols) for _ in range(randint(2, 4))]
    password_list = password_letters + password_numbers + password_symbols

    shuffle(password_list)
    final_password = "".join(password_list)
    entry_password.insert(0, final_password)


# ---------------------------- SAVE PASSWORD ------------------------------- #
def on_click_add():
    website = entry_website.get()
    email = entry_email.get()
    password = entry_password.get()
    new_data = {
        website: {
            "email": email,
            "password": password,
        }
    }
    if len(website) == 0 or len(email) == 0 or len(password) == 0:
        messagebox.showerror(title=website, message="Above Entries can't be left empty!!")
        on_click_clear()
    else:
        is_ok = messagebox.askokcancel(title=website,
                                       message=f"These are the below details entered:\nwebsite: {website}\nEmail: {email}\nIs is OK to save?")
        if is_ok:
            try:
                # Reading old data
                with open("data.json", "r") as data_file:
                    data = json.load(data_file)
            except FileNotFoundError:
                with open("data.json", "w") as data_file:
                    json.dump(new_data, data_file, indent=4)
            else:
                # updating old data with new data
                data.update(new_data)
                # saving updated data
                with open("data.json", "w") as data_file:
                    json.dump(data, data_file, indent=4)
            finally:
                on_click_clear()
        else:
            on_click_clear()


# to clear the field if we click on cancel/Ok on popup box
def on_click_clear():
    entry_website.delete(0, END)
    entry_password.delete(0, END)


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.minsize(width=600, height=600)
window.config(padx=80, pady=50, bg="white")

canvas = Canvas(width=200, height=200, bg="white", highlightthickness=0)
logo_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo_img)
canvas.grid(row=0, column=1)

label_website = Label(text="Website", bg="white", font=("courier", 16, "normal"), highlightthickness=0)
label_website.grid(row=1, column=0,pady=10)

label_email = Label(text="Email", bg="white", font=("courier", 16, "normal"), highlightthickness=0)
label_email.grid(row=2, column=0,pady=10)

label_password = Label(text="Password", bg="white", font=("courier", 16, "normal"), highlightthickness=0)
label_password.grid(row=3, column=0,pady=10)

entry_website = Entry(width=30)
entry_website.grid(row=1, column=1,pady=10)

entry_email = Entry(width=30)
entry_email.insert(0, "devmailbox27@gmail.com")
entry_email.grid(row=2, column=1,pady=10)

entry_password = Entry(width=30)
entry_password.grid(row=3, column=1,pady=10)

button_search = Button(text="Search", width=20, command=on_click_search)
button_search.grid(row=1, column=2)

button_password = Button(text="Generate", width=20, command=on_click_generate)
button_password.grid(row=3, column=2)

button_add = Button(text="Add", width=27, command=on_click_add)
button_add.grid(row=4, column=1)

button_clear = Button(text="Clear", width=20, command=on_click_clear)
button_clear.grid(row=4, column=0)

button_exit = Button(text="Exit", width=20, command=on_click_exit)
button_exit.grid(row=4, column=2)

window.mainloop()
