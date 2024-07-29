from turtle import Turtle
DISTANCE = 30


class Paddle(Turtle):

    def __init__(self, x_pos, y_pos):
        super().__init__()
        self.color("white")
        self.speed("fastest")
        self.shape("square")
        self.penup()
        self.shapesize(stretch_wid=5, stretch_len=1, outline=1)
        self.goto((x_pos, y_pos))
        self.distance = DISTANCE

    def up(self):
        new_y = self.ycor() + self.distance
        self.goto((self.xcor(), new_y))

    def down(self):
        new_y = self.ycor() - self.distance
        self.goto((self.xcor(), new_y))

    def reset_l_paddle(self):
        self.clear()
        self.goto(-350, 0)

    def reset_r_paddle(self):
        self.clear()
        self.goto(350, 0)
