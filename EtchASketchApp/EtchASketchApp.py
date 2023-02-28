from turtle import Turtle, Screen


screen = Screen()
tim = Turtle()

def move_forward():
    tim.forward(100)

def move_backward():
    tim.forward(-100)

def turn_left():
    current_heading = tim.heading() - 90
    tim.setheading(current_heading)

def turn_right():
    current_heading = tim.heading() + 90
    tim.setheading(current_heading)

def clear():
    tim.clear()
    tim.penup()
    tim.home()

screen.listen()

screen.onkey(move_forward,"w")
screen.onkey(move_backward, "s")
screen.onkey(turn_left,"a")
screen.onkey(turn_right,"d")
screen.onkey(clear,"c")

screen.exitonclick()