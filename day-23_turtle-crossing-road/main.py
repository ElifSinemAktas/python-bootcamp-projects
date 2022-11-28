from turtle import Turtle, Screen
from car import Car
import random
import time
from player import Player
from level import Level

screen = Screen()
screen.setup(width=600, height=600)
screen.title("Cross Over")
screen.colormode(255)
screen.tracer(0)

car = Car()
car.hideturtle()

player = Player()
level = Level()

screen.listen()
screen.onkeypress(player.go_up, "Up")
screen.onkeypress(player.go_right, "Right")
screen.onkeypress(player.go_left, "Left")

game_is_on = True
while game_is_on:
    time.sleep(level.speed)
    screen.update()
    car.new_car()
    car.move()
    if player.ycor() > 280:
        player.update()
        level.level_up()
        level.level_update()
    for i in car.car_list:
        if i.distance(player) < 20:
            game_is_on = False
            level.game_over()

screen.exitonclick()