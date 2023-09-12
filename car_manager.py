from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 20
CARS_POSITIONS = [(300, -250), (300, -228), (300, -206), (300, -184), (300, -162), (300, -140),
                  (300, -118), (300, -96), (300, -74), (300, -52), (300, -30), (300, -8), (300, 14),
                  (300, 36), (300, 58), (300, 80), (300, 102), (300, 124), (300, 146), (300, 168),
                  (300, 190), (300, 212), (300, 234)]


class CarManager(Turtle):
    def __init__(self):
        super().__init__()
        self.cars = []

    def create_rand_cars(self):
        for i in range(random.randint(0, 3)):
            new_car = Turtle()
            new_car.penup()
            new_car.goto(random.choice(CARS_POSITIONS))
            new_car.shape("square")
            new_car.color(random.choice(COLORS))
            new_car.shapesize(stretch_wid=1, stretch_len=2)
            self.cars.append(new_car)

    def move_cars(self):
        for car in self.cars:
            car.setheading(180)
            car.forward(MOVE_INCREMENT)

