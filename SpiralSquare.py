# SpiralSquare.py
# Cooper Cross
# 9/20/19

b = 50
import turtle
joe = turtle.Turtle()
joe.pencolor("gray99")
joe.speed(11)
wn = turtle.Screen()
wn.bgcolor("gray1")

for i in range(50):
    joe.forward(b)
    joe.left(90)
    b = b + 20
    
