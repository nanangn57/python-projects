from turtle import Turtle


class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.penup()
        self.x_move = 10
        self.y_move = 10

    def move(self):
        x_pos = self.xcor() + self.x_move
        y_pos = self.ycor() + self.y_move
        self.goto((x_pos, y_pos))

    def bounce_wall(self):
        self.y_move *= -1

    def bounce_paddle(self):
        self.x_move *= -1

    def reset_ball(self):
        self.goto((0, 0))




