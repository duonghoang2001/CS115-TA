# Lab 1 Key
# Author:  Duong Hoang
# Email:  duong.hoang@uky.edu
# Section: 003
'''
  Purpose: 
      convert feet to inches, using fact that there are 12 inches in 1 foot
  Pre-conditions (input): 
      number of feet (floating point)
  Post-conditions (output): 
      number of inches, floating point with 2 decimals rounded
'''

def main():
# Design and implementation

    #  1.  Output a message to identify the program, and a blank line
    print("Conversion of feet to inches")
    print()

    #  2.  Input amount of feet from user
    feet = float(input("How many feet? "))

    #  3.  Calculate number of inches
    # 12 inches in one foot
    inches = feet * 12

    #  4. Output resulting inches and given number of feet
    print()
    print(feet, "feet is {:.2f} inches".format(inches))

main()
# end of program file
# 

'''
1. Syntax Error: Missing closing parenthesis on line 22
2. Error Message:
    Traceback (most recent call last):
    File "c:\\Users\\hhduo\\TA_CS115\\Lab\\lab1.py", line 22, in <module>
        feet = float(input("How many feet? ")
    Syntax Error: invalid syntax. Perhaps you forgot a comma?: <string>, line 22, pos 18
3. Fix: Add 1 missing closing parenthesis to the ens of line 22 
4. 12 inches = 1 foot. So inches = feet * 12 instead of +
5. The Semantic Error is on line 26
6. Fix: Change + to * in the equation
'''

