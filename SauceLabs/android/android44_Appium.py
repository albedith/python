#!/usr/bin/python
# -*- coding: UTF-8 -*-

import unittest
import os #to read enviroment variables
from appium import webdriver

#Retreiving enviroment variables
SAUCE_USERNAME = os.environ.get('SAUCE_USERNAME')
SAUCE_ACCESS_KEY = os.environ.get('SAUCE_ACCESS_KEY')

class PythonTest(unittest.TestCase):
    def setUp(self):
# Setting the desired_capabilities as indicated in https://wiki.saucelabs.com/display/DOCS/Platform+Configurator#/
        self.desired_capabilities = {}
        self.desired_capabilities['browserName']='browser'
        self.desired_capabilities['platformName'] = 'Android'
        self.desired_capabilities['platformVersion'] = '4.4'
        self.desired_capabilities['appiumVersion'] = '1.5.3'
        self.desired_capabilities['deviceName'] = 'Android Emulator'
        self.desired_capabilities['deviceType'] = 'phone'
        self.desired_capabilities['deviceOrientation'] = 'portrait'
        self.desired_capabilities['name'] = 'Web App Test with Appium'

#Accessing the Sauce Labs Cloud
        self.driver = webdriver.Remote(command_executor = ('http://' + SAUCE_USERNAME + ':' + SAUCE_ACCESS_KEY + '@ondemand.saucelabs.com:80/wd/hub'), desired_capabilities = self.desired_capabilities)
        self.driver.implicitly_wait(30)

    def test_sauce(self):
        self.driver.get('http://www.google.com')
        title = self.driver.title
        self.assertEquals("Google", title)

    def tearDown(self):
        print("Link to your test: https://saucelabs.com/beta/tests/%s" % self.driver.session_id)
        self.driver.quit()

if __name__ == '__main__':
    unittest.main()

