# InputPolygon.py
# Cooper Cross
# 9/18/19

s = input("Enter amount of sides: ")
s = int(s)
l = input("Enter side length: ")
l = int(l)
p = input("Enter line color: ")
p = str(p)
f = input("Enter fill color: ")
f = str(f)

import turtle

wn = turtle.Screen()
Joe = turtle.Turtle()

Joe.pencolor(p)
Joe.begin_fill()
Joe.fillcolor(f)
Joe.pensize(5)

for i in range(s):
    Joe.forward(l)
    Joe.left(360/s)

Joe.end_fill()


