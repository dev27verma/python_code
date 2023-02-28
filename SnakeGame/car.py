from turtle import Turtle
from random import randint, choice

COLOR = ["red", "green", "blue", "black", "purple", "yellow"]
CAR_MOVEMENT = 5
SPEED_INCREMENT = 5


class Car:
    def __init__(self):
        self.all_cars = []

    def create_car(self):
        chance = randint(1, 6)
        if chance == 1:
            new_car = Turtle("square")
            new_car.shapesize(1, 2)
            new_car.color(choice(COLOR))
            new_car.penup()
            new_car.goto(400, randint(-250, 250))
            self.all_cars.append(new_car)

    def move(self):
        for car in self.all_cars:
            car.backward(5)
