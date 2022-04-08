# Lab 10 Key
# Author:  Duong Hoang
# Email:  duong.hoang@uky.edu
# Section: 003

'''
    Purpose: turn an English sentence into Pig Latin
    Pre-cond: a sentence (string)
    Post-cond: two versions of Pig Latin
'''

def main():
    # print header
    print("Translate an English sentence to a Pig Latin sentence!")
    # input sentence
    sentence = input("Enter English sentence: ")
    # split sentence into list of words
    words = sentence.split()
    # initialize new sentence
    new_sentence = ""
    ## VERSION 1
    # make a string of all the vowels
    vowels = "aeiou"
    # loop each word of the words in sentence
    for word in words:
        # if word[0] in vowels
        if vowels.find(word[0].lower()) != -1:
            # add to new sentence with suffix
            new_sentence += word + "way "
        # else
        else:
            # add to new sentence with suffix
            new_sentence += word[1:] + word[0] + "ay "
    # print sentence
    print("English:", sentence)
    # print new sentence
    print("PL Ver1:", new_sentence)

    ## VERSION 2
    new_sentence_2 = ""
    # loop each word of the words in sentence
    for word in words:
        # find vowel index using find_vowel
        vowel_index = find_vowel(word)
        # if there is a vowel that's not at the beginning of the word
        if vowel_index != -1 and vowel_index != 0:
            new_sentence_2 += word[vowel_index:] + word[:vowel_index] + "ay "
        else:
            new_sentence_2 += word + "way "
    # print new sentence
    print("PL Ver2:", new_sentence_2)
    
def find_vowel(word: str):
    '''
        Purpose: find the location of the first vowel in a string
        Pre-cond: the word (a string).
        Post-cond: It returns the location of the vowel that is closest to 
                the left end of the word, and -1 if no vowel is found at all.
    ''' 
    # make a string of all the vowels
    vowels = "aeiou"
    # initialize character index to the beginning of the string
    char_ind = 0
    # initialize vowel index to -1 (not found)
    vowel_ind = -1
    # while end of the string is not reached and vowel is not found
    while char_ind < len(word) and vowel_ind == -1:
        # if character is a vowel
        if vowels.find(word[char_ind].lower()) != -1:
            # set current index as vowel index
            vowel_ind = char_ind
        # increase character index to the next one
        char_ind += 1

    # return vowel index, -1 if not found
    return vowel_ind

main()

