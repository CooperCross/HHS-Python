# TurtlePractice.py
# Cooper Cross
# 9/4/19

import turtle
Turner = turtle.Turtle()
wn = turtle.Screen()
wn.bgcolor("sky blue")
Turner.speed(11)

#draws square & changes pen and fill colors
Turner.pencolor("lime green")
Turner.pensize(4)
Turner.fillcolor("spring green")
Turner.begin_fill()
Turner.forward(100)
Turner.left(90)
Turner.forward(100)
Turner.left(90)
Turner.forward(100)
Turner.left(90)
Turner.forward(100)
Turner.left(90)
Turner.end_fill()

#move turtle
Turner.penup()
Turner.goto(-200,200)
Turner.pendown()

#draws circle
Turner.pencolor("mediumorchid1")
Turner.fillcolor("orchid1")
Turner.pensize(10)
Turner.begin_fill()
Turner.circle(75)
Turner.end_fill()

#move turtle
Turner.penup()
Turner.goto(-200,-150)
Turner.pendown()

#change turtle shape, turtle size and stamp
Turner.pencolor("yellow")
Turner.fillcolor("darkorange1")
Turner.shape("turtle")
Turner.turtlesize(2,2,3)
Turner.stamp()

x = -150
for i in range(6):
    x = x - 50
    Turner.penup()
    Turner.goto(x,-150)
    Turner.pendown()
    Turner.stamp()
    
#Turner.hideturtle()
