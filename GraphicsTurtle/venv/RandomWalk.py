import random
import turtle
from turtle import Turtle, Screen

tim = Turtle()
screen = Screen()

turtle.colormode(255)

def random_colour():
    r = random.randint(0,255)
    g = random.randint(0,255)
    b = random.randint(0,255)
    colour = (r,g,b)
    return colour

tim.speed("fastest")
tim.pensize(15)

for direction in range(500):
    angle = random.randint(0, 360)
    tim.color(random_colour())
    tim.forward(20)
    tim.setheading(angle)


screen.exitonclick()
