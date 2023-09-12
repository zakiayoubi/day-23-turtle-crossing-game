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

car_manager = CarManager()
car_manager.create_rand_car()

scoreboard = Scoreboard()

game_is_on = True

while game_is_on:
    time.sleep(.1)
    screen.update()
    car_manager.create_rand_car()
    car_manager.move_cars()
    # detect collision with car objects
    for car in car_manager.all_cars:
        if car.distance(player) < 20:
            game_is_on = False
            scoreboard.game_over()

    # reaching the other side of the screen
    if player.is_at_finish_line():
        player.goto_starting_line()
        car_manager.level_up()
        scoreboard.increase_level()
        scoreboard.update_scoreboard()

screen.exitonclick()
