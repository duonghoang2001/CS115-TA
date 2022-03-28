# Lab 9 Key
# Author:  Duong Hoang
# Email:  duong.hoang@uky.edu
# Section: 003


def time_compare(h1, m1, s1, h2, m2, s2):
    '''
        Purpose: compare two times and decide whether one time comes before the other or they are equal
        Precond 3 ints for time1 (hours, mins, secs), 3 ints for time2 (hours, mins, secs)
        Postcond: one integer, 0 if times are the same, 1 if time1 comes before time2, 2 if time1 comes after time2
    '''
    compare = 0
    if h1 > h2: compare= 2
    elif h1 < h2: compare = 1
    else:
        if m1 > m2: compare = 2
        elif m1 < m2: compare = 1
        else:
            if s1 > s2: compare = 2
            elif s1 < s2: compare = 1
    return compare

def time_print(h, m, s):
    '''
        Purpose: print out a time in a formatted way, 00:00:00
        Precond: 3 integers, hours, minutes, seconds
        Postcond: output to shell in format specified, ending with newline
    '''
    if h < 10: print('0', end='')
    print(h, end=':')
    if m < 10: print('0', end='') 
    print(m, end=':')
    if s < 10: print('0', end='')
    print(s)
    

def main():
    '''
        Purpose: compare two times provided by user, determine what relationship they have to each other
                repeating until user enters -1 (sentinel logic)
        Pre-cond: 6 integers, representing 2 times (hours, minutes, seconds)  
                assume between 0 and 23 for hours, 0 to 59 for minutes and seconds
        Post-cond: message about times' relationship, "the same", "time1 is before time2", "time1 is after time2"
    '''
    # print header
    print('Mastery is not a function of genius or talent, but a function of time')
    print('and intense focus applied to a particular field of knowledge.\n')

    h1 = int(input('Enter first hours or -1 to stop: '))
    # while loop for sentinel logic
    while h1 != -1:
        # get other inputs
        m1 = int(input('Enter first minutes: '))
        s1 = int(input('Enter first seconds: '))
        h2 = int(input('Enter second hours: '))
        m2 = int(input('Enter second minutes: '))
        s2 = int(input('Enter second seconds: '))
        
        # print times
        print()
        print('Time 1:', end=' ')
        time_print(h1, m1, s1)
        print('Time 2:', end=' ')
        time_print(h2, m2, s2)

        # if/elif/else to report correct message about relationship
        print()
        compare = time_compare(h1, m1, s1, h2, m2, s2)
        print('Time 1 is', end=' ')
        if compare == 0: print('equal', end=' ')
        elif compare == 1: print('before', end=' ')
        else: print('after', end=' ')
        print('Time 2\n')

        # get the next hour
        h1 = int(input('Enter first hours or -1 to stop: '))

main()

'''
Test cases:
A. 1    B. 1    C. 1    D. 2    E. 2    F. 2
'''