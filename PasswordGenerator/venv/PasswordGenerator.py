import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
           'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Password Generator")
character = int(input("Number of character to add in password: "))
num = int(input("Enter numbers to add: "))
symbol = int(input("Enter number of symbols to add: "))

password =""

password_list = []

for a in range(character):
    password_list += random.choice(letters)

for a in range(num):
    password_list += random.choice(numbers)

for a in range(symbol):
    password_list += random.choice(symbols)

print(password_list)

random.shuffle(password_list)

print(password_list)

for char in password_list:
    password += char

print(password)