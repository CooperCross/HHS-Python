# CosinePlot.py
# Cooper Cross
# 10/22/19

import turtle, math
t = turtle.Turtle()
b = turtle.Screen()
b.setworldcoordinates(0, -2, 360, 2)
x = 1

t.penup()
t.goto(0,math.cos(math.radians(0)))
t.pendown()

for angle in range(500):
    y = math.cos(math.radians(angle))
    t.goto(angle, y)
