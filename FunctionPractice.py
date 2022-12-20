# FunctionPractice.py
# Cooper Cross
# 9/26/19
# This will draw a grid of squares.

import turtle, random

sideLength = int(input("Input length of side: "))
joe = turtle.Turtle()
joe.pensize(3)
joe.hideturtle()
turtle.tracer(0)
wn = turtle.Screen()
wn.bgcolor("Sky Blue")
wn.colormode(255)
y = 200

#takes two arguments (turtle,length) and it's non-fruitful
def drawSquare(turt,length):
    turt.pencolor(randomColor()) #calls function from within a function
    turt.fillcolor(randomColor())
    turt.begin_fill()
    for i in range(4):
        turt.forward(length)
        turt.right(90)
    turt.end_fill()

#non-fruitful - doesn't return anything
def moveTurtle(turt,x,y):
    turt.penup()
    turt.goto(x,y)
    turt.pendown()
    

#fruitful - it returns a random color
def randomColor():
    red = random.randint(0,255)
    green = random.randint(0,255)
    blue = random.randint(0,255)
    return(red,green,blue)

#calling functions
drawSquare(joe,sideLength)
moveTurtle(joe,-200,-100)
drawSquare(joe,sideLength/2)

#grid of squares
moveTurtle(joe,-200,y)
#nested for loop
for row in range(1920):               #change row count
    for column in range(1080):        #change column count
        drawSquare(joe,1)           #change size of squares in grid
        joe.forward(1)
    y = y - 1
    moveTurtle(joe,-200,y)
