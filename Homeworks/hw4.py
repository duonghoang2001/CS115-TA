# CS 115 Spring 2022 - Homework 4 Key
# Author: Duong Hoang
# Section: 003
# Email: duong.hoang@uky.edu

'''
Purpose:  offer the user a choice of food items, calculate total bill
Pre-conditions:  user enters 5 or 6 y's or n's depending on desired items (strings)
Post-conditions:  prompts for choices, total bill before (float) and after tip, (float)
   and parting message.
'''

### Implementation ###
def main():

    # name of food vendor
    print("Welcome to Keen Concessions")

    # give user instructions of expected inputs
    print("Please answer each question with y or n\n")

    # initialize total bill to zero
    total_bill = 0

    # ask first choice (grilled cheese sandwich)
    cheese_sandwich = input("Would you like a grilled cheese sandwich? ")
    # if the user desired the item,
    if cheese_sandwich == 'y': 
        # add price to total bill
        total_bill += 4.49

    # ask second choice (nachos)
    nachos = input("Would you like a serving of nachos? ")
    # if the user desired the item,
    if nachos == 'y': 
        # add price to total bill
        total_bill += 5.49

    # ask third choice (fish sandwich)
    fish_sandwich = input("Would you like a fish sandwich? ")
    # if the user desired the item,
    if fish_sandwich == 'y': 
        # add price to total bill
        total_bill += 6.99

    # ask fourth choice (hamburger)
    hamburger = input("Would you like a Hamburger? ")
    # if the user desired the item,
    if hamburger == 'y': 
        # ask additional choice (cheeseburger)
        cheeseburger = input("Would you like cheese on that? ")
        # if the user desired the additional item,
        if cheeseburger == 'y':
            # add additional price to total bill
            total_bill += 8.99
        # if not desired,
        else:
            # add original price to total bill
            total_bill += 7.99
    
    # ask fifth choice (hot dog)
    hot_dog = input("Would you like a hot dog? ")
    # if the user desired the item,
    if hot_dog == 'y':
        # add price to total bill
        total_bill += 2.99

    # output blank line
    print()

    # output total bill before tip
    print("The total for your food is ${:.2f}".format(total_bill))

    # calculate total bill with 20% tip (100% + 20% = 120% = 120/100 = 1.2)
    total_bill *= 1.2

    # output total bill with tip
    print("The total with 20% tip is ${:.2f}".format(total_bill))

    # print closing ment
    print("We appreciate your business!")

main()

'''
Test Cases:
A. $5.49, $6.59
B. $7.99, $9.59
C. $16.97, $20.36
D. $0.00, $0.00
E. $28.95, $34.74
'''