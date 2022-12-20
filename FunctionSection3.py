#FunctionsSection3.py
#Cooper Cross
#19

import turtle

joe = turtle.Turtle()
joe.pensize(3)
joe.pencolor("hotpink")
wn = turtle.Screen()
wn.bgcolor("lightgreen")
joe.speed(11)

joe.penup()
joe.goto(-175,100)
joe.pendown()

for i in range(5):
    joe.penup()
    joe.forward(350)
    joe.right(144)
    joe.pendown()
    for i in range(5):
        joe.forward(100)
        joe.left(216)
