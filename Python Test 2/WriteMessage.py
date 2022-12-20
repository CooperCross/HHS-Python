# WriteMessage.py
# Cooper Cross
# 11/22/19

import turtle

joe = turtle.Turtle()
wn = turtle.Screen()
joe.hideturtle()

def getInput():
    bgColor = input("Background color: ")
    wn.bgcolor(bgColor)
    message = input("Message: ")
    fontName = input("Font: ")
    fontSize = int(input("Font Size: "))
    color1 = input("First Color: ")
    color2 = input("Second Color: ")
    writeMessage(joe,message,color1,color2,fontName,fontSize)

def moveTurtle(turt):
    xCoor = int(input("X coordinate: "))
    yCoor = int(input("Y coordinate: "))
    turt.pu()
    turt.goto(xCoor,yCoor)

def writeMessage(turt,message,color1,color2,fontName,fontSize):
    moveTurtle(turt)
    for i in range(len(message)):
        if i % 2 == 0:
            turt.pencolor(color1)
        else:
            turt.pencolor(color2)
        turt.write(message[i],True,align="left",font=(fontName,fontSize,"bold"))

getInput()
