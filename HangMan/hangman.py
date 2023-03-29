import random
from word_list import word_list
from logo import logo
from lives import stages

print(logo)
# lives given before you lose game
lives = 6
# chose a random word from word_list file
chosen_word = random.choice(word_list)
display = []
for i in range(len(chosen_word)):
    display += '_'
print(display)
end_of_game = False
while not end_of_game:
    # user enter a character to guess the word selected by random
    guess = input("Enter a character ").lower()
    # logic to check if the enter char is matched with the letter of word or not
    for position in range(len(chosen_word)):
        letter = chosen_word[position]
        if letter == guess:
            # insert letter in display list
            display[position] = letter
    if guess not in chosen_word:
        lives -= 1
        print(stages[lives])
        print(f"Lives left {lives}")
        if lives == 0:
            end_of_game = True
            print(f"You lost, correct word was {chosen_word}")
            exit()
    # convert list to string
    print(f"{' '.join(display)}")
    # check if anymore _ is left or not, if not end the game
    if "_" not in display:
        end_of_game = True
        print("You win")
        exit()
