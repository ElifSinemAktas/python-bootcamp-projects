import turtle
import pandas as pd
import time

screen = turtle.Screen()
screen.title("U.S States Game")
screen.setup(width=725, height=491)
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

# Create a seperate pen/turtle to write true answers/states on screen.
pen = turtle.Turtle()
pen.hideturtle()

# This information below is awesome, to take coordinate from screen just clicking!
# def get_mouse_click_coor(x, y):
#     print(x, y)
#
# turtle.onscreenclick(get_mouse_click_coor)

# screen.exitonclick()

game_is_on = True

states_frame = pd.read_csv("50_states.csv")
state_list = states_frame.state.to_list()
total_states = 50
true_answer = 0
remain_answer = 50
guess_list = []

while remain_answer > 0:
    time.sleep(1)
    answer_state = screen.textinput(title=f"{true_answer}/{total_states} States Correct",
                                    prompt="What is another states name?").title()
    remain_answer -= 1

    # You can also check answer with the code below
    # if answer_state in state_list

    if answer_state == "Exit":
        # missing_states = pd.DataFrame(list(set(state_list) - set(guess_list)))
        missing_states = [i for i in state_list if i not in guess_list]
        missing_states = pd.DataFrame(missing_states)
        missing_states.to_csv("missing_states.csv")
        break

    for i in state_list:
        if answer_state == i:
            state_name = states_frame[states_frame.state == i]
            x_cor = int(state_name.x)
            y_cor = int(state_name.y)
            pen.penup()
            pen.goto(x_cor, y_cor)
            pen.write(f"{i}", align="center")
            true_answer += 1
            guess_list.append(i)

turtle.mainloop()
