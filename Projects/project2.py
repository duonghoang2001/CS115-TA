# CS 115 Spring 2022 - Project 2 Key
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

def main():
    # print title
    print("Don't get to 21!\n")
    print("Each player tries not to get to 21")
    print("Each player has 3 passes, which allow them to not roll on a round.")
    print()

    #  get player 1's name
    p1 = input('Who is player 1? ')
    #  get player 2's name
    p2 = input('Who is player 2? ')
    
    #  roll totals set to zero
    p1_total = 0
    p2_total = 0
    #  passcounts set to 3 (number of passes available at start)
    p1_pass_ct = 3
    p2_pass_ct = 3
    #  initialize round counter to 1
    round_ct = 1
    #  while both totals are < 21
    while p1_total < 21 and p2_total < 21:
        # display round counter
        print("\nRound {}:".format(round_ct))
        # play a turn for player 1
        p1_total, p1_pass_ct = play_turn(p1, p1_total, p1_pass_ct)
        # if player 1's total is < 21
        if p1_total < 21:
            # play a turn for player 2
            p2_total, p2_pass_ct = play_turn(p2, p2_total, p2_pass_ct)
        # increment round counter
        round_ct += 1
        # display info for both players
        print()
        print(p1, "total roll", p1_total, "passes", p1_pass_ct, end='\t|\t')
        print(p2, "total roll", p2_total, "passes", p2_pass_ct, '\n')

    # announce who won (roll tot < 21)
    if p1_total < 21:
        print(p1, "won!")
    else:
        print(p2, "won!")

def play_turn(player: str, total: int, pass_count: int):
    '''
        Purpose: to do one player's turn, performing rolls or passes as player chooses
        Precondition: player name (string), player roll total (int), player's pass count (int)
        Postcondition: player roll total and player's pass count, both int, modified as needed
                if player passed, pass count reduced, if player rolled, roll total increased
    '''
    # if the players still has at least 1 pass
    if pass_count > 0:
        # ask do you want to roll or pass 
        choice = pass_or_roll(player)
        # if they choose roll, 
        if choice == 'R':
            # roll a die 
            roll = random.randint(1, 6)
            # add roll to roll total
            total += roll
            # display roll to players
            print(player, "rolled a", roll)
        # otherwise 
        else:
            # state that the player passed the roll
            print(player, "passed the roll")
            # take one from pass count
            pass_count -= 1
    # otherwise roll a die and add to total (ran out of passes)
    else:
        # roll a die
        roll = random.randint(1, 6)
        # add roll to roll total
        total += roll
        # display roll to players
        print(player, "rolled a", roll)
        
    # returns total roll, passcount
    return total, pass_count

def pass_or_roll(player: str):
    '''
        Purpose: ask the player (pname) whether they want to pass the die or roll
                invalid answers are rejected until the player enters either P or R
                upper or lower case
        Precondition: the player's name (string)
        Postcondition: either P or R (string) based on player's answer (always uppercase)
    '''
    # prompt the player P or R using player's name and get the player's answer
    choice = input("Player {} (P)ass or (R)oll? ".format(player))
    # make it uppercase
    choice = choice.upper()
    # while the answer is not valid
    while choice != 'P' and choice != 'R':
        # display error message
        print("Invalid response, P or R please")
        # get the player's answer
        choice = input("Player {} (P)ass or (R)oll? ".format(player))
        # make it uppercase
        choice = choice.upper()
    
    # return the player's answer
    return choice

main()