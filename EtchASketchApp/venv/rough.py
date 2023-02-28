from turtle import Turtle,Screen

tim = Turtle()
screen = Screen()

def move_forward():
    tim.forward(200)

def move_backward():
    tim.forward(-200)

def turn_left():
    current_position = tim.heading() - 30
    tim.setheading(current_position)

def turn_right():
    current_position = tim.heading() + 30
    tim.setheading(current_position)

def clear():
    tim.clear()
    tim.penup()
    tim.home()
    tim.pendown()

screen.listen()
screen.onkey(move_forward, "w")
screen.onkey(move_backward,"s")
screen.onkey(turn_left, "a")
screen.onkey(turn_right,"d")
screen.onkey(clear,"c")

screen.exitonclick()