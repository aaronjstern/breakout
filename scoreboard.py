from turtle import Turtle

class ScoreBoard(Turtle):

    def __init__(self, points):
        super().__init__()
        self.penup()
        self.goto(-600, 300)
        self.color("white")
        self.hideturtle()
        self.write(f"Points: {points}", font=("Courier", 20, "normal"))

    def update_scoreboard(self, points):
        self.clear()
        self.write(f"Points: {points}", font=("Courier", 20, "normal"))
