# CS 115 Spring 2022 - Homework 3 Key
# Author: Duong Hoang
# Section: 003
# Email: duong.hoang@uky.edu

# Purpose: calculate the height of a tree using trigonometric function
# Pre-cond: angle of elevation (deg, float), distance to tree (ft, float), 
#           height of observer to eyes (ft, float)
# Post-cond: height of tree (ft, float, 2 decimals)


### Implementation ###

# use math library for radians function needed to convert input angle to radians
# and tan function used to calculate height
from math import radians, tan

def main():

    # print title and blank line
    print("Finding the height of a tree\n")

    # get 3 input values, angle of elevation, distance to base and height of observer
    angle_deg = float(input("Angle of elevation to top of tree (deg): "))
    distance = float(input("How far to the base of the tree (ft)? "))
    eye_height = float(input("Your height up to your eyes (ft)? "))

    # convert input angle to radians
    angle_rad = radians(angle_deg)

    # calculate height of tree using formula: 
    # height = distance times tan(angle of elevation) plus height to eyes
    tree_height = distance * tan(angle_rad) + eye_height

    # report resulting height, using 2 decimals
    print(f'The height of the tree is {tree_height:.2f} feet')

main()
# end program
#

'''
Test cases:
A. (45, 50, 5): 55.00 feet
B. (75.0, 92.5, 4.9): 350.11 feet
C. (89.5, 0, 5.1): 5.10 feet
D. (-10.0, 100, 5.2): -12.43 feet
'''