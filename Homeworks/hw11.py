# CS 115 Spring 2022 - Homework 11 Key
# Author: Duong Hoang
# Section: 003
# Email: duong.hoang@uky.edu

'''
    Purpose: calculate payrolls for the employees of a company
    Preconditions: name (str), hours worked (float), hourly rate (float)
    Postconditions: employees (str, ascending) and their paychecks (float, 2 decimals)

'''

def main():
    # print title
    print("Payroll for the Global Thingamabob Manufacturing Company")
    # print user prompt
    print("Enter Information (Name, hours worked, hourly rate) separated by commas")
    print("Press Enter to stop Entering Employee Information")
    # initialize total payroll counter to 0
    total_pay = 0
    # initialize an empty list of employees and their paychecks
    info_lst = []
    # get user input until an Enter only is inputted
    info = input("Enter Employee Information: ")
    while info != "":
        # extract name, hours, and rate that are separated by commas
        info = info.split(",")
        # calculate pay check
        paycheck = get_paycheck(info)
        # add paycheck to total payroll
        total_pay += paycheck
        # append a pair of employee name and their paycheck to the list
        info_lst.append([info[0], paycheck])
        # get next input
        info = input("Enter Employee Information: ")
    # sort list by name in ascending order
    info_lst.sort()
    # report total payroll formatted to 2 decimal places
    print("\nTotal Payroll ${:.2f}".format(total_pay))
    # print paycheck report header
    print("\nEmployees with Paychecks")
    # report each paycheck
    for i in range(len(info_lst)):
        print("{}\t${:.2f}".format(info_lst[i][0], info_lst[i][1]))
    
def get_paycheck(info: list):
    '''
        Purpose: calculate paycheck amount
        Preconditions: a list of raw data containing name, hours worked, hourly rate (list of str)
        Postconditions: paycheck amount calculated by hours worked times hourly rate
    '''
    return float(info[1]) * float(info[2])

main()

"""
Test Cases:
A.  Total Payroll $1146.50, Carl $395.00, Jim $234.00, Martha $517.50
B.  Total Payroll $0.00

"""