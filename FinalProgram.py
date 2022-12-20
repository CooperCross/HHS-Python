# FinalProgram.py
# Cooper Cross
# 1/13/2020

import turtle, random, math, image
fot = turtle.Turtle()
wn = turtle.Screen()
wn.colormode(255)
turtle.tracer(0)

def getRandomColor():
    r = random.randint(0,255)
    g = random.randint(0,255)
    b = random.randint(0,255)
    return(r,g,b)

def drawPoly(t,num_sides,side_length):
    for i in range(num_sides):
        t.fd(side_length)
        t.left(360/num_sides)
        t.color(getRandomColor())

for i in range(999):
    drawPoly(fot,10,20)
    fot.pu()
    fot.goto(random.randrange(-100,100),random.randrange(-100,100))
    fot.pd()

inq = int(input("Does this hurt your eyes? 1 if Yes, 2 if No "))

if inq == 1:
    img = image.Image("ecksdee.gif")

    newimg = image.EmptyImage(img.getWidth(), img.getHeight())
    win = image.ImageWin()

    for col in range(img.getWidth()):
        for row in range(img.getHeight()):
            p = img.getPixel(col, row)
            R = p.getRed()
            G = p.getGreen()
            B = p.getBlue()
            newR = int((R * 1 + G * 1 + B * 1))
            if newR > 254:
                newR = 255
            newG = int((R * 1 + G * 1 + B * 1))
            if newG > 254:
                newG = 255
            newB = int((R * 1 + G * 1 + B * 1))
            if newB > 254:
                newB = 255

            newpixel = image.Pixel(newR, newG, newB)

            newimg.setPixel(col, row, newpixel)

    newimg.draw(win)
else:
    
