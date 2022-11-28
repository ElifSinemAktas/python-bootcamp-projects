from turtle import Turtle

START = 3
MOVE_BODY = 20


class Snake:
    def __init__(self):
        self.bodies = []
        self.create_snake()
        self.head = self.bodies[-1]

    def create_snake(self):
        x = 0
        y = 0
        for position in range(START):
            self.bodies.append(self.add_body())
            self.bodies[position].goto(x=x, y=y)
            x += MOVE_BODY

    def add_body(self):
        body = Turtle()
        body.shape("square")
        body.color("white")
        body.penup()
        return body

    def extend_body(self):
        self.bodies.insert(0, self.add_body())
        self.bodies[0].goto(self.bodies[1].position())
        # self.bodies[0].backward(MOVE_BODY)

    def move(self):
        for i in range(len(self.bodies) - 1):
            self.bodies[i].goto(self.bodies[i + 1].position())
        self.bodies[-1].forward(MOVE_BODY)

    def up(self):
        if self.bodies[-1].heading() != 270:
            self.bodies[-1].setheading(90)

    def down(self):
        if self.bodies[-1].heading() != 90:
            self.bodies[-1].setheading(270)

    def left(self):
        if self.bodies[-1].heading() != 0:
            self.bodies[-1].setheading(180)

    def right(self):
        if self.bodies[-1].heading() != 180:
            self.bodies[-1].setheading(0)

    def clear(self):
        for i in self.bodies:
            i.clear()







