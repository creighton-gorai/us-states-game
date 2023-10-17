import turtle
import pandas
from print_state import PrintState

screen = turtle.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)
screen.setup(width=850, height=525)
turtle.shape(image)

data = pandas.read_csv("50_states.csv")

correct_guesses = 0

is_game_on = True
while is_game_on:

    answer = screen.textinput(title=f"{correct_guesses}/50 Guess the State", prompt="What's another states name?")
    print(answer)
    caps_answer = answer.title()
    print(caps_answer)

    for state in data["state"]:
        if state == caps_answer:
            print_state = PrintState()
            x_coor = data[data["state"] == state]["x"]
            x_coor_item = x_coor.tolist()
            y_coor = data[data["state"] == state]["y"]
            y_coor_item = y_coor.tolist()
            print_state.print_the_state(state, x_coor_item[0], y_coor_item[0])
            correct_guesses += 1
            break



