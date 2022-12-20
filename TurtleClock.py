# TurtleClock.py
# Cooper Cross
# 9/24/19

import turtle

joe = turtle.Turtle()
joe.pencolor("blue")
joe.fillcolor("blue")
joe.shape("turtle")
joe.turtlesize(2,2,3)
joe.speed(0)
joe.left(90)
wn = turtle.Screen()
wn.bgcolor("palegreen")
joe.begin_fill()
for i in range(12):
    joe.penup()
    joe.forward(100)
    joe.pendown()
    joe.forward(10)
    joe.penup()
    joe.forward(40)
    joe.stamp()
    joe.backward(150)
    joe.right(30)
joe.end_fill()
