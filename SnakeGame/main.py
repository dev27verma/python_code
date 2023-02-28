import time
from turtle import Screen
from player import Player
from car import Car
from score import Score

screen = Screen()
screen.setup(800, 600)
screen.title("My Game")
screen.tracer(0)

player = Player()
car = Car()
score = Score()

screen.listen()
screen.onkey(player.up, "Up")

game_is_on = True

while game_is_on:
    screen.update()
    time.sleep(0.1)
    car.create_car()
    car.move()

    for detect in car.all_cars:
        if detect.distance(player) < 20:
            game_is_on = False
            score.game_over()

    if player.ycor() > 280:
        player.reset()
        score.increase_score()

screen.exitonclick()
