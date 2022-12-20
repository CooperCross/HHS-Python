# recursionSection2Q1
# Cooper Cross
# 1/7/20

import turtle

wn.colormode(255)
fortnite = turtle.Turtle()
wn = turtle.Screen()

def drawPoly(t, num_sides, side_length, r, g, b):
    for i in range(num_sides):
        t.forward(side_length)
        t.left(360/num_sides)
    t.fillcolor(r,g,b) 

