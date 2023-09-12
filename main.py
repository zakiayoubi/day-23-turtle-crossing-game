import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

player = Player()

screen.listen()
screen.onkey(player.move, "Up")

cars = CarManager()
cars.create_rand_cars()


game_is_on = True
while game_is_on:
    time.sleep(.5)
    screen.update()
    cars.create_rand_cars()
    cars.move_cars()


screen.exitonclick()
