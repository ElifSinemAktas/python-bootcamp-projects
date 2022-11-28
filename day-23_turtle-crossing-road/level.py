from turtle import Turtle

ALIGN = "center"
FONT = ("Verdana", 10, "normal")

class Level(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.level = 0
        self.speed = 0.2
        self.level_update()

    def level_update(self):
        self.goto(-250, 270)
        self.clear()
        self.write(f"Level : {self.level}", align=ALIGN, font=FONT)

    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER", align=ALIGN, font=FONT)

    def level_up(self):
        self.level += 1
        self.speed *= 0.5

