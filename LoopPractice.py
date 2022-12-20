# LoopPractice.py
# Cooper Cross
# 10/31/19

import turtle
import time
import random

joe = turtle.Turtle()
wn = turtle.Screen()
x = 0
y = 0
done = False

colors = ["red","blue","yellow","green","purple"]

def makeSquare(turt,size,color):
    turt.fillcolor(color)
    turt.begin_fill()
    for i in range(4):
        turt.forward(size)
        turt.left(90)
    turt.end_fill()

for bgColor in (["coral","orange","violet","SeaGreen1","deep pink"]):
    wn.bgcolor(bgColor)
    for color in (colors):
        makeSquare(joe,20,color)
        joe.forward(20)
    joe.penup()
    y = y + 20
    joe.goto(0,y)
    joe.pendown()

while(done == False):
    userDone = input("Do you want to write a message (y or n): ")
    if userDone.lower() == "y":
        message = input("Input a message: ")
        joe.hideturtle()
        joe.penup()
        joe.pencolor(random.choice(["MediumPurple","peach puff","red2","light sea green","dark orange"]))
        joe.write(message,True,align="center",font=("Comic Sans MS",30,"bold"))
        time.sleep(10)
        joe.clear()
    else:
        done = True

for i in range(10,1,-1):
    for j in range(i,1,-1):
        color = random.choice(colors)
        makeSquare(joe,20,color)
        joe.forward(20)
    joe.penup()
    y = y - 20
    x = x + 20
    joe.goto(x,y)
    joe.pendown()
    
