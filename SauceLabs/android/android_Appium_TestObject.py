#!/usr/bin/python
# -*- coding: UTF-8 -*-

import time
import unittest
from appium import webdriver

class PythonTest(unittest.TestCase):
    def setUp(self):
# Setting the desired_capabilities as indicated in https://wiki.saucelabs.com/display/DOCS/Platform+Configurator#/
        self.desired_capabilities = {}
        self.desired_capabilities['testobject_api_key'] = 'C86598D8266D43CDB4D1969717DF7FBD'
        self.desired_capabilities['testobject_device'] = 'LG_Nexus_5X_real'
        self.desired_capabilities['testobject_appium_version'] = '1.5.2-patched-chromedriver'
        self.desired_capabilities['testobject_app_id'] = '1'
        self.desired_capabilities['testobject_test_name'] = 'Web App Test with Appium and Test Object'

#Accessing the Sauce Labs Cloud
        self.driver = webdriver.Remote(command_executor = ('http://appium.testobject.com/wd/hub'), desired_capabilities = self.desired_capabilities)
        self.driver.implicitly_wait(30)

    def test_sauce(self):
        self.driver.get('http://www.google.com')
        elem = self.driver.find_element_by_name("q")
        elem.click
        elem.send_keys("Sauce Labs")
        elem.submit()
        time.sleep(10)

    def tearDown(self):
        self.driver.quit()

if __name__ == '__main__':
    unittest.main()

