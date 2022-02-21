# Lab 3 Key
# Author:  Duong Hoang
# Email:  duong.hoang@uky.edu
# Section: 003
'''
    Purpose: calculate the perimeter and area of the triangle described by 3 given points
    Pre-conditions (input): 3 Pairs of Point Coordinates (int)
    Post-conditions (output): Perimeter (float, 3 decimals), Area (float, 3 decimals)
'''
import math

def main():
    #1. Print title
    print("Triangle Calculator\n")

    #2. Get 6 inputs from user (x,y,x,y,x,y)
    x1 = int(input("Enter x1: "))
    y1 = int(input("Enter y1: "))
    x2 = int(input("Enter x2: "))
    y2 = int(input("Enter y2: "))
    x3 = int(input("Enter x3: "))
    y3 = int(input("Enter y3: "))

    #3. Calculate the distances between each pair of points (lengths of sides)
    distance_12 = math.sqrt((x1 - x2)**2 + (y1 - y2)**2)
    distance_23 = math.sqrt((x2 - x3)**2 + (y2 - y3)**2)
    distance_31 = math.sqrt((x3 - x1)**2 + (y3 - y1)**2)

    #4. Calculate the perimeter, which equals the sum of the length of the 3 sides of the triangle
    perimeter = distance_12 + distance_23 + distance_31

    #5. Calculate the area
    semiPerimeter = perimeter / 2
    area = math.sqrt(semiPerimeter * (semiPerimeter - distance_12) * (semiPerimeter - distance_23) * (semiPerimeter - distance_31))

    # Output
    print()
    print("The perimeter of the triangle is {:.3f}".format(perimeter))
    print("The area of the triangle is {:.3f}".format(area))
    
main()

'''
Test Cases:
A. 21.656, 4.000
B. 16.719, 11.000
C. 199992.006, 245552.000
D. 3.414, 0.500
E. 0.000, 0.000
F. 5.657, 0.000

'''