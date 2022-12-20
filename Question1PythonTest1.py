# Question1PythonTest1.py
# Cooper Cross
# 10/8/19

import turtle
joe = turtle.Turtle()
x = 0
y = 0
joe.ht()

for i in range(3):
    joe.penup()
    joe.goto(x,y)
    joe.pendown()
    joe.forward(100)
    y = y + 20


