# IterationSection1.py
# Cooper Cross
# 11/7/19

import random
import turtle

def isInScreen(w,t):
    leftBound = - w.window_width() / 2
    rightBound = w.window_width() / 2
    topBound = w.window_height() / 2
    bottomBound = -w.window_height() / 2

    turtleX = t.xcor()
    turtleY = t.ycor()

    stillIn = True
    if turtleX > rightBound or turtleX < leftBound:
        stillIn = False
    if turtleY > topBound or turtleY < bottomBound:
        stillIn = False

    return stillIn

t = turtle.Turtle()
wn = turtle.Screen()

a = [0,60,120,180,240,300]
    

while isInScreen(wn,t):
    coin = random.randrange(0, 2)
    if coin == 0:
        t.left(random.choice(a))
    else:
        t.right(random.choice(a))

    t.forward(20)
