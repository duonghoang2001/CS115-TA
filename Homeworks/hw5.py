# CS 115 Spring 2022 - Homework 5 Key
# Author: Duong Hoang
# Section: 003
# Email: duong.hoang@uky.edu

'''
    Purpose: Calculate all the Leap Years in a given inclusive range
    Pre-cond: Start and End of the range (both int)
    Post-cond: All the Leap Years (int)

'''

def main():
    # print title
    print("Leap Years within a range\n")

    # prompt user for range
    start = int(input("What is the start of the range? "))
    end = int(input("What is the end of the range? "))

    # if inputs are given in reverse order,
    if start > end:
        # reverse them
        start, end = end, start

    # calculate all the leap years
    print(f"Leap Years in range {start} to {end}\n")
    for year in range(start, end + 1): # inclusive range
        if year % 4 == 0 and year % 100 != 0: # divisible by 4 but not 100
            print(year)
        elif year % 400 == 0: # divisible by 400, leap year
            print(year)
  

main()

'''
Test Cases:
A. Not divisible by 4: 
B. Divisible by 4 but not 100: 2096 -> leap year, 2100 -> not leap year
C. Divisible by 400: 2000 -> leap year
D. Reverse inputs

'''