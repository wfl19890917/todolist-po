'''
Created on 2018年6月11日

@author: admin
'''
import unittest
import time
from PO import LoginPage,EditPage
from Public import BasePage
from appium import webdriver
class Test(unittest.TestCase):
    def setUp(self):
        #driver_configure.driver_configure.get_driver(self)
        self.driver=webdriver.Remote('http://127.0.0.1:4723/wd/hub',BasePage.Base.desired_caps)
        LoginPage.userlogin(self)
    def tearDown(self):
        self.driver.quit()
    def test_edit(self):
        EditPage.edit_page(self.driver).touch_act_loc()
        self.driver.find_element_by_name('编辑').click()
        EditPage.edit_page(self.driver).clear_text_loc()
        EditPage.edit_page(self.driver).input_shuru_loc('逛街')
        time.sleep(5)
        EditPage.edit_page(self.driver).click_save_loc()
    def test_delete(self):
        EditPage.edit_page(self.driver).touch_act_loc()
        self.driver.find_element_by_name('删除').click()
        EditPage.edit_page(self.driver).click_sure_loc()  
    def test_cancel(self):
        EditPage.edit_page(self.driver).touch_act_loc()
        self.driver.find_element_by_name('删除').click()
        EditPage.edit_page(self.driver).click_cancel_loc()
               
if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    suite=unittest.TestSuite()
    suite.addTest(Test('test_edit'))
    suite.addTest(Test('test_delete'))
    suite.addTest(Test('test_cancel'))
    runner=unittest.TextTestRunner(verbosity=2)
    runner.run(suite)