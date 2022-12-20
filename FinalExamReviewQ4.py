# FinalExamReviewQ4.py
# Cooper Cross
# 1/15/2020

import turtle
turt = turtle.Turtle()

def drawPoly(t,num_sides,side_length):
    for i in range(num_sides):
        t.fd(side_length)
        t.left(360/num_sides)

def shrinkingSquares(t,sideLength,x,y):
    t.pu()
    t.goto(x,y)
    t.pd()
    drawPoly(t,4,sideLength)
    if sideLength >= 10:
        shrinkingSquares(t,sideLength-20,x,y)
    
shrinkingSquares(turt,100,0,0)


