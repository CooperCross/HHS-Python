# Question2Volume.py
# Cooper Cross
# 10/10/19

import math

radius = input("Please enter the radius of the base of the cylinder: ")
height = input("Please enter the height of the cylinder: ")
radius = (float(radius))
height = (float(height))
volume = ((math.pi * radius)*(math.pi * radius)*height)
print("The volume of your cylinder is: "+str(volume))

