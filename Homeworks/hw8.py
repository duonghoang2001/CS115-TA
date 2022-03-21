# CS 115 Spring 2022 - Homework 8 Key
# Author: Duong Hoang
# Section: 003
# Email: duong.hoang@uky.edu

'''
    Purpose: input 2 numbers from the user (positive, integer) and determine
            whether they are friendly or not
    Pre-cond:  2 integers greater than 0
    Post-cond: whether they are friendly or not

'''

def factors(num):
    '''
    purpose: calculates the sum of an integer number's factors 
    pre-cond: one integer greater than zero
    post-cond: integer sum of the factors of the parameter (int)
    '''
    # initialize sum of the factors
    factors_sum = 0

    # loop through all the possible factors
    for i in range(1, num + 1):
        # if i is a factor of the parameter
        if num % i == 0:
            # add i to sum of the factors
            factors_sum += i
    #print(factors_sum)
    return factors_sum

def friendly(num1, num2):
    '''
    purpose: determine whether two numbers are friendly
    (the ratio of the sum of a number's factors to the number is found
    for each parameter, the ratios are compared, if equal, then friendly)
    pre-cond: two integer greater than zero
    post-cond: whether they are friendly or not (bool)
    '''
    return factors(num1) / num1 == factors(num2) / num2
        
def main():
    # get first input integer and validate whether input is positive
    num1 = int(input('Enter first number: '))
    # while first input is invalid (smaller or equal to 0)
    while num1 <= 0:
        # output invalid message
        print('Please enter a number greater than zero')
        # prompt user for new input
        num1 = int(input('Enter first number: '))

    # get second input integer and validate whether input is positive
    num2 = int(input('Enter second number: '))
    # while second input is invalid (smaller or equal to 0)
    while num2 <= 0:
        # output invalid message
        print('Please enter a number greater than zero')
        # prompt user for new input
        num2 = int(input('Enter second number: '))

    # output result whether the two inputs are friendly or not
    print()
    if friendly(num1, num2):
        print('{} and {} are friendly'.format(num1, num2))
    else:
        print('{} and {} are not friendly'.format(num1, num2))

main()

'''
Test cases:
A. 31
B. 252
C. True
D. False
E. 30 and 140 are friendly
F. 120 and 150 are not friendly
'''