import turtle

# turtle command
scr = turtle.Screen()  # screen show as scr
scr.bgcolor("cyan")  # background color
#turtle.penup()  # remove pen
turtle.pendown()  # show pen
turtle.pensize(3) # pen size
#turtle.left(60)  # rotate left side
#turtle.right(60)  # rotate right side
#turtle.forward(100)  # move turtle 100 steps
#turtle.shape("turtle")  # change turtle shape
#turtle.hideturtle()  # hide turtle shape
#turtle.showturtle()  # show turtle shape
#turtle.begin_fill()  # fill in the shape
#turtle.end_fill()  # stop filling in the shape
turtle.color("yellow","red")  # colors filling in the shape outline and fill color
#turtle.exitonclick()  # close turtle


for i in range(0,10):
    turtle.right(36)
    for i in range(0,5):
        turtle.forward(100)
        turtle.right(72)

turtle.exitonclick()