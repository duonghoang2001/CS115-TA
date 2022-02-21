# CS 115 Spring 2022 - Homework 6 Key
# Author: Duong Hoang
# Section: 003
# Email: duong.hoang@uky.edu

'''
    Purpose: calculate a worker's payroll
    Pre-cond: name (string), rate (float), days (int)
    Post-cond: the total thingamabobs made (int),
                the extra pay (float, 2 decimals) if applicable,
                and the pay the person gets (float, 2 decimals)

'''


def main():
    limit = 100 

    print('Thingamabob Company Payroll')

    # get inputs
    name = input('Enter name of worker: ')
    rate = float(input('Enter the rate per thingamabob: '))
    days = int(input('How many days? '))

    # initialize accumulators
    total_products = 0

    # get input of each day
    for i in range(days):
        products = int(input('Thingamabobs produced on Day '+ str(i) +'? '))
        total_products += products
    
    # output the total thingamabobs
    print()
    print('Total thingamabobs produced:', total_products)

    # calculate the total pay
    total_pay = 0
    if total_products > limit: # if there is extra pay
        extra_pay = (total_products - limit) * 1.5 * rate
        # output extra pay
        print('Extra thingamabobs pay ${:.2f}'.format(extra_pay))
        total_pay = limit * rate + extra_pay
    else:
        total_pay = total_products * rate

    # output total pay
    print('The pay for', name, 'is ${:.2f}'.format(total_pay))

main()        


