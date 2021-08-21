import turtle
from turtle import Turtle, Screen
import random
screen =Screen()
screen.setup(width=500, height=400)
game_on = False
user_bet = screen.textinput(title="who will win the race?", prompt="Red/Green/Orange/Pink/Black/blue/yellow")
print(f"your bets on {user_bet}")


colors = ["red","green","orange","pink","black","blue","yellow"]
y_position = [-120, -80, -40, 0, 40, 80, 120]
all_turtles = []

if user_bet:
    game_on = True

for turtle_index in range(0, 7):
    asnan = Turtle()
    asnan.shape("turtle")
    asnan.color(colors[turtle_index])
    asnan.penup()
    asnan.goto(x=-230,y=y_position[turtle_index])
    all_turtles.append(asnan)



while game_on:
    for turtle in all_turtles:
        if turtle.xcor() > 220:
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                print(f"You have won, the {turtle.pencolor()} takes the day")
                game_on = False
            else:
                print(f"You have lost the winner is {turtle.pencolor()}")
                game_on = False

        distance = random.randint(0, 10)
        turtle.forward(distance)




screen.exitonclick()