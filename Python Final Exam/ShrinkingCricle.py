# ShrinkingCircle.py
# Cooper Cross
# 1/22/2020

import turtle

turt = turtle.Turtle()
wn = turtle.Screen()
turt.speed(0)
colors = ["red2","dark orange","yellow","green2","blue","purple3","purple4","MediumPurple1","deep pink"]
def shrinkingCircles(t,radius,x,y,colorNum,backNum):
    wn.bgcolor("black")
    t.pencolor(colors[colorNum])
    t.fillcolor(colors[backNum])
    t.pu()
    t.goto(x,y)
    t.pd()
    t.begin_fill()
    t.circle(radius)
    t.end_fill()
    if radius >= 10:
        shrinkingCircles(t,radius-30,x,y+30,colorNum+1,backNum-1)

shrinkingCircles(turt,275,0,-275,0,8)
    

