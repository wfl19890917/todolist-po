'''
Created on 2018年6月11日

@author: admin
'''
import unittest
import time
from PO import LoginPage,DetailPage
from Public import BasePage
from appium import webdriver
class Test(unittest.TestCase):
    def setUp(self):
        self.driver=webdriver.Remote('http://127.0.0.1:4723/wd/hub',BasePage.Base.desired_caps)
        LoginPage.userlogin(self)
    def tearDown(self):
        self.driver.quit()
    def test_detail(self):
        DetailPage.detail_page(self.driver).click_act_loc()
        DetailPage.detail_page(self.driver).click_back_loc()
        ac=self.driver.current_activity
        print(ac)
        self.assertEqual(ac, '.MainActivity', msg='验证失败')
        
if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()