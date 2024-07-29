from turtle import Turtle


class Score(Turtle):

    def __init__(self):
        super().__init__()
        self.color("white")
        self.score = 0
        self.high_score = 0
        self.update_highscore()
        self.penup()
        self.goto(0, 280)
        self.hideturtle()
        self.update_score()

    def update_highscore(self):
        with open("score.txt") as file:
            self.high_score = int(file.read())

    def update_score(self):
        self.clear()
        self.write(f"Score: {self.score} High Score: {self.high_score}",
                   align="center", font=('Arial', 12, 'normal'))

    def increase_score(self):
        self.score += 1
        self.clear()
        self.write(f"Score: {self.score} High Score: {self.high_score}",
                   align="center", font=('Arial', 12, 'normal'))

    # def game_over(self):
    #     self.goto(0, 0)
    #     self.write(f"GAME OVER", align="center",
    #                font=('Arial', 24, 'normal'))

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
        self.score = 0
        self.update_score()

        with open("score.txt", mode="w") as file:
            file.write(f"{self.high_score}")
