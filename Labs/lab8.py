# Lab 8 Key
# Author:  Duong Hoang
# Email:  duong.hoang@uky.edu
# Section: 003

'''
    Purpose: play a game using graphics, guess where a hidden point is
    Pre-cond:  clicks from user
    Post-cond:  number of guesses taken, distance from click to hidden point, winning message

'''

# Import libraries
from graphics import *
import random

# Initialize
WINDOW_SIZE = 600

def distance (pt1, pt2):
    #purpose: calculate the distance between 2 graphics Points
    #pre-conditions: two Point objects
    #post-conditions: returns distance using distance formula
    return ((pt1.getX() - pt2.getX())**2 + (pt1.getY() - pt2.getY())** 2) ** 0.5


def drawPoint(pt, color, win):
    #purpose: draw a Circle of radius 3 at location given by pt with the color specified on the GraphWin win
    #pre-conditions: pt is a Point object which acts as center of circle, color is string, win is GraphWin object used to draw on 
    #post-conditions: a colored Circle of radius 3 is drawn on win, center at location given by pt
    c = Circle(pt, 3)
    c.setFill(color)
    c.draw(win)

def main():
    # Build a graphics window, size is your choice.
    win = GraphWin('game', WINDOW_SIZE, WINDOW_SIZE)
    # Use random numbers to choose a location on the window. Use them to build a Point, but don't draw it YET!
    rand_pt = Point(random.randint(0, WINDOW_SIZE), random.randint(0, WINDOW_SIZE))
    # Use a Text object to tell the user to click on the window.
    prompt = Text(Point(WINDOW_SIZE/2, WINDOW_SIZE/2), 'click to guess where the mystery point is')
    prompt.draw(win)
    # Get the user's guess by getting the Point that they click on.
    click = win.getMouse()
    # Draw a red circle at the point they guessed USE GIVEN FUNCTION
    drawPoint(click, 'red', win)
    # Initialize a counter for the guesses, using 1 (already made 1 guess)
    guess_ct = 1
    # Use a Text object to display the counter with a label (draw it)
    guesses = Text(Point(WINDOW_SIZE/2, WINDOW_SIZE * 4/5), 'guesses ' + str(guess_ct))
    guesses.draw(win)
    # Get the distance from the user's guess to the mystery point. USE GIVEN FUNCTION
    guess_distance = distance(rand_pt, click)
    # Make a Text object with the label "Distance" and draw it. Don't put a number in it yet.
    current_distance = Text(Point(WINDOW_SIZE/2, WINDOW_SIZE * 9/10), 'distance')
    current_distance.draw(win)
    # While the integer result of this distance is greater than 10,
    while guess_distance > 10 and guess_ct < 15:
        # use setText to output the distance (cast to integer) to the screen with label
        current_distance.setText('distance ' + str(int(guess_distance)))
        # get another guess from user
        click = win.getMouse()
        # draw a red circle at the point they guessed USE GIVEN FUNCTION
        drawPoint(click, 'red', win)
        # count the guess
        guess_ct += 1
        # update the displayed counter
        guesses.setText('guesses ' + str(guess_ct))
        # find the distance between the new guess and the mystery point USE GIVEN FUNCTION
        guess_distance = distance(rand_pt, click)
    # Report that the user found the mystery point
    if guess_distance <= 10:
        prompt.setText('YOU GOT IT!!\nclick to close')
    else:
        prompt.setText("you couldn't find the point within 15 guesses\nclick to close")
    # Draw a green circle where the mystery point is - USE GIVEN FUNCTION
    drawPoint(rand_pt, 'green', win)
    # Get another click so program will pause
    win.getMouse()
    # close window
    win.close()

main()

'''
Test cases:
A.  draws red circle where clicked, outputs guess counter, draws green circle where mystery point is,
    reports "you got it, click to close", gets click, closes window
B.  draws red circle, outputs guess counter and distance to mystery point, adds 1 to guess counter, waits for next user click

'''