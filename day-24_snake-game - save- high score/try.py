from turtle import Turtle, Screen

screen = Screen()

from food import Food
food = Food()
food.create_food()
pos=food.pos()
print(pos)
screen.exitonclick()


