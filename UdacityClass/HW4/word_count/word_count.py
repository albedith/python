'''
Created on Feb 24, 2014

@author: albedith
'''
def count_words(word):
    # returns number of words in a string. Words are defined as string of characters
    # divided by spaces.
    list_words = word.split()
    num_words = 0
    for word in list_words:
        num_words = num_words + 1
    return num_words


passage =("The number of orderings of the 52 cards in a deck of cards "
"is so great that if every one of the almost 7 billion people alive "
"today dealt one ordering of the cards per second, it would take "
"2.5 * 10**40 times the age of the universe to order the cards in every "
"possible way.")
print count_words(passage)
#>>>56