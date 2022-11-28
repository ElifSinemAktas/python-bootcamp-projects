from turtle import Turtle
ALIGNMENT = "center"
FONT = ('Arial', 12, 'normal')

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        with open("/Users/beyri/Desktop/data.txt", mode="r") as score_file:
            self.high_score = int(score_file.read())
        self.color("white")
        self.penup()
        self.goto(0, 280)
        self.hideturtle()
        self.write_score()

    def write_score(self):
        self.write(f"Score= {self.score} High Score = {self.high_score}", align=ALIGNMENT, font=FONT)

    def add_score(self):
        self.clear()
        self.score += 1
        self.write_score()

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open("/Users/beyri/Desktop/data.txt", mode="w") as score_file:
                score_file.write(f"{self.high_score}")
        self.goto(0, 0)
        self.write("GAME OVER", align=ALIGNMENT, font=FONT)


    # def game_over(self):
    #     self.goto(0, 0)
    #     self.write("GAME OVER", align=ALIGNMENT, font=FONT)

