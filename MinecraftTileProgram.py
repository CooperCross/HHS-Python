# MinecraftTileProgram
# Cooper Cross
# 9/30/19

import turtle
jojo = turtle.Turtle()
wn = turtle.Screen()
turtle.tracer(0)
jojo.pencolor("gray53")
jojo.fillcolor("gray53")

jojo.penup()
jojo.goto(-50,50)
jojo.pendown()
jojo.begin_fill()

for i in range(4):
    jojo.forward(100)
    jojo.right(90)

jojo.end_fill()
jojo.penup()
jojo.goto(-43.75,-43.75)
jojo.pencolor("green2")
jojo.fillcolor("green2")
jojo.begin_fill()

for i in range(4):
    jojo.forward(12.5)
    jojo.left(90)
    
jojo.end_fill()

jojo.penup()
jojo.forward(37.5)
jojo.left(90)
jojo.forward(25)

jojo.begin_fill()
for i in range(4):
    jojo.forward(12.5)
    jojo.right(90)

jojo.end_fill()
jojo.penup()

jojo.forward(18.75)
jojo.right(90)
jojo.begin_fill()

for i in range(4):
    jojo.forward(12.5)
    jojo.left(90)

jojo.end_fill()
jojo.left(90)
jojo.penup()
jojo.forward(6.25)
jojo.left(90)
jojo.begin_fill

for i in range(4):
    jojo.forward(12.5)
    jojo.right(90)

jojo.end_fill()

jojo.penup()
jojo.forward(37.5)
jojo.right(90)
jojo.forward(25)

jojo.begin_fill()
for i in range(4):
    jojo.forward(12.5)
    jojo.right(90)

jojo.end_fill()
