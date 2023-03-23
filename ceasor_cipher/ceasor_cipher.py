from art import logo

print(logo)
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
            'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p',
            'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']


def encrypt(start_text, shift_amount):
    end_text = ""
    for char in start_text:
        if char in alphabet:
            position = alphabet.index(char)
            new_position = position + shift_amount
            end_text += alphabet[new_position]
        else:
            end_text += char
    print(f"Here's the encode result: {end_text}")


def decrypt(start_text, shift_amount):
    end_text = ""
    for char in start_text:
        if char in alphabet:
            position = alphabet.index(char)
            new_position = position - shift_amount
            end_text += alphabet[new_position]
        else:
            end_text += char
    print(f"Here's the encode result: {end_text}")


should_end = False
while not should_end:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    if direction == 'encode':
        text = input("Type your message:\n").lower()
        shift = int(input("Type the shift number:\n"))
        shift = shift % 26
        encrypt(text, shift)
    elif direction == "decode":
        text = input("Type your message:\n").lower()
        shift = int(input("Type the shift number:\n"))
        shift = shift % 26
        decrypt(text, shift)
    else:
        print("Invalid entry! Exiting the program.")
        exit()
    restart = input("Type 'yes' if you want to go again. Otherwise type 'no': \n")
    if restart == "no":
        should_end = True
        print("Goodbye")
