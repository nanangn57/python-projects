from turtle import Turtle, Screen
import random

screen = Screen()
screen.setup(width=500, height=450)
user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter a color: ")
colors = ["red", "orange", "yellow", "green", "blue", "purple"]
list_turtles = []
racing = False

y_position = -120
for i in range(len(colors)):
    new_turtle = Turtle(shape="turtle")
    new_turtle.color(colors[i])
    new_turtle.up()
    new_turtle.goto(x=-230, y=y_position)
    y_position += 50
    list_turtles.append(new_turtle)

if user_bet:
    racing = True

    while racing:
        for turtle in list_turtles:
            distance = random.randint(0, 10)
            turtle.forward(distance)
            if turtle.position()[0] == 240:
                racing = False
                if turtle.color() == user_bet:
                    print(f"Your won! Turtle {user_bet} won!")
                else:
                    print(f"You lose! Turtle {turtle.color()[0]} won!")

screen.exitonclick()
