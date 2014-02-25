'''
Created on Feb 24, 2014

@author: albedith
'''
import unittest
import converting_seconds


class Test(unittest.TestCase):


    def test_converting_seconds_zero_seconds(self):
        sec = 0
        result = converting_seconds.convert_seconds(sec)
        self.assertEqual(result,'0 hours, 0 minutes, 0 seconds')

    def test_converting_seconds_singular_entries(self):
        sec = 3661
        result = converting_seconds.convert_seconds(sec)
        self.assertEqual(result,'1 hour, 1 minute, 1 second')

    def test_converting_seconds_plural_entries(self):
        sec = 7325
        result = converting_seconds.convert_seconds(sec)
        self.assertEqual(result,'2 hours, 2 minutes, 5 seconds')

    def test_converting_seconds_decimals(self):
        sec = 7261.7
        result = converting_seconds.convert_seconds(sec)
        self.assertEqual(result,'2 hours, 1 minute, 1.7 seconds')



if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()