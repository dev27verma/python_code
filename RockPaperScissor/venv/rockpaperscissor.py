import random
from art import rock, paper, scissor

options = [rock, paper, scissor]
user_input = int(input("Enter 0.Rock, 1.Paper, 2.Scissor: "))
if user_input > 2 or user_input < 0:
    print("Invalid Input, User lost")
else:
    print(f"user input: ")
    print(options[user_input])
    comp_input = random.randint(0, 2)
    print(f"computer choice ")
    print(options[comp_input])
    if user_input == 0:
        if comp_input == 1:
            print("Computer won")
        elif comp_input == 0:
            print("Draw")
        else:
            print("You won")
    elif user_input == 1:
        if comp_input == 1:
            print("Draw")
        elif comp_input == 0:
            print("User won")
        else:
            print("Computer won")
    elif user_input == 2:
        if comp_input == 0:
            print("Computer won")
        elif comp_input == 1:
            print("User won")
        else:
            print("Draw")
