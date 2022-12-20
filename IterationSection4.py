# IterationSection4.py
# Cooper Cross
# 11/15/19

import image
img = image.Image("joemama.gif")

newimg = image.EmptyImage(img.getWidth(), img.getHeight())
win = image.ImageWin()

for col in range(img.getWidth()):
    for row in range(img.getHeight()):
        p = img.getPixel(col, row)
        R = p.getRed()
        G = p.getGreen()
        B = p.getBlue()
        newR = int((R * 0.393 + G * 0.769 + B * 0.189))
        if newR > 254:
            newR = 255
        newG = int((R * 0.349 + G * 0.686 + B * 0.168))
        if newG > 254:
            newG = 255
        newB = int((R * 0.272 + G * 0.534 + B * 0.131))
        if newB > 254:
            newB = 255

        newpixel = image.Pixel(newR, newG, newB)

        newimg.setPixel(col, row, newpixel)

newimg.draw(win)

