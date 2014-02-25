'''
Created on Feb 24, 2014

@author: albedith
'''
import unittest
import convert_to_roman


class Test(unittest.TestCase):


    def test_convert_to_roman_I_to_X(self):
        roman_list = ['I', 'II', 'III', 'IV', 'V', 'VI', 'VII', 'VIII', 'XI', 'X']
        i = 1
        for roman_num in roman_list:
            self.assertEqual(convert_to_roman.convert_to_roman(i),roman_list[i-1])
            i += 1
            


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.test_convert_to_roman']
    unittest.main()