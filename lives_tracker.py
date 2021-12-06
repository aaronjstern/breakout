from turtle import Turtle


class LivesTracker(Turtle):

    def __init__(self, lives):
        super().__init__()
        self.penup()
        self.goto(400,300)
        self.color("white")
        self.hideturtle()
        self.write(f"Lives remaining: {lives}", font=("Courier", 20, "normal"))

    def update_lives(self, lives):
        self.clear()
        self.write(f"Lives remaining: {lives}", font=("Courier", 20, "normal"))

