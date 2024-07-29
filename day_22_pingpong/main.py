import time
from turtle import Screen
from paddle import Paddle
from ball import Ball
from score import Score

screen = Screen()
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.title("Ping Pong")
screen.tracer(0)

r_paddle = Paddle(x_pos=350, y_pos=0)
l_paddle = Paddle(x_pos=-350, y_pos=0)
ball = Ball()
score = Score()

screen.listen()
screen.onkey(r_paddle.up, "Up")
screen.onkey(r_paddle.down, "Down")
screen.onkey(l_paddle.up, "w")
screen.onkey(l_paddle.down, "s")

game_on = True
while game_on:
    screen.update()
    speed_ball = 0.01
    time.sleep(speed_ball)

    ball.move()
    score.draw_line()
    score.update_score()
    score_update = 0

    if abs(ball.ycor()) > 290:
        ball.bounce_wall()

    if (ball.distance(r_paddle) < 35 and ball.xcor() < 350) or (ball.distance(l_paddle) < 35 and ball.xcor() > -350):
        ball.bounce_paddle()

    if ball.xcor() > 380:
        score.increase_left_score()
        score_update = 1
    elif ball.xcor() < -380:
        score.increase_right_score()
        score_update = 1

    if score_update == 1:
        ball.reset_ball()
        r_paddle.reset_r_paddle()
        l_paddle.reset_l_paddle()
        r_paddle.distance += 5
        l_paddle.distance += 5
        speed_ball *= 0.03

    if score.l_score == 3 or score.r_score == 3:
        game_on = False
        score.game_over()

screen.exitonclick()

