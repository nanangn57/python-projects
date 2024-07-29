import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

player = Player()
car_manager = CarManager()
score_board = Scoreboard()

screen.listen()
screen.onkey(player.up, "Up")
screen.onkey(player.down, "Down")
screen.onkey(player.go_left, "Left")
screen.onkey(player.go_right, "Right")

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()

    car_manager.generate_new_car()
    car_manager.move_cars()

    if player.ycor() == 280:
        score_board.increase_level()
        player.reset_game()
        car_manager.increase_speed()

    for car in car_manager.list_cars:
        if player.distance(car) < 28:
            game_is_on = False
            score_board.game_over()
