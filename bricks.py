from turtle import Turtle


class Brick(Turtle):

    def __init__(self, position, color):
        super().__init__()
        self.position()
        self.shape("square")
        self.penup()
        self.shapesize(stretch_wid=2, stretch_len=5)
        self.goto(position)
        self.color(color)



