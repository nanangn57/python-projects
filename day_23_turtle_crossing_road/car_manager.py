from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager:

    def __init__(self):
        self.list_cars = []
        self.speed = STARTING_MOVE_DISTANCE

    def generate_new_car(self):
        chance = random.randint(1, 6)
        if chance == 1:
            new_car = Turtle()
            new_car.shape("square")
            new_car.shapesize(stretch_len=2)
            new_car.penup()
            new_car.color(random.choice(COLORS))
            pos_y = random.randint(-250, 250)
            new_car.goto(300, pos_y)
            self.list_cars.append(new_car)

    def move_cars(self):
        for car in self.list_cars:
            car.backward(self.speed)

    def increase_speed(self):
        self.speed += MOVE_INCREMENT
