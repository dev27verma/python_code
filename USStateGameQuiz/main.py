from turtle import Turtle, Screen
import pandas

screen = Screen()
screen.title("US State Quiz")
image = "blank_states_img.gif"
screen.addshape(image)

quiz = Turtle()
quiz.shape(image)

data = pandas.read_csv("50_states.csv")
all_states = data.state.to_list()

guessed_states = []

while len(guessed_states) < 50:
    user_guess = screen.textinput(title="My game", prompt="Guess the state name").title()
    if user_guess == "Exit":
        missing_state = [state for state in all_states if state not in guessed_states]
        state_file = pandas.DataFrame(missing_state)
        state_file.to_csv("state_to_learn.csv")
        break
    if user_guess in all_states:
        guessed_states.append(user_guess)
        new_state = Turtle()
        new_state.hideturtle()
        new_state.penup()
        state_data = data[data.state == user_guess]
        new_state.goto(int(state_data.x), int(state_data.y))
        new_state.write(user_guess)
