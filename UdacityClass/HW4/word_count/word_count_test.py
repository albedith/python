'''
Created on Feb 24, 2014

@author: albedith
'''
import unittest
import word_count


class Test(unittest.TestCase):

    def test_word_count_no_words(self):
        word = ''
        result = word_count.count_words(word)
        self.assertEqual(result, 0)

    def test_word_count_one_word(self):
        word = 'I'
        result = word_count.count_words(word)
        self.assertEqual(result, 1)

    def test_word_count_one_sentence(self):
        word = 'I love my dog.'
        result = word_count.count_words(word)
        self.assertEqual(result, 4)

    def test_word_count_passage(self):
        word = ("The number of orderings of the 52 cards in a deck of cards "
                "is so great that if every one of the almost 7 billion people alive "
                "today dealt one ordering of the cards per second, it would take "
                "2.5 * 10**40 times the age of the universe to order the cards in every "
                "possible way.")
        result = word_count.count_words(word)
        self.assertEqual(result, 56)



if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()