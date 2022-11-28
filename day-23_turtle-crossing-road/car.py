from turtle import Turtle
import random

MOVE = 20


def pick_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    color_tuple = (r, g, b)
    return color_tuple


class Car(Turtle):
    def __init__(self):
        super().__init__()
        self.car_list = []

    def new_car(self):
        random_choice = random.randint(1, 3)
        if random_choice == 1:
            new_car = Car()
            new_car.color(pick_color())
            new_car.shape("square")
            new_car.shapesize(1, 2)
            new_car.penup()
            var = random.randrange(-250, 250)
            new_car.goto(320, var)
            self.car_list.append(new_car)
            # for i in self.car_list:
            #     if i.distance(new_car) < 50:
            #         new_var = random.randrange(-250, 250)
            #         new_car.goto(320, new_var)

    def move(self):
        for i in self.car_list:
            i.backward(MOVE)
            if i.xcor() < -400:
                self.car_list.remove(i)





