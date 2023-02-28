from turtle import Turtle


class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.color("green")
        self.shape("turtle")
        self.penup()
        self.setheading(90)
        self.reset()

    def up(self):
        self.forward(20)

    def reset(self):
        self.goto(0, -280)
