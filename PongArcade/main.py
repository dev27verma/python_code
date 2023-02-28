import time
from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard


screen = Screen()
screen.setup(800,600)
screen.bgcolor("black")
screen.title("Pong Arcade")
screen.tracer(0)

l_paddle = Paddle((-380,0))
r_paddle = Paddle((380,0))
ball = Ball()
score_card = Scoreboard()

screen.listen()
screen.onkey(l_paddle.up,"w")
screen.onkey(l_paddle.down,"s")
screen.onkey(r_paddle.up,"Up")
screen.onkey(r_paddle.down,"Down")

game_is_on = True
while game_is_on:
    time.sleep(ball.move_ball)
    screen.update()
    ball.move()

    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    if ball.distance(r_paddle) < 50 and ball.xcor() > 360 or ball.distance(l_paddle) < 50 and ball.xcor() < -360:
        ball.bounce_x()

    if ball.xcor() > 380:
        ball.reset_position()
        ball.bounce_x()
        score_card.l_score_card()

    if ball.xcor() < -380:
        ball.reset_position()
        ball.bounce_y()
        score_card.r_score_card()

screen.exitonclick()