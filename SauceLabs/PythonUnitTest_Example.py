#!/usr/bin/python
# -*- coding: UTF-8 -*-

import unittest
import os
import sys
from selenium import webdriver
import sauceclient

# Retrieving environment variables
SAUCE_USERNAME = os.environ.get('SAUCE_USERNAME')
SAUCE_ACCESS_KEY = os.environ.get('SAUCE_ACCESS_KEY')

# Credentials for SauceClient
test_result = sauceclient.SauceClient(SAUCE_USERNAME, SAUCE_ACCESS_KEY)


class Test(unittest.TestCase):
    def setUp(self):
        self.desired_capabilities = {
            'platform': 'Mac 10.10',
            'version': '8',
            'browserName': 'safari',
            'name': 'Python Example Test'}

        self.driver = webdriver.Remote(command_executor = ('http://' + SAUCE_USERNAME + ':' + SAUCE_ACCESS_KEY + '@ondemand.saucelabs.com:80/wd/hub'), desired_capabilities = self.desired_capabilities)

        self.driver.implicitly_wait(30)

    def test_https(self):

        self.driver.get("https://www.google.com/")
        title = self.driver.title
        self.assertEquals("Google", title)

    def tearDown(self):
        # print("Link to your test: https://saucelabs.com/beta/tests/%s" % self.driver.session_id)
        # using the sauceclient to set the pass/fail flags for this test.
        try:
            if sys.exc_info() == (None, None, None):
                test_result.jobs.update_job(self.driver.session_id, passed=True)
            else:
                test_result.jobs.update_job(self.driver.session_id, passed=False)
        finally:
            self.driver.quit()

if __name__ == '__main__':
        unittest.main()

