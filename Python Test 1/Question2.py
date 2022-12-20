# Question2.py
# Cooper Cross
# 10/10/19

import math

radius = input("Please enter the radius of the base of the cylinder: ")
height = input("Please enter the height of the cylinder: ")
radius = (float(radius))
height = (float(height))
surfaceArea = ((2 * math.pi * radius) * (height + radius))
print("The area of the right cylinder = "+str(surfaceArea))
