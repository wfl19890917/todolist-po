'''
Created on 2018年6月11日

@author: admin
'''
import unittest
import time
from PO import LoginPage,LogoutPage
from Public import BasePage
from appium import webdriver
class Test(unittest.TestCase):
    def setUp(self):
        self.driver=webdriver.Remote('http://127.0.0.1:4723/wd/hub',BasePage.Base.desired_caps)
        LoginPage.userlogin(self)
    def tearDown(self):
        self.driver.quit()
    def test_logout(self):
        time.sleep(5)
        self.driver.tap([(608,48),(720,144)], 500)
        self.driver.find_element_by_id('android:id/title').click()
        time.sleep(5)
        self.driver.find_element_by_id('android:id/button1').click()
        self.assertEqual(u"登入",self.driver.find_element_by_id('com.example.todolist:id/loginBtn').get_attribute('text'),msg='验证失败')
if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()