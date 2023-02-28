from turtle import Turtle

ALIGN = "center"
FONT = ("Aerial", 24, "normal")


class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.level = 0
        self.color("black")
        self.hideturtle()
        self.penup()
        self.goto(-10, 260)
        self.update()

    def update(self):
        self.clear()
        self.write(f"Level: {self.level}", align=ALIGN, font=FONT)

    def increase_score(self):
        self.level += 1
        self.clear()
        self.write(f"Level: {self.level}", align=ALIGN, font=FONT)

    def game_over(self):
        self.goto(0, 0)
        self.write(f"Game Over", align=ALIGN, font=FONT)
