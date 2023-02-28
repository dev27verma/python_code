from turtle import Turtle

ALIGN = "center"
FONT = ("aerial",24 , "normal")
class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.l_score = 0
        self.r_score = 0
        self.hideturtle()
        self.update_score_card()


    def update_score_card(self):
        self.clear()
        self.goto(-100, 250)
        self.write(self.l_score, align=ALIGN, font=FONT)
        self.goto(100, 250)
        self.write(self.r_score, align=ALIGN, font=FONT)

    def l_score_card(self):
        self.l_score += 1
        self.update_score_card()

    def r_score_card(self):
        self.r_score += 1
        self.update_score_card()