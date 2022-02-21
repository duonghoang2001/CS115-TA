# Lab 4 Key
# Author:  Duong Hoang
# Email:  duong.hoang@uky.edu
# Section: 003
'''
    Purpose: to take the user on an adventure
    Pre-conditions:  user inputs choices as integers, 1 or 2.
    Post-conditions:  prompts are displayed, results of actions are displayed
        outcome of game is reported

'''

###Implementation###

def main():
    # set gold flag to False
    gold_flag = False
    # set coconut flag to False
    coconut_flag = False
    # set lived flag to True
    lived_flag = True
    # display first prompt  
    print("Your three hour Caribbean cruise encounters a perfect storm.")
    print("Tossed overboard, you wake on the beach of a deserted island.")
    print("You see the beach stretching to the north and some trees inland.\n")
    print("Do you")
    print("1. Walk along the beach")
    print("2. Head for the trees")
    # get user's first choice
    first_choice = input("> ")
    # if user chooses 1
    if first_choice == '1':
        # display chest prompt Open / Carry
        print("You see a chest half buried in the sand.\n")
        print("Do you")
        print("1. Open the chest")
        print("2. Pick up the chest.")
        # get user's second choice
        second_choice = input("> ")
        # if user chooses 1
        if second_choice == '1':
            print("You find 500 gold doubloons")
            gold_flag = True
        else:
            print("Sorry, as you place your hand under the chest,")
            print("you are bitten by a venomous snake.")
            print("Your suffering is great, followed by your death")
            lived_flag = False
    
    else: 
        # display gorilla prompt Arm wrestle/Hello
        print("You see a gorilla next to a tree\n")
        print("Do you")
        print("1. Arm wrestle the gorilla")
        print("2. Say hello.")
        # get user's second choice
        second_choice = input("> ")
        # if user chooses 1
        if second_choice == '1':
            print("You win the match with the gorilla! He gives you a coconut!")
            coconut_flag = True
        else:
            print("He thumps his chest, and sprints up the mountain.")

    # display result
    print("\nAdventrure over!\n")
    if lived_flag:
        print("Congratulations! You survived the challenge.")
        if coconut_flag:
            print("You have a coconut")
        elif gold_flag:
            print("You have gold")
    else:
        print("You didn't make it")

main()

'''
Test cases:
A.  Walk on the beach, pick up chest
B.  Sorry, as you place your hand under the chest,
    you are bitten by a venomous snake.
    Your suffering is great, followed by your death,
    You didn't make it
C.  Head for the trees, arm wrestle the gorilla
D.  1
E.  You win the match with the gorilla! He gives you a coconut!,
    Congratulations! You survived the challenge.
    You have a coconut
F.  Head for the trees, say hello
G.  2
H.  Congratulations! You survived the challenge.

'''

