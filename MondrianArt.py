# MondrianArt.py
# Cooper Cross
# 11/13/19

import random, turtle
t = turtle.Turtle()
wn = turtle.Screen()

turtle.tracer(0)

wn.bgcolor("black")

amountOfSquares = input("Amount of squares: ")
rangeLength = input("Enter max width: ")
rangeHeight = input("Enter max height: ")

amountOfSquares = int(amountOfSquares)
rangeLength = int(rangeLength)
rangeHeight = int(rangeHeight)

turtle.colormode(255)

def randomColor():
    R = random.randint(0, 255)
    G = random.randint(0, 255)
    B = random.randint(0, 255)
    return(R,G,B)

def drawSquare(turt):
    for i in range(amountOfSquares):
        x = random.randint(-500, 500)
        y = random.randint(-500, 500)
        turt.penup()
        turt.goto(x, y)
        turt.pendown()
        q = random.randint(10, rangeLength)
        w = random.randint(10, rangeHeight)
        turt.fillcolor(randomColor())
        turt.begin_fill()
        for i in range(2):
            turt.forward(q)
            turt.left(90)
            turt.forward(w)
            turt.left(90)
        turt.end_fill()
drawSquare(t)

