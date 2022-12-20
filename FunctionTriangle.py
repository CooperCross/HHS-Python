# FunctionTriangle
# Cooper Cross
# 10/4/19

import turtle

def drawPoly(t, num_sides, side_length):
    for i in range(num_sides):
        t.forward(side_length)
        t.left(360/num_sides)

wn = turtle.Screen()
wn.bgcolor("lightgreen")

joe = turtle.Turtle()
joe.color("hotpink")
joe.pensize(3)


def drawEquitriangle(turt, size):
    drawPoly(turt, 3, size)

drawEquitriangle(joe, 100)
