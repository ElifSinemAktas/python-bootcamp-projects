from turtle import Turtle, Screen
import random
screen = Screen()
screen.setup(width=500, height=400)

colors = ["red", "green", "purple", "yellow", "blue", "orange"]
choice = screen.textinput("Make your choice", "Which turtle will be winner? Enter a color "
                                              "(red, green, purple, yellow, blue, orange): ")
turtle_list = []
x = -230
y = -120
for i in range(6):
    new_turtle = Turtle()
    new_turtle.shape("turtle")
    new_turtle.color(colors[i])
    new_turtle.penup()
    new_turtle.goto(x, y)
    y += 40
    turtle_list.append(new_turtle)

game = True
while game:
    for turtle in turtle_list:
        move = random.randint(0, 10)
        turtle.forward(move)
        if turtle.xcor() > 230:
            game = False
            if choice == turtle.pencolor():
                print("You win.")
            else:
                print("You lost")





#
# timmy = Turtle(shape="turtle")
#
# timmy.goto(-230, 0)