# CS 115 Spring 2022 - Project 1 Key
# Author: Duong Hoang
# Section: 003
# Email: duong.hoang@uky.edu

'''
    Purpose: calculate the number of dies per wafer
    Pre-cond: wafer's diameter (mm, float), die's area (mm^2, float)
    Post-cond: error message for invalid die's area, 
            else output the number of dies per wafer (int)

'''

from math import floor, sqrt, pi

# main function
def main():
    # display introductoty message
    print('--- Wafer Fabrication Calculations ---')

    # ask for wafer's diameter and die's area (floats)
    wafer_diameter = float(input('What is the diameter of the wafer? (mm) '))
    die_area = float(input('What is the area of a single die? (mm^2) '))
    print()

    # if die area is less than or equal to zero
    if die_area <= 0: 
        # output error message
        print('Impossible die area value. No dies possible.')
    else:
        # calculate wafer's area = pi * r**2 and r = d/2
        wafer_area = pi * (wafer_diameter / 2)**2

        # calculate number of dies per wafer
        dies_per_wafer = floor(wafer_area / die_area - pi * wafer_diameter / sqrt(2 * die_area))

        # output message
        print('From a wafer with area {:.2f} square millimeters'.format(wafer_area))
        print('you can cut', dies_per_wafer, 'dies.')
        print("This does not take into account defective dies, alignment markings and test sites on the wafer's surface.")

main()