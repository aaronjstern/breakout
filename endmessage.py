from turtle import Turtle

class EndMessage(Turtle):

    def __init__(self):
        super().__init__()
        self.penup()
        self.goto(0, 300)
        self.color("white")
        self.hideturtle()

    def lose_message(self):
        self.write(f"Out of lives", font=("Courier", 40, "normal"), align="center")

    def win_message(self):
        self.write(f"You win!", font=("Courier", 40, "normal"), align="center")
