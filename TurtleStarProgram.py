# TurtleStarProgram.py
# Cooper Cross
# 9/18/19

import turtle
Joe = turtle.Turtle()

l = input("Enter line color: ")
b = input("Enter background color: ")
s = input("Enter pen size: ")
wn = turtle.Screen()
wn.bgcolor(b)
Joe.pencolor(l)
Joe.pensize(s)

for i in range(5):
    Joe.forward(150)
    Joe.left(216)


    
