# Lab 7 Key
# Author:  Duong Hoang
# Email:  duong.hoang@uky.edu
# Section: 003

'''
    Purpose: approximate pi using Monte Carlo method
    Pre-cond: number of darts (int)
    Post-cond: time taken to run loop (sec, min & sec if over 1 min),
                approximation of pi and the error (both floats)

'''

# Import libraries
from time import process_time       # track time performance
from random import random, seed     # randomize x and y values
from math import pi                 # actual pi value to compare


# Implementation
def main():
    seed(0) # set seed to get the same random numbers every run

    # print title
    print("Estimating pi with the Monte Carlo method\n")
    
    # prompt user for number of darts
    darts = int(input("How many darts for this simulation? "))
    print()

    # initialize counter for number of darts inside the circle
    inside_ct = 0
    # start the timer
    start = process_time()
    # for loop generate darts number of x and y random values
    for i in range(darts):
        # generate 2 random coordinates for dart
        x = random()
        y = random()
        # if the dart's coordinates satisfy: x**2 + y**2 < 1
        if x**2 + y**2 < 1:
        #if x*x + y**2 < 1:
            # increase the inside dart counter
            inside_ct += 1
    # end the timer
    end = process_time()

    # calculate time taken
    duration = end - start
    # output time taken
    print("Time taken:", duration, "seconds")
    # if the time taken is more than 1 min, output time taken in min and sec
    if duration > 60:
        duration_min = duration / 60
        duration_sec = duration % 60
        print("or", duration_min, "minutes and", duration_sec, "seconds")

    # calculate pi approximation
    # if no sarts were thrown, approximation = 0
    if darts == 0: 
        approx = 0 
    # otherwise, calculate the pi approximation
    else:
        inside_ratio = inside_ct / darts
        approx = inside_ratio * 4
    # output the approximation
    print("approximation to pi", approx)

    # calculate the difference between approximation and real pi value
    difference = pi - approx
    # output the difference
    print(pi, "-", approx, "=", difference)

main()

'''
Experimenting:
1.  No, because the coordinates are random each run, 
    so the ratio will be different and thus the approximation will be vary
2.  1 sec: 1500000, 10 sec: 15000000
3.  Running (2) on all members machines
4.  x*x is faster than x**2

'''