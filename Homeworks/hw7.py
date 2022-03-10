# CS 115 Spring 2022 - Homework 7 Key
# Author: Duong Hoang
# Section: 003
# Email: duong.hoang@uky.edu

'''
   Purpose: Draw a greeting card customized with a person's name
   Preconditions: User prompts for the name on the card
   Postconditions: Display the card on graphics window (greeting, name, drawing)

'''

from graphics import *

# Design and implementation
def main():
    
    # create a 600 x 600 pink graphics window
    win = GraphWin("Happy Birthday Card", 600, 600)
    win.setBackground("light pink")
    
    # display greeting centered on top of the screen
    greeting = Text(Point(300, 100), "Happy Birthday!")
    greeting.setFace("courier")
    greeting.setSize(27)
    greeting.setFill("firebrick2")
    greeting.draw(win)
    
    # create an entry box for name on the card centered under the greeting
    pt_1 = Point(300, 180)
    entry_box = Entry(pt_1, 10)
    entry_box.setFill("snow")
    entry_box.setText("Enter Name")
    entry_box.setSize(24)
    entry_box.setTextColor("light slate blue")
    entry_box.draw(win)
   
    # display prompt click to continue
    prompt_1 = Text(Point(300, 250), "Click on the window to continue")
    prompt_1.draw(win)
    
    # get input (name) from user
    win.getMouse()
    entered_name = entry_box.getText()
    
    # display the person's name on the graphics window
    
    name = Text(pt_1, entered_name)
    name.setSize(24)
    name.setFill("light slate blue")
    name.draw(win)
    
    # undraw the entry box and prompt
    entry_box.undraw()
    prompt_1.undraw()
    
    # draw a present with mint wrapping
    x1 = 200 
    y1 = 280
    width = 200
    height = 200
    present = Rectangle(Point(x1, y1), Point(x1 + width, y1 + height))
    present.setFill("DarkSlateGray2")
    present.draw(win)
    
    # draw the blue ribbon on the present (thick blue line)
    pt_2 = Point(x1 + width / 2, y1)
    
    ribbon_1 = Line(pt_2, Point(x1 + width / 2 , y1 + height))
    ribbon_1.setWidth(10)
    ribbon_1.setFill("DodgerBlue2")
    ribbon_1.draw(win)
     
    ribbon_2 = Line(Point(x1, y1 + height / 2), Point(x1 + width, y1 + height /2))
    ribbon_2.setWidth(10)
    ribbon_2.setFill("DodgerBlue2")
    ribbon_2.draw(win)
    
    # draw a bow on top of the present
    pt_3 = Point(x1 + width / 2, y1 + 10)
    
    bow_1 = Oval(Point(220,260), pt_3)
    bow_1.setWidth(10)
    bow_1.setOutline("blue4")
    bow_1.draw(win)
    
    bow_2 = bow_1.clone()
    bow_2.move(80, 0)
    bow_2.draw(win)    
    
    bow_3 = Line(Point(230, 340), pt_2)
    bow_3.setWidth(10)
    bow_3.setOutline("blue4")
    bow_3.draw(win)
    
    bow_4 = Line(Point(370, 340), pt_2)
    bow_4.setWidth(10)
    bow_4.setOutline("blue4")
    bow_4.draw(win)
    
    # draw two orange balloons next to the present
    r = 50
    x2 = 100
    y2 = 200
    distance = 400
    
    balloon_1 = Circle(Point(x2, y2), r)
    balloon_1.setFill("dark orange")
    balloon_1.draw(win)
    tail_1 = Line(Point(x2, y2 + 50), Point(x2, y2 + 270))
    tail_1.draw(win)
    knot_1 = Polygon(Point(x2, y2 + 50), Point(x2 - 20, y2 + 80), Point (x2 + 20, y2 + 80))
    knot_1.setFill("dark orange")
    knot_1.draw(win)
    
    balloon_2 = balloon_1.clone()
    balloon_2.move(distance, 0)
    balloon_2.draw(win)
    tail_2 = tail_1.clone()
    tail_2.move(distance, 0)
    tail_2.draw(win)
    knot_2 = knot_1.clone()
    knot_2.move(distance, 0)
    knot_2.draw(win)    
    
    # display prompt, get user click and close graphics window
    prompt_2 = Text( Point(300, 540), "Click to close the window")
    prompt_2.draw(win)
    win.getMouse()
    win.close()
    
main()
# End of the program
