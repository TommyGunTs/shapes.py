"""
*******************************************************
CS 1026A - Assignment 1 - Shapes and Sizes Calculator
Code by: Thomas Tyndorf
Student ID: ttyndor3
File created: September 27th, 2024
*******************************************************
This program is used to calculate the perimeter and area of certain shapes provided on a list.
The Shapes included are the circle, triangle, rectangle, trapezoid, and hexagon.
In the case that you type a shape not in this list an error message will show.
"""

import math
#1st step in worksheet
shape = input("Enter the name of a shape: ")
shape = shape.lower()

#Only shapes that can be calculated and any wrong shapes include an error message
shapes = ["rectangle" or "triangle" or "circle" or "trapezoid" or "hexagon"]


if shape == "rectangle":                                 #Rectangle part
    width = float(input("Enter the width: "))
    height = float(input("Enter the height: "))
#make sure for no negative numbers and any in the future
    if width <= 0 or height <=0:
        print("Invalid value, Enter Positive Numbers")         #Explain the reason for the error
    else:                                                      #so it doesn't happen again
        perimeter = 2 * height + 2 * width
        area = height * width
#top is solving formula^^^
#bottom result message
        print("Shape: Rectangle")
        print("Perimeter:", round(perimeter, 2))
        print("Area:", round(area, 2))
elif shape =="triangle":                                    #Triangle part
    base = float(input("Enter the base: "))               #Base is the bottom side so make sure
    height = float(input("Enter the Height: "))           # it's bigger than side
    sideA = float(input("Enter sideA: "))
    sideC = float(input("Enter sideC: "))

    if base <=0 or height <=0 or sideA <=0 or sideC <=0:
        print("Invalid value, Enter Positive Numbers")
    else:
        perimeter = base + sideA + sideC
        area = (base * height) / 2
#reason for "import math" don't delete top^^ -- Same for pi command
        print("Shape: Triangle")
        print("Perimeter:", round(perimeter, 2))
        print("Area:", round(area, 2))
elif shape == "circle":                               #Circle part
    radius = float(input("Enter the radius: "))

    if radius <= 0:
        print("Invalid value, Enter Positive Numbers")
    else:
        perimeter = 2 * math.pi * radius
        area = math.pi * radius * radius

        print("Shape: Circle")
        print("Perimeter:", round(perimeter, 2))
        print("Area:", round(area, 2))
elif shape == "trapezoid":                             #Trapezoid part
    top = float(input("Enter top: "))
    bottom = float(input("Enter bottom: "))
    left = float(input("Enter left: "))
    right = float(input("Enter right: "))
    height = float(input("Enter height: "))

    if top <= 0 or bottom <= 0 or left <= 0 or right <= 0 or height <= 0:
        print("Invalid value, Enter Positive Numbers")
    else:
        perimeter = top + bottom + left + right
        area = (top + bottom) / 2 * height

        print("Shape: Trapezoid")
        print("Perimeter:", round(perimeter, 2))
        print("Area:", round(area, 2))
elif shape == "hexagon":                       #Hexagon part
    side = float(input("Enter the side length: "))

    if side <=0:
        print("Invalid value, Enter Positive Numbers")
    else:
        perimeter = 6 * side
        area = ((3 * math.sqrt(3)) / 2) * (side * side)

        print("Shape: Hexagon")
        print("Perimeter:", round(perimeter, 2))
        print("Area:", round(area, 2))
else:
    print("Invalid Shape")
