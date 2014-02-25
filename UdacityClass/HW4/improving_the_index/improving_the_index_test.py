'''
Created on Feb 21, 2014

@author: albedith
'''
import unittest
import improving_the_index


class TestImprovingTheIndex(unittest.TestCase):


    def test_add_to_index_first_keyword(self):
        index = []
        keyword = 'Udacity'
        url = 'http://www.udacity.com'
        improving_the_index.add_to_index(index,keyword,url)
        self.assertEqual(index,[['Udacity',['http://www.udacity.com']]])

    def test_add_to_index_new_keyword(self):
        index = [['Udacity',['http://www.udacity.com']]]
        keyword = 'Wikipedia'
        url = 'http://www.wikipedia.org'
        improving_the_index.add_to_index(index,keyword,url)
        self.assertEqual(index,[['Udacity',['http://www.udacity.com']],['Wikipedia',['http://www.wikipedia.org']]])

    def test_add_to_index_new_url(self):
        index = [['Udacity',['http://www.udacity.com']],['Wikipedia',['http://www.wikipedia.org']]]
        keyword = 'Udacity'
        url = 'http://www.udacity.com/cs101x/index.html'
        improving_the_index.add_to_index(index,keyword,url)
        self.assertEqual(index,[['Udacity',['http://www.udacity.com','http://www.udacity.com/cs101x/index.html']],['Wikipedia',['http://www.wikipedia.org']]])

    def test_add_to_index_repeated_url(self):
        index = [['Udacity',['http://www.udacity.com','http://www.udacity.com/cs101x/index.html']],['Wikipedia',['http://www.wikipedia.org']]]
        keyword = 'Udacity'
        url = 'http://www.udacity.com/cs101x/index.html'
        improving_the_index.add_to_index(index,keyword,url)
        self.assertEqual(index,[['Udacity',['http://www.udacity.com','http://www.udacity.com/cs101x/index.html']],['Wikipedia',['http://www.wikipedia.org']]])

    def test_union_to_empty_list(self):
        a = []
        b = [1,2,3]
        improving_the_index.union(a,b)
        self.assertEqual(a,[1,2,3])

    def test_union_to_equal_empty_list(self):
        a = []
        b = []
        improving_the_index.union(a,b)
        self.assertEqual(a,[])

    def test_union_to_diff_float_list(self):
        a = [1.23,2.3,3.4]
        b = [1.24,2.3,3.4]
        improving_the_index.union(a,b)
        self.assertEqual(a,[1.23,2.3,3.4,1.24])

    def test_union_to_diff_list(self):
        a = [1,2,3]
        b = [4,5,6]
        improving_the_index.union(a,b)
        self.assertEqual(a,[1,2,3,4,5,6])

    def test_union_to_string_list_one_equal_element(self):
        a = ['a','b','c']
        b = ['c','d','e']
        improving_the_index.union(a,b)
        self.assertEqual(a,['a','b','c','d','e'])







if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.test_add_to_index']
    unittest.main()