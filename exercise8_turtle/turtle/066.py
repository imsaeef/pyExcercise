import turtle
import random

turtle.bgcolor("black")

turtle.pensize(2)
for i in range(0,10):
    turtle.right(36)
    for i in range(0,8):
        turtle.color(random.choice(["red","green","blue","cyan","yellow","orange"]))
        turtle.forward(60)
        turtle.right(45)

turtle.exitonclick()
