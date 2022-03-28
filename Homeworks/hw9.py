# CS 115 Spring 2022 - Homework 9 Key
# Author: Duong Hoang
# Section: 003
# Email: duong.hoang@uky.edu

'''
    Purpose: present the user with a box in a graphics window, ask them to click 
            inside the box, count and report all clicks until they do, ask for 
            another click and close the window
    Pre-conditions:  user clicks
    Post-conditions: prompts for user to click, box with label, click counter 
                    and click to close at the end
'''
from graphics import *

def inbetween (pt1, pt2, pt3):
    '''
    Purpose:  detect whether a Point pt2 is between Points pt1 and pt3
       assumes that pt1 is to the left of pt3 (x of pt1 is <= x of pt3)
       and that pt1 is above pt3 (y of pt1 is <= y of pt3)
    Preconditions:  pt1 and pt3 are the boundary Points, forming a rectangle.
       pt2 is the Point which is being tested for "betweenness".
    Postconditions:
       returns True if the Point pt2 lies in the rectangle formed by pt1 and pt3.
          This includes pt2 being exactly ON one side of the rectangle.
       returns False if this is not true.  
    '''
    between = False
    if (pt1.getX() <= pt2.getX() <= pt3.getX()) and (pt1.getY() <= pt2.getY() <= pt3.getY()):
           between = True
    return between

def main():
    # prepare window, at least 500 by 500
    win = GraphWin('Counter', 500, 500)
    # make 2 variables, x and y for the upper left corner of the Yes box (pick your locations as you like)
    x = 120
    y = 120
    # make a variable for the size of the box (assume it is going to be square) (length of the side)
    box_size = 50
    # create 2 Points, for the upper left and lower right corners of the Yes box 
    #   use the variables in the previous lines to calculate where the lower right point will be
    upper_left = Point(x, y)
    lower_right = Point(x + box_size, y + box_size)
    # draw a box using those two 
    box = Rectangle(upper_left, lower_right)
    box.draw(win)
    # make it a color (your choice)
    box.setFill('lightpink')
    # Label it Yes.  The label should be centered in the box.
    #   centered by calculating middle of box
    box_label = Text(Point(x + box_size / 2, y + box_size / 2), 'YES')
    box_label.draw(win)
    # Give the user a message "Click anywhere, ending in the box".
    click_prompt = Text(Point(250, 250), 'click anywhere, ending in the box')
    # Draw the message
    click_prompt.draw(win)
    # Get and store the user's mouse click. It's a Point object!
    #   using getMouse()
    click_pt = win.getMouse()
    # Initialize a click counter and draw it
    click_counter = 1
    counter = Text(Point(100, 30), 'clicked ' + str(click_counter) + ' times')
    counter.draw(win)
    # while the Point the user clicked is NOT in the box
    #   (You MUST call inbetween (below) in the condition of the while loop!)
    while not inbetween(upper_left, click_pt, lower_right):
        # let the user click again
        click_pt = win.getMouse()
        # add one to the click counter
        click_counter += 1
        counter.setText('clicked ' + str(click_counter) + ' times')

    # tell the user to click to close
    close_prompt = Text(Point(100, 80), 'click to close')
    close_prompt.draw(win)
    # close the window and exit properly
    win.getMouse()
    win.close()

main()