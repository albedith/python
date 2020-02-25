#!/usr/bin/python
# -*- coding: UTF-8 -*-

import unittest
from appium import webdriver

class PythonTest(unittest.TestCase):
    def setUp(self):
# Setting the desired_capabilities as indicated in https://wiki.saucelabs.com/display/DOCS/Platform+Configurator#/
        self.desired_capabilities = {}
        self.desired_capabilities['testobject_api_key'] = 'BA609799D3A94FA3950959EE84DB372D'
        self.desired_capabilities['testobject_device'] = 'LG_Nexus_5X_real'
        self.desired_capabilities['testobject_appium_version'] = '1.6.0'
        self.desired_capabilities['testobject_app_id'] = '4'
        self.desired_capabilities['testobject_test_name'] = 'Native App Test with Appium'

#Accessing the Sauce Labs Cloud
        self.driver = webdriver.Remote(command_executor = ('http://appium.testobject.com/wd/hub'), desired_capabilities = self.desired_capabilities)
        self.driver.implicitly_wait(30)

    def test_sauce(self):
        contexts = self.driver.contexts
        print contexts

        source = self.driver.page_source
        print source

    def tearDown(self):
        self.driver.quit()

if __name__ == '__main__':
    unittest.main()

