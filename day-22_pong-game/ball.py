import random
from turtle import Turtle

headlist = [45, 135, 225, 315]



class Ball(Turtle):
    def __init__(self):
        super().__init__()
        x = 0
        y = random.randint(-400, 400)
        self.shape("circle")
        self.color("white")
        self.penup()
        self.goto(x, y)
        self.setheading(random.choice(headlist))
        self.ball_speed = 0.05

    def move(self):
        self.forward(20)

    def reset_position(self):
        x = 0
        y = random.randint(-400, 400)
        self.goto(x, y)
        self.ball_speed *= 0.9

