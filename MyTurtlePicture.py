
# MyTurtlePicture.py
# Cooper Cross
# 9/25/19
import turtle
import random

def randomColor():
    red = random.randint(0,255)
    green = random.randint(0,255)
    blue = random.randint(0,255)
    return(red,green,blue)

joe = turtle.Turtle()
wn = turtle.Screen()
wn.bgcolor("gray99")
wn.colormode(255)
joe.pencolor(randomColor())
turtle.tracer(0)
g = 2

for i in range(100):
    joe.pencolor(randomColor())
    for i in range(200):
        joe.forward(g)
        joe.right(120)
        g = g + 1







