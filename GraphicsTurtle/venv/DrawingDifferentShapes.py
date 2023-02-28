import random
from turtle import Turtle, Screen

tim = Turtle()
screen = Screen()

colour = ["red","green", "yellow", "blue"]

def draw_shapes(num_sides):
    angle = 360 / num_sides
    for s in range(num_sides):
        tim.forward(100)
        tim.right(angle)

for num_sides in range(3,11):
    tim.color(random.choice(colour))
    draw_shapes(num_sides)


screen.exitonclick()