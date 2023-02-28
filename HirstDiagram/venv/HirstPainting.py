import colorgram
import turtle as turtle_module
import random


tim = turtle_module.Turtle()
screen = turtle_module.Screen()

tim.speed("fastest")
tim.penup()
tim.hideturtle()
turtle_module.colormode(255)

rgb_colour = []
colours = colorgram.extract("img.png",35)

for color in colours:
    r = color.rgb.r
    g = color.rgb.g
    b = color.rgb.b
    new_colour = (r,g,b)
    rgb_colour.append(new_colour)

tim.setposition(-250,-250)
number_of_dots = 100

for dot_count in range(1, number_of_dots + 1):
    tim.dot(20, random.choice(rgb_colour))
    tim.forward(50)

    if dot_count % 10 == 0:
        tim.setheading(90)
        tim.forward(50)
        tim.setheading(180)
        tim.forward(500)
        tim.setheading(0)


screen.exitonclick()