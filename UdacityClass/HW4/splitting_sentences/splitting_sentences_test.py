'''
Created on Feb 20, 2014

@author: albedith
'''
import unittest
import splitting_sentences



class TestSplittingSentences(unittest.TestCase):


    def test_no_delimiters(self):
        """
        checks if the final
        list doesn't contain any
        delimiters.
        """
        source = "I like Ice Cream"
        splitlist = ""
        result = splitting_sentences.split_string(source,splitlist)
        self.assertEqual(result,['I like Ice Cream'])
        
    def test_one_delimiter(self):
        """
        checks if the final
        list doesn't contain any
        delimiters.
        """
        source = "First Name,Last Name,Street Address,City,State,Zip Code"
        splitlist = ","
        result = splitting_sentences.split_string(source,splitlist)
        self.assertEqual(result,['First Name', 'Last Name', 'Street Address', 'City', 'State', 'Zip Code'])
        
    def test_two_delimiters(self):
        """
        checks if the final
        list doesn't contain any
        delimiters.
        """
        source = "After  the flood   ...  all the colors came out."
        splitlist = " ."
        result = splitting_sentences.split_string(source,splitlist)
        self.assertEqual(result,['After', 'the', 'flood', 'all', 'the', 'colors', 'came', 'out'])  
        
    def test_multiple_delimeters(self):
        """
        checks if the final
        list doesn't contain any
        delimiters.
        """
        source = "This is a test-of the,string separation-code!"
        splitlist = " ,!-"
        result = splitting_sentences.split_string(source,splitlist)
        self.assertEqual(result,['This', 'is', 'a', 'test', 'of', 'the', 'string', 'separation', 'code'])       



if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()