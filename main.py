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

correct_guesses = []

while correct_guesses != 50:

    answer = screen.textinput(title=f"{len(correct_guesses)}/50 Guess the State",
                              prompt="What's another states name?").title()

    for state in data["state"]:
        if state == answer:
            print_state = PrintState()
            correct_guesses.append(state)
            x_coor = data[data["state"] == state]["x"]
            x_coor_item = x_coor.tolist()
            y_coor = data[data["state"] == state]["y"]
            y_coor_item = y_coor.tolist()
            print_state.print_the_state(state, x_coor_item[0], y_coor_item[0])
            break
    if answer == "Exit":
        missing_states = []
        for state in data.state.to_list():
            if state not in correct_guesses:
                missing_states.append(state)
        new_data = pandas.DataFrame(missing_states)
        new_data.to_csv("states_to_learn.csv")
        break




