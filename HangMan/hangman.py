import random
from word_list import word_list
from logo import logo
from lives import stages

print(logo)

chosen_word = random.choice(word_list)  # chose a random word from above list
lives = 6                # lives given before you lose game

display = []
for i in range(len(chosen_word)):
    display += '_'
print(display)

end_of_game = False
while not end_of_game:
    guess = input("Enter a character ").lower()  # user enter a characted to guess the word selected by random

    for position in range(len(chosen_word)):# logic to check if the enter char is matched with the letter of word or not
        letter = chosen_word[position]
        if letter == guess:
            display[position] = letter     #insert letter in display list
    if guess not in chosen_word:
        lives -=1
        print(stages[lives])
        print(f"Lives left {lives}")
        if lives == 0:
            end_of_game = True
            print(f"You lost, correct word was {chosen_word}")
            exit()
    print(f"{' '.join(display)}")             #convert list to string
    if "_" not in display:                    #check if any more _ is left or not, if not end the game
        end_of_game = True
        print("You win")
        exit()