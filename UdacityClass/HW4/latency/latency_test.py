'''
Created on Feb 24, 2014

@author: albedith
'''
import unittest
import latency


class Test(unittest.TestCase):


    def test_latency_point_A(self):
        ms = 50
        km = 5000
        result = latency.speed_fraction(ms, km)
        self.assertEqual(result,0.666666666667)

    def test_latency_point_B(self):
        ms = 50
        km = 10000
        result = latency.speed_fraction(ms, km)
        self.assertEqual(result,1.33333333333)


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()