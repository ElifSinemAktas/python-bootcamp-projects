
from turtle import Turtle, Screen
from ball import Ball
from racket import Racket
from scoreboard import Scoreboard
import time

screen = Screen()
screen.setup(1500, 900)
screen.bgcolor("black")
screen.title("Pong")
screen.tracer(0)

line = Turtle()
line.shape("square")
line.shapesize(0.5)
line.color("white")
line.penup()
line.goto(0, 435)
line.setheading(270)
while line.ycor() > -500:
    for i in range(3):
        line.stamp()
        line.forward(10)
    line.forward(30)

scoreboard = Scoreboard()

l_racket = Racket()
r_racket = Racket()
r_racket.create_rocket(720, 0)
l_racket.create_rocket(-720, 0)
ball = Ball()


screen.listen()
screen.onkey(r_racket.move_paddle_up, "Up")
screen.onkey(r_racket.move_paddle_down, "Down")
screen.onkey(l_racket.move_paddle_up, "w")
screen.onkey(l_racket.move_paddle_down, "s")

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(ball.ball_speed)
    ball.move()
    a = ball.heading()
    if ball.ycor() > 430 or ball.ycor() < -430:
        ball.setheading(360 - a)
    if ball.distance(r_racket) < 40 and ball.xcor() > 700 or ball.distance(l_racket) < 40 and ball.xcor() > -700:
        ball.setheading(180 - a)
    if ball.xcor() > 750:
        ball.reset_position()
        scoreboard.score_l()
    if ball.xcor() < -750:
        ball.reset_position()
        scoreboard.score_r()


screen.exitonclick()
