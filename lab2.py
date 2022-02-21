# Lab 2 Key
# Author:  Duong Hoang
# Email:  duong.hoang@uky.edu
# Section: 003
'''
    Purpose: convert feet to inches, using fact that there are 12 inches in 1 foot
    Pre-conditions (input): Principal (float), Number of Years (int), 
                            Interest Rate per Year (APR, float)
    Post-conditions (output): Payment (float, 2 decimals)
'''

### Implementation ###
import math

def main():
    #1. Print title
    print("Payment Calculator\n")

    #2. Get inputs from user (principal, number years, interest rate)
    principal = float(input("Enter initial amount of loan: "))
    years = int(input("Number of years to pay back loan: "))
    interest_rate = float(input("Interest rate per year (%): "))

    #3. Convert rate to percent and to monthly rate
    monthly_rate = interest_rate / 100 / 12

    #4. Convert years to months
    months = years * 12

    #5. Find the payment using the given formula
    payment = principal * monthly_rate * (1+monthly_rate)**months / ((1+monthly_rate)**months - 1)

    #6. Display the payment with only two decimal places
    print(f"Payment is ${payment:.2f}")

main()

'''
Test cases:
A. (220., 3, 20.5): $8.23
B. (15000, 4, 10): $380.44
C. (1e9, 5, 10): $21247044.71
D. (1, 1, 1): $0.08
E. (0, 0, 0): ZeroDivisionError: float division by zero 
                (the denom is (1-0)**0-1 = 1-1 = 0)
'''