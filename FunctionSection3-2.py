# FunctionsSection3-2
# Cooper Cross
# 11/12/19

import turtle

wn = turtle.Screen()
jojo = turtle.Turtle()
jojo.pencolor("hotpink")
jojo.fillcolor("hotpink")
wn.bgcolor("lightgreen")
jojo.speed(11)

angle = 360 / 15

jojo.begin_fill()

for i in range(15):
    jojo.right(angle)
    jojo.forward(120)

    jojo.right(180)
    jojo.forward(120)
    jojo.right(180)

jojo.turtlesize(7,7,7)
jojo.shape("circle")
jojo.end_fill()

wn.exitonclick()
