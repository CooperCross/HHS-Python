# AdditionalQuestionPythonTest2Practice.py
# Cooper Cross
# 11/21/19

import turtle
import random

wn = turtle.Screen()
wn.colormode(255)

def randomColor():
    red = random.randint(0,255)
    green = random.randint(0,255)
    blue = random.randint(0,255)
    return(red,green,blue)
    
runner = turtle.Turtle()

def move(x,y):
    direction = random.randint(1,2)
    angle = 120
    if direction == 1:
        runner.left(angle)
    else:
        runner.right(angle)
    runner.fd(50)
        
turtle.onscreenclick(move)
