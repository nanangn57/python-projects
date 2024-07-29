from turtle import Turtle, Screen
import random
import colorgram

colors = colorgram.extract('image.jpg', 100)
colors = [color.rgb for color in colors]


def random_color(list_colors):
    temp_color = random.choice(list_colors)
    r = temp_color.r/255
    g = temp_color.g/255
    b = temp_color.b/255
    return r, g, b


timmy = Turtle()
timmy.hideturtle()
timmy.up()
timmy.setposition(-300, -270)
timmy.speed("fastest")

row = 0
while row <= 28:
    for _ in range(30):
        timmy.dot(10, random_color(colors))
        timmy.forward(20)

    timmy.left(90)
    timmy.forward(20)
    timmy.left(90)
    timmy.forward(20)

    for _ in range(30):
        timmy.dot(10, random_color(colors))
        timmy.forward(20)

    timmy.right(90)
    timmy.forward(20)
    timmy.right(90)
    timmy.forward(20)

    row += 2

Screen()
