from turtle import Turtle


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.color("white")
        self.penup()
        self.l_score = 0
        self.r_score = 0
        self.score_update()

    def score_update(self):

        self.clear()
        self.goto(-100, 300)
        self.write(self.l_score, align="center", font=("Courier", 80, "normal"))
        self.goto(100, 300)
        self.write(self.r_score, align="center", font=("Courier", 80, "normal"))

    def score_l(self):
        self.l_score += 1
        self.score_update()

    def score_r(self):
        self.r_score += 1
        self.score_update()



