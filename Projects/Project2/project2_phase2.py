# CS 115 Spring 2022 - Project 2 Phase II Key
# Author: Duong Hoang
# Section: 003
# Email: duong.hoang@uky.edu

"""
    Purpose: 2 players take turns rolling a die - 6-sided
            the first player to total rolls to 21 or greater loses.
            a player can pass a roll but only 3 times
    Preconditions: player names (strings), decisions to roll or pass (strings)
    Postconditions: prompts, display of totals and pass counts, rolls of the die
                    statement of who wins
"""

# import random libary
import random
from graphics import *

def main():
    # create window
    win_width = 500
    win_height = 600
    win = GraphWin("TwentyOne!", win_width, win_height)

    # calculate window middle point
    x1 = win_width / 2
    y1 = win_height / 2

    # display title
    title1 = Text(Point(x1, 40), "Don't get to 21!\n")
    title2 = Text(Point(x1, 90), "Each player tries not to get to 21")
    title3 = Text(Point(x1, 110), "Each player has 3 passes, which allow them to not roll on a round.")
    title1.draw(win)
    title2.draw(win)
    title3.draw(win)

    # get player 1's name and player 2's name
    x2 = win_width / 5
    entry_size = 7
    p1_prompt = Text(Point(x2, y1), 'Player 1 Name:')
    p1_entry = Entry(Point(x2 * 2, y1), entry_size)
    p2_prompt = Text(Point(x2 * 3, y1), 'Player 2 Name:')
    p2_entry = Entry(Point(x2 * 4, y1), entry_size)
    p1_prompt.draw(win)
    p2_prompt.draw(win)
    p1_entry.draw(win)  
    p2_entry.draw(win)
    win.getMouse() # leave time for player to type
    p1 = p1_entry.getText()
    p2 = p2_entry.getText()

    # clear screen
    title2.undraw()
    title3.undraw()
    p1_prompt.undraw()
    p2_prompt.undraw()
    p1_entry.undraw()
    p2_entry.undraw()

    #  roll totals set to zero
    p1_total = 0
    p2_total = 0
    #  passcounts set to 3 (number of passes available at start)
    p1_pass_ct = 3
    p2_pass_ct = 3
    #  initialize round counter to 1
    round_ct = 1
    # initialize report display
    y2 = 15
    name_1 = Text(Point(x2, y2), "Player " + p1)
    rolls_1 = Text(Point(x2, y2 + 20), "Total Rolls: " + str(p1_total))
    passes_1 = Text(Point(x2, y2 + 40), "Passes: " + str(p1_pass_ct))
    name_2 = Text(Point(x2 * 4, y2), "Player " + p2)
    rolls_2 = Text(Point(x2 * 4, y2 + 20), "Total Rolls: " + str(p2_total))
    passes_2 = Text(Point(x2 * 4, y2 + 40), "Passes: " + str(p2_pass_ct))
    name_1.draw(win)
    name_2.draw(win)
    rolls_1.draw(win)
    rolls_2.draw(win)
    passes_1.draw(win)
    passes_2.draw(win)

    #  while both totals are < 21
    while p1_total < 21 and p2_total < 21:
        # display round counter
        title1.setText("\nRound {}:".format(round_ct))
        # play a turn for player 1
        p1_total, p1_pass_ct = play_turn(p1, p1_total, p1_pass_ct, win)
        # if player 1's total is < 21
        if p1_total < 21:
            # play a turn for player 2
            p2_total, p2_pass_ct = play_turn(p2, p2_total, p2_pass_ct, win)
        # increment round counter
        round_ct += 1
        # update display info for both players
        rolls_1.setText("Total Rolls: " + str(p1_total))
        passes_1.setText("Passes: " + str(p1_pass_ct))
        rolls_2.setText("Total Rolls: " + str(p2_total))
        passes_2.setText("Passes: " + str(p2_pass_ct))

    # announce who won (roll tot < 21)
    result = p1 + " wins!"
    if p2_total < 21:
        result = p2 + " wins!"
    announce = Text(Point(x1, y1), result)
    announce.setSize(30)
    announce.draw(win)

    # prompt to close
    close_prompt = Text(Point(x1, win_height - 30), "Click to close")
    close_prompt.draw(win)
    win.getMouse()
    win.close()

def play_turn(player: str, total: int, pass_count: int, window: GraphWin):
    '''
        Purpose: to do one player's turn, performing rolls or passes as player chooses
        Precondition: player name (string), player roll total (int), player's pass count (int)
        Postcondition: player roll total and player's pass count, both int, modified as needed
                if player passed, pass count reduced, if player rolled, roll total increased
    '''
    # initialize roll value to 0 (assume player passes)
    roll = 0
    # initialize result to empty
    result = ""
    # if the players still has at least 1 pass
    if pass_count > 0:
        # ask do you want to roll or pass 
        choice = pass_or_roll(player, window)
        # if they choose roll, 
        if choice == 'R':
            # roll a die 
            roll = random.randint(1, 6)
            # add roll to roll total
            total += roll
            # display roll to players
            result = player + " rolled a " + str(roll)
        # otherwise 
        else:
            # state that the player passed the roll
            result = player + " passed the roll"
            # take one from pass count
            pass_count -= 1
    # otherwise roll a die and add to total (ran out of passes)
    else:
        # roll a die
        roll = random.randint(1, 6)
        # add roll to roll total
        total += roll
        # display roll to players
        result = player + " rolled a " + str(roll)
    # display result
    display_result = Text(Point(window.getWidth() / 2, 150), result)
    display_result.draw(window)

    # draw die rolled
    die_image = draw_die(roll, window)
    # hold the screen for the user to see the image
    window.getMouse()
    # clear the window
    display_result.undraw()
    die_image.undraw()
    # returns total roll, passcount
    return total, pass_count

def pass_or_roll(player: str, window: GraphWin):
    '''
        Purpose: ask the player (pname) whether they want to pass the die or roll
                invalid answers are rejected until the player enters either P or R
                upper or lower case
        Precondition: the player's name (string)
        Postcondition: either P or R (string) based on player's answer (always uppercase)
    '''
    # prompt the player P or R using player's name 
    player_prompt = Text(Point(window.getWidth() / 2, 230), 
                        player + " what do you want to do?")
    player_prompt.setSize(20)
    player_prompt.draw(window)

    # draw Pass and Roll boxes for player to choose
    size = 100
    p_x_upper = 150
    p_y_upper = 300
    p_upper_left = Point(p_x_upper, p_y_upper)
    p_lower_right = Point(p_x_upper + size, p_y_upper + size)
    p_box = Rectangle(p_upper_left, p_lower_right)
    p_text = Text(p_box.getCenter(), "Pass")
    r_upper_left = Point(p_x_upper + size + 20, p_y_upper)
    r_lower_right = Point(r_upper_left.getX() + size, p_lower_right.getY())
    r_box = Rectangle(r_upper_left, r_lower_right)
    r_text = Text(r_box.getCenter(), "Roll")
    p_box.draw(window)
    p_text.draw(window)
    r_box.draw(window)
    r_text.draw(window)

    # get user's click choice
    click = window.getMouse()
    # while the click in not inside any boxes
    while (not inbetween(p_upper_left, click, p_lower_right) and 
            not inbetween(r_upper_left, click, r_lower_right)):
        # get the player's next click
        click = window.getMouse()
    
    # clear window
    player_prompt.undraw()
    p_box.undraw()
    r_box.undraw()
    p_text.undraw()
    r_text.undraw()

    # check which box user clicked
    # initialize to "P" (assuming user choose to pass)
    choice = "P" 
    # if user choose to roll
    if inbetween(r_upper_left, click, r_lower_right): 
        choice = "R"

    # return the player's choice
    return choice

def draw_die(roll: int, window: GraphWin):
    '''
        Purpose: draw die based on number rolled, 0 for pass
        Precondition: roll (int), window (GraphWin)
        Postcondition: draw corresponding die image to the window,
                        and return Image object
    '''
    # create die image corresponding to roll number
    die_pic = Image(Point(250, 250), str(roll) + ".gif")
    # draw image
    die_pic.draw(window)
    
    # return die image
    return die_pic

def inbetween (pt1: Point, pt2: Point, pt3: Point):
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

main()