# Lab 5 Key
# Author:  Duong Hoang
# Email:  duong.hoang@uky.edu
# Section: 003

'''
    Purpose: calculate a student's GPA for a semester's worth of classes
    Pre-cond: number of classes (int), then letter grade (str, A-E) 
                and number of credit hours (float) for each class
    Post-cond: total quality points, total credit hours, GPA (all float, 2 decimals),
                and message about their status if applicable

'''

def main():
    # print title
    print('Quality Points, GPA and Classification\n')

    # initialize total quality points and total credit hours
    total_quality_points = 0
    total_credit_hours = 0

    # ask user for number of classes they took
    num_classes = int(input('Input number of classes for this student: '))

    # for each class
    for i in range(num_classes):
        # input letter grade and credit hours
        letter_grade = input('Letter grade? ')
        credit_hours = float(input('Credit hours? '))

        # convert letter grade to quality points using if/elifs (control structure)
        if letter_grade == 'A' or letter_grade == 'a': quality_point = 4
        elif letter_grade == 'B' or letter_grade == 'b': quality_point = 3
        elif letter_grade == 'C' or letter_grade == 'c': quality_point = 2
        elif letter_grade == 'D' or letter_grade == 'd': quality_point = 1
        elif letter_grade == 'E' or letter_grade == 'e': quality_point = 0
        else:
            print(' << Invalid grade entered, no quality points given >> ')
            quality_point = 0

        # add quality points * credit hours to total_quality_points
        total_quality_points += quality_point * credit_hours
        # add credit hours to total_credit_hours
        total_credit_hours += credit_hours

    # if total_credit_hours is not 0, 
    # divide total_quality_points by total_credit_hours to get gpa 
    if total_credit_hours != 0: gpa = total_quality_points / total_credit_hours
    # otherwise gpa is a 0
    else: gpa = 0
    
    # output total_quality_points, total_credit_hours and gpa (2 decimal places)
    print()
    print('Total Quality Points {:.2f}'.format(total_quality_points))
    print('Total Credit Hours {:.2f}'.format(total_credit_hours))
    print('Grade Point Average = {:.2f}'.format(gpa))

    # check gpa for special cases: probation and Dean's list using if/elif (control structures)
    if gpa > 3.5 and total_credit_hours >= 12:
        print("Dean's List")
    elif gpa < 2.0:
        print('Academic Probation')

main()

'''
Test cases:
A.  Total Quality Points 25.00
    Total Credit Hours 13.00
    Grade Point Average = 1.92
    Academic Probation

B.  Total Quality Points 49.50
    Total Credit Hours 13.00
    Grade Point Average = 3.81
    Dean's List

C.  Total Quality Points 18.00
    Total Credit Hours 10.00
    Grade Point Average = 1.80
    Academic Probation

D.  Total Quality Points 27.00
    Total Credit Hours 9.00
    Grade Point Average = 3.00

E.  Total Quality Points 8.00
    Total Credit Hours 4.00
    Grade Point Average = 2.00

F.  Total Quality Points 9.00
    Total Credit Hours 6.00
    Grade Point Average = 1.50
    Academic Probation

G.  Total Quality Points 0.00
    Total Credit Hours 0.00
    Grade Point Average = 0.00
    Academic Probation

'''