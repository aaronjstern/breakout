from turtle import Screen, Turtle
from paddle import Paddle
from ball import Ball
from bricks import Brick
from lives_tracker import LivesTracker
from itertools import cycle
from scoreboard import ScoreBoard
from endmessage import EndMessage


screen = Screen()
screen.bgcolor("black")
screen.setup(width=1300, height=800)
screen.title("Breakout")
screen.tracer(0)


paddle = Paddle((0, -300))

screen.listen()
screen.onkey(paddle.move_left, "Left")
screen.onkey(paddle.move_right, "Right")

ball = Ball()

x_vals = [i for i in range(-600, 620, 110)]
y_vals = [i for i in range(0, 300, 60)]

positions = []

colors = ["red", "orange", "yellow", "green", "blue", "purple"]

for yval in y_vals:
    for xval in x_vals:
        positions.append((xval, yval))

positions_colors = list(zip(positions, cycle(colors)))

print(positions_colors)

bricks = []
for position_color in positions_colors:
    brick = Brick(position=position_color[0], color=position_color[1])
    bricks.append(brick)

lives = 5

livesTracker = LivesTracker(lives)

points = 0

scoreboard = ScoreBoard(points)

game_is_on = True
while lives > 0:
    screen.update()
    ball.move()

    if ball.ycor() < -380:
        lives -= 1
        livesTracker.update_lives(lives)
        ball.reset_position()

    if ball.ycor() > 380:
        ball.bounce_y()

    if ball.xcor() > 630 or ball.xcor() < -630:
        ball.bounce_x()

    if paddle.distance(ball) < 100 and ball.ycor() <= - 280:
        ball.bounce_y()

    for brick in bricks:
        if brick.distance(ball) < 65:
            bricks.remove(brick)
            ball.bounce_x()
            brick.reset()
            ball.bounce_y()
            points += 1
            scoreboard.update_scoreboard(points)

    if len(bricks) == 0:
        break

end_message = EndMessage()

if lives == 0:
    end_message.lose_message()
else:
    end_message.win_message()

screen.exitonclick()