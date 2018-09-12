import turtle

turtle.speed(20)

turtle.pencolor("yellow")

turtle.color("yellow")
#this is to fill in the face yellow
turtle.begin_fill()

turtle.circle(200)

turtle.end_fill()

turtle.penup()

turtle.goto(100,100)

turtle.pencolor("black")

turtle.pendown()

turtle.width(5)

turtle.back(200)

turtle.penup()

turtle.goto(0,200)

turtle.pendown()

#this was to create a loop
def drawANose():
    for x in range(1):
        turtle.right(60)
        turtle.forward(75)
        turtle.right(130)
        turtle.forward(50)
for x in range(1):
    drawANose()

turtle.penup()

turtle.goto(100,250)

turtle.color("black")

turtle.left(280)

turtle.pendown()

turtle.pencolor("black")

#this part is to create a loop to draw an eye
def drawAnEye():
    for x in range(6):
        turtle.forward(30)
        turtle.left(60)
for x in range(1):
    turtle.color("black")
    turtle.begin_fill()
    drawAnEye()
    turtle.end_fill()

turtle.penup()
turtle.goto(-50,250)
turtle.pendown()
for x in range(1):
    turtle.color("black")
    turtle.begin_fill()
    drawAnEye()
    turtle.end_fill()

turtle.exitonclick()
