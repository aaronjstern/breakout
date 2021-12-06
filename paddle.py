from turtle import Screen, Turtle


class Paddle(Turtle):

    def __init__(self, position):
        Turtle.__init__(self)
        self.shape("square")
        self.color("white")
        self.penup()
        self.shapesize(stretch_wid=1, stretch_len=10)
        self.goto(position)

    def move_right(self):
        new_x = self.xcor() + 40
        self.goto((new_x, self.ycor()))

    def move_left(self):
        new_x = self.xcor() - 40
        self.goto((new_x, self.ycor()))



