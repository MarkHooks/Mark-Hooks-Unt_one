# this program is to draw a face with 2 eyes a nose and a mouth

import turtle

turtle.speed(40)

turtle.pencolor("yellow")

turtle.color("yellow")
# this is to draw the shape of the face
turtle.begin_fill()

turtle.circle(200)

turtle.end_fill()

turtle.penup()

turtle.goto(100, 100)

turtle.pencolor("black")

turtle.pendown()
# this part is to draw the mouth
turtle.width(5)

turtle.back(200)

turtle.penup()

turtle.goto(0, 200)

turtle.pendown()


# this was to create a loop for the nose
def draw_nose():
    for x in range(1):
        turtle.right(60)
        turtle.forward(75)
        turtle.right(130)
        turtle.forward(50)


for v in range(1):
    draw_nose()

turtle.penup()

turtle.goto(100, 250)

turtle.color("black")

turtle.left(280)

turtle.pendown()

turtle.pencolor("black")


# this part is to create a loop to draw an eye
def draw_eye():
    for w in range(6):
        turtle.forward(30)
        turtle.left(60)


for z in range(1):
    turtle.color("black")
    turtle.begin_fill()
    draw_eye()
    turtle.end_fill()

turtle.penup()
turtle.goto(-50, 250)
turtle.pendown()
for y in range(1):
    turtle.color("black")
    turtle.begin_fill()
    draw_eye()
    turtle.end_fill()

# all the lines below are for drawing the hair
turtle.penup()

turtle.goto(165, 320)

turtle.pendown()

turtle.width(10)

turtle.pencolor("brown")

turtle.forward(50)

turtle.penup()

turtle.goto(120, 360)

turtle.pendown()

turtle.forward(50)

turtle.penup()

turtle.goto(70, 390)

turtle.pendown()

turtle.forward(50)

turtle.penup()

turtle.goto(10, 400)

turtle.pendown()

turtle.forward(50)

turtle.penup()

turtle.goto(-50, 390)

turtle.pendown()

turtle.forward(50)

turtle.penup()

turtle.goto(-120, 360)

turtle.pendown()

turtle.forward(50)

turtle.penup()

turtle.goto(-165, 320)

turtle.pendown()

turtle.forward(50)

turtle.exitonclick()
