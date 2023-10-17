from turtle import Turtle

FONT = ("Courier", 8, "normal")


class PrintState(Turtle):
    def __init__(self):
        super().__init__()
        self.color("black")
        self.penup()
        self.hideturtle()

    def print_the_state(self, state_to_print, x, y):
        self.goto(x=x, y=y)
        self.write(state_to_print, False, font=FONT )
