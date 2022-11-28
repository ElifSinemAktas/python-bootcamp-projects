from turtle import Turtle
import random


class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.color("yellow")
        self.shape("circle")
        self.penup()
        self.turtlesize(0.5)
        self.refresh()

    def refresh(self):
        x = random.randrange(-240, 240, 20)
        y = random.randrange(-240, 240, 20)
        self.goto(x=x, y=y)





