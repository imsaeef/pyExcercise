import turtle

turtle.pensize(2)
turtle.shape("turtle")


for x in range(0,10):
    turtle.right(36)
    for i in range(0,8):
        turtle.forward(50)
        turtle.right(45)

turtle.hideturtle()

turtle.exitonclick()