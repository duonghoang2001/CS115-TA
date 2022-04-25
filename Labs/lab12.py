# Lab 12 Key
# Author:  Duong Hoang
# Email:  duong.hoang@uky.edu
# Section: 003

'''
    Purpose: check spelling of a text
    Pre-cond: a dictionary file (.txt), a story file (.txt)
    Post-cond: report misspelled words and total count of them (int)
'''

# main function
def main():
    # get the dictionary file (call the function below) 
    dict_list = get_dictionary()
    # ask the user for the filename to spell check
    story_filename = input("Enter a filename to check: ")
    # open it
    story_file = open(story_filename, "r")
    # turn the words in the file into a list of strings, one word per string 
    story = story_file.read()
    story_list = story.split()
    # close it
    story_file.close()

    # initialize misspelled word counter
    misspell_ct = 0
    # print report header
    print("Misspelled words:")
    # for all the words in that list of words
    for word in story_list:
        # force the word to be lowercase
        word = word.lower()
        # if the word is more than 3 characters long 
        # and is not in the dictionary list
        if len(word) > 3 and word not in dict_list:
            # report it as misspelled and count it
            print(word)
            misspell_ct += 1
    # report the count of misspelled words
    print("There were", misspell_ct, "misspelled words.")

# ----------------------------------------

# function get the dictionary file
def get_dictionary():
    # purpose: get a dictionary file 
    # preconditions: nothing
    # postconditions: returns the list of good words from dictionary file
 
    # assume dictionary file is called "dictionary.txt"
    # open dictionary file
    dict_file = open("dictionary.txt", "r")
    # read the file into one string
    dictionary = dict_file.read()
    # split the string into words in a list (goodlist)
    goodlist = dictionary.split()
    # close dictionary file
    dict_file.close()
    # return goodlist  
    return goodlist
    
# -----------------------------------------

main()