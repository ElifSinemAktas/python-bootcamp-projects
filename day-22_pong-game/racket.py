from turtle import Turtle


class Racket(Turtle):
    def __init__(self):
        super().__init__()
        self.player = []

    def create_rocket(self, xcor, ycor):
        self.shape("square")
        self.color("white")
        self.penup()
        self.goto(xcor, ycor)
        self.shapesize(5, 1)

    def move_paddle_up(self):
        new_y = self.ycor() + 20
        self.goto(self.xcor(), new_y)

    def move_paddle_down(self):
        new_y = self.ycor() - 20
        self.goto(self.xcor(), new_y)













