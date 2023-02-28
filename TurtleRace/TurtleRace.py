from turtle import Turtle,Screen
import random

screen = Screen()
screen.setup(width=1000,height=800)
colour = ["red","green","blue","black","purple","yellow"]
position = [-70,-40,-10,20,50,80]
all_turtle = []

input_bet = screen.textinput(title="Please Bet", prompt="Please choose a colour: ")

for t in range(0,6):
    new_turtles = Turtle(shape="turtle")
    new_turtles.color(colour[t])
    new_turtles.penup()
    new_turtles.goto(-480,position[t])
    all_turtle.append(new_turtles)

if input_bet:
    is_race_on = True

while is_race_on:
    for t in all_turtle:
        if t.xcor() > 460:
            is_race_on = False
            winning_colour = t.pencolor()
            if winning_colour == input_bet:
                print(f"You won!! {winning_colour} is the winner")
            else:
                print(f"You lost!! {winning_colour} is the winner")

        run = random.randint(0,10)
        t.forward(run)

screen.exitonclick()