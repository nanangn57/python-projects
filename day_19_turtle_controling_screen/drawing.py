from turtle import Turtle, Screen

timmy = Turtle()


def go_forward():
    timmy.forward(10)


def go_backward():
    timmy.backward(10)


def clockwise():
    timmy.setheading(timmy.heading() + 10)


def counter_clockwise():
    timmy.setheading(timmy.heading() - 10)


def clear():
    timmy.up()
    timmy.home()
    timmy.clear()
    timmy.down()


screen = Screen()
screen.listen()
screen.onkey(key="w", fun=go_forward)
screen.onkey(key="s", fun=go_backward)
screen.onkey(key="a", fun=counter_clockwise)
screen.onkey(key="d", fun=clockwise)
screen.onkey(key="c", fun=clear)

screen.exitonclick()
