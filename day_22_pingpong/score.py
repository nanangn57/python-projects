from turtle import Turtle


class Score(Turtle):

    def __init__(self):
        super().__init__()
        self.color("white")
        self.draw_line()
        self.l_score = 0
        self.r_score = 0
        self.update_score()

    def draw_line(self):
        self.penup()
        self.goto((0, -300))
        self.setheading(90)
        self.pensize(5)
        for _ in range(30):
            self.penup()
            self.forward(10)
            self.pendown()
            self.forward(10)

    def update_score(self):
        self.penup()
        self.goto(0, 240)
        self.hideturtle()
        self.write(f"{self.l_score}    {self.r_score}",
                   align="center", font=('arial', 30, 'bold'))

    def increase_left_score(self):
        self.l_score += 1
        self.clear()
        self.write(f"{self.l_score}    {self.r_score}",
                   align="center", font=('arial', 30, 'bold'))

    def increase_right_score(self):
        self.r_score += 1
        self.clear()
        self.write(f"{self.l_score}    {self.r_score}",
                   align="center", font=('arial', 30, 'bold'))

    def game_over(self):
        self.goto(0, 0)
        self.write(f"GAME OVER", align="center",
                   font=('Arial', 40, 'bold'))
