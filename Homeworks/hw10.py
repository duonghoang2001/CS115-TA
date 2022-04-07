# CS 115 Spring 2022 - Homework 10 Key
# Author: Duong Hoang
# Section: 003
# Email: duong.hoang@uky.edu

'''
    Purpose: read words from user, delimited by whitespace, until they enter an
            empty line. report number of words and average word length
    Pre-cond: one or more words on a line, empty line at end (all strings)
    Post-cond; prompts (str), word count (int), average word length to 2 places (float)
    
'''

def main():
    # initialize counters for total words and total characters of inputs
    char_ct = 0
    words_ct = 0
    lines_ct = 0

    # print prompt and get user's input
    print("----- Enter one line of words at a time, Enter a blank line to stop -----")
    content = input("Enter line: ")

    # while the user input is not just an enter key (empty string)
    while content != '':
        # increment line count
        lines_ct += 1
        # extract a list of words from input
        words = content.split()
        # add number of words from new input to word counter
        words_ct += len(words)
        # calculate total characters of input
        for word in words:
            # add number of characters from new input to character counter
            char_ct += len(word)

        # get next input
        content = input("Enter line: ")

    # calculate average characters/word
    rate = 0
    if words_ct != 0:
        rate = char_ct / words_ct

    # output report with rate formatted to 2 decimal places
    print("\nThere were", lines_ct, "lines containing", words_ct, "words" )
    print("There was an average of {:.2f} characters per word".format(rate))

main()

'''
Test cases:
1.  1, 11.00
2.  20, 4.05
3.  3, 5.00
4.  16, 3.38
5.  0, 0.00

'''