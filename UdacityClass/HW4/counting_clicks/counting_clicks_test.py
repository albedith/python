'''
Created on Feb 23, 2014

@author: albedith
'''
import unittest
import counting_clicks


class Test(unittest.TestCase):

    def test_record_user_click_first_click(self):
        index = [['Udacity',[['http://www.udacity.com',0]]]]
        keyword = 'Udacity'
        url = 'http://www.udacity.com'
        counting_clicks.record_user_click(index,keyword,url)
        self.assertEqual(index,[['Udacity',[['http://www.udacity.com',1]]]])

    def test_record_user_click_first_click_to_second_entry(self):
        index = [['Udacity',[['http://www.udacity.com',0]]],['Wikipedia',[['http://www.wikipedia.org',0]]]]
        keyword = 'Wikipedia'
        url = 'http://www.wikipedia.org'
        counting_clicks.record_user_click(index, keyword, url)
        self.assertEqual(index,[['Udacity',[['http://www.udacity.com',0]]],['Wikipedia',[['http://www.wikipedia.org',1]]]])

    def test_record_user_click_to_not_existent_entry(self):
        index = [['Udacity',[['http://www.udacity.com',0]]]]
        keyword = 'Wikipedia'
        url = 'http://www.wikipedia.org'
        counting_clicks.record_user_click(index, keyword, url)
        self.assertEqual(index,[['Udacity',[['http://www.udacity.com',0]]],['Wikipedia',[['http://www.wikipedia.org',0]]]])

    def test_add_to_index_first_keyword(self):
        index = []
        keyword = 'Udacity'
        url = 'http://www.udacity.com'
        counting_clicks.add_to_index(index,keyword,url)
        self.assertEqual(index,[['Udacity',[['http://www.udacity.com',0]]]])

    def test_add_to_index_new_keyword(self):
        index = [['Udacity',[['http://www.udacity.com',0]]]]
        keyword = 'Wikipedia'
        url = 'http://www.wikipedia.org'
        counting_clicks.add_to_index(index,keyword,url)
        self.assertEqual(index,[['Udacity',[['http://www.udacity.com',0]]],['Wikipedia',[['http://www.wikipedia.org',0]]]])

    def test_add_to_index_new_url(self):
        index = [['Udacity',[['http://www.udacity.com',0]]],['Wikipedia',[['http://www.wikipedia.org',0]]]]
        keyword = 'Udacity'
        url = 'http://www.udacity.com/cs101x/index.html'
        counting_clicks.add_to_index(index,keyword,url)
        self.assertEqual(index,[['Udacity',[['http://www.udacity.com',0],['http://www.udacity.com/cs101x/index.html',0]]],['Wikipedia',[['http://www.wikipedia.org',0]]]])

    def test_add_to_index_repeated_url(self):
        index = [['Udacity',[['http://www.udacity.com',0],['http://www.udacity.com/cs101x/index.html',0]]],['Wikipedia',[['http://www.wikipedia.org',0]]]]
        keyword = 'Udacity'
        url = 'http://www.udacity.com/cs101x/index.html'
        counting_clicks.add_to_index(index,keyword,url)
        self.assertEqual(index,[['Udacity',[['http://www.udacity.com',0],['http://www.udacity.com/cs101x/index.html',0]]],['Wikipedia',[['http://www.wikipedia.org',0]]]])

    def test_lookup_existent_keyword_list(self):
        index = [['Udacity',[['http://www.udacity.com',0],['http://www.udacity.com/cs101x/index.html',0]]],['Wikipedia',[['http://www.wikipedia.org',0]]]]
        keyword = 'Udacity'
        result = counting_clicks.lookup(index, keyword)
        self.assertEqual(result,[['http://www.udacity.com',0],['http://www.udacity.com/cs101x/index.html',0]])

    def test_lookup_not_existent_keyword(self):
        index = [['Udacity',[['http://www.udacity.com',0],['http://www.udacity.com/cs101x/index.html',0]]],['Wikipedia',[['http://www.wikipedia.org',0]]]]
        keyword = 'Google'
        result = counting_clicks.lookup(index, keyword)
        self.assertEqual(result,None)


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()