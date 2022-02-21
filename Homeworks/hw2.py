# CS 115 Spring 2022 - Homework 2 Key
# Author: Duong Hoang
# Section: 003
# Email: duong.hoang@uky.edu

#Purpose:   Calculate the equivalent number of miles, feet and yards from kilometers.
#Preconditions:   number of kilometers (float)
#Postconditions:   equivalent number of miles, feet, yards (float, 3 decimals)

# Implementation
def main():
    # 1. Get needed data from the keyboard, the number of kilometers.
    kilometers = float(input("Enter kilometers: "))
    # 2. Calculate the equivalent miles.
    miles = kilometers * 0.621371
    # 3. Calculate the equivalent number of feet.
    feet = miles * 5280
    # 4. Calculate the equivalent number of yards.
    yards = feet / 3

    # 5. Print blank line
    print()
    # 6. Output the input kilometers with label and 3 places.
    print(f'{kilometers:.3f} kilometers =', end=" ")
    # 7. Output the miles with label and 3 places.
    print(f'{miles:.3f} miles')
    # 8. Output the feet with label and 3 places.
    print(f'which is {feet:.3f} feet')
    # 9. Output the yards with label and 3 places.
    print(f'which is {yards:.3f} yards')

main()

'''
Test cases:
A. 10 km = 6.214 miles = 32808.389 feet = 10936.130 yards
B. 12.5 km = 7.767 miles = 41010.486 feet = 13670.162 yards
C. 0 km = 0 miles = 0 feet = 0 yards
D. 2e4 km (20000.000 kilometers) = 12427.420 miles = 65616777.600 feet = 21872259.200 yards
'''