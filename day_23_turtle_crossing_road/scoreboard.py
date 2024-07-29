from turtle import Turtle

FONT = ("Courier", 20, "normal")


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.color("black")
        self.level = 1
        self.penup()
        self.goto(-280, 260)
        self.hideturtle()
        self.update_level()

    def update_level(self):
        self.write(f"Level: {self.level}", align="left", font=FONT)

    def increase_level(self):
        self.clear()
        self.level += 1
        self.write(f"Level: {self.level}", align="left", font=FONT)

    def game_over(self):
        self.goto(0, 0)
        self.write(f"GAME OVER", align="center", font=FONT)
