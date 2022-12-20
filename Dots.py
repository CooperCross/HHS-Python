# Dots.py
# Cooper Cross
# 11/19/2019

import random, turtle

joe = turtle.Turtle()
joe.ht()

def getDotNum():
    dnumber = int(input("Enter number of dots: "))
    return dnumber

def getDotInfo(turt):
    dsize = int(input("Enter dot size: "))
    dcolor = input("Enter dot color: ")
    drawDot(turt,dsize,dcolor)

def moveTurtle(turt):
    x = random.randint(-350,350)
    y = random.randint(-350,350)
    turt.pu()
    turt.goto(x,y)
    turt.pd()

def drawDot(turt,dsize,dcolor):
    moveTurtle(turt)
    turt.dot(dsize,dcolor)

for i in range(getDotNum()):
    getDotInfo(joe)

        
