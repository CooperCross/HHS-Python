# recursionSection2Q1
# Cooper Cross
# 1/7/20

import turtle
turtle.tracer(0)
wn= turtle.Screen()
wn.colormode(255)
fot = turtle.Turtle()
wn.bgcolor(245, 66, 215)


def drawPoly(t, num_sides, side_length,r,g,b):
    t.pencolor(0,0,0)
    t.fillcolor(r,g,b)
    t.begin_fill()
    for i in range(num_sides):
        t.forward(side_length)
        t.left(360/num_sides)
    t.end_fill()
    if num_sides > 2:
        drawPoly(t, num_sides - 1, side_length,r + 10, g  + 25, b + 35)
        
drawPoly(fot,10,50,0,0,0)


        


