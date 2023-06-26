import turtle
import pandas

screen = turtle.Screen()
screen.title("US States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

# def get_coor(x, y):
#     print(x, y)
#
#
# turtle.onscreenclick(get_coor)
#
# turtle.mainloop()


data = pandas.read_csv("50_states.csv")
all_states = data.state.tolist()
guessed = []

while len(guessed)< 50:
    ans_state = screen.textinput(title=f"{len(guessed)}/50 states correct",
                                 prompt="What's another states name?").title()
    if ans_state == "Exit":
        missing = [state for state in all_states if state not in guessed]
        # missing = []
        # for x in all_states:
        #     if x not in guessed:
        #         missing.append(x)
        new_data = pandas.DataFrame(missing)
        new_data.to_csv("states_to_learn.csv")
        break

    if ans_state in all_states:
        guessed.append(ans_state)
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        state_data = data[data.state == ans_state]
        t.goto(int(state_data.x), int(state_data.y))
        t.write(ans_state)




