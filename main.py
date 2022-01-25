import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

player = Player()
cars = CarManager()
scoreboard = Scoreboard()


screen.listen()
screen.onkey(player.move, 'Up')

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    cars.create_car()
    cars.move()
    for car in cars.all_cars:
        if car.distance(player) < 20:
            scoreboard.gameover()
            game_is_on = False

    if player.is_at_finish_line():
        player.goto_start()
        cars.levelup()
        scoreboard.increase_level()


screen.exitonclick()