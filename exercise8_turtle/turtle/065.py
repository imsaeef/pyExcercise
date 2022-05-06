import turtle

turtle.bgcolor('cyan')

# show one
turtle.left(90)
turtle.forward(100)
turtle.right(90)
turtle.penup()

# show gap
turtle.forward(50)

# show two
turtle.pendown()
turtle.forward(100)
turtle.right(90)
turtle.forward(50)
turtle.right(90)
turtle.forward(100)
turtle.left(90)
turtle.forward(50)
turtle.left(90)
turtle.forward(100)
turtle.right(90)
turtle.penup()

# show gap
turtle.forward(50)

# show three
turtle.left(90)
turtle.pendown()
turtle.forward(100)
turtle.right(90)
turtle.forward(50)
turtle.right(90)
turtle.forward(60)
turtle.right(180)
turtle.forward(60)
turtle.right(90)
turtle.forward(50)
turtle.right(90)
turtle.forward(100)

turtle.hideturtle()
turtle.exitonclick()