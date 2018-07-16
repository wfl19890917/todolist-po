'''
Created on 2018��6��9��

@author: fanglli
'''
import unittest
import time
from PO import LoginPage
from Public import BasePage
from appium import webdriver
from Public import send_email
from Public import toast
from Data import globalparameter as gl
import os
class Test(unittest.TestCase):
    def setUp(self):
        self.driver=webdriver.Remote('http://127.0.0.1:4723/wd/hub',BasePage.Base.desired_caps)
    def tearDown(self):
        self.driver.quit()
    def test_login_success(self):
        login=LoginPage.login_page(self.driver)
        login.input_user('1')
        login.input_passwd('1')
        login.click_btnlogin()
        print("登录成功")
    def test_login_user_null(self):
        login=LoginPage.login_page(self.driver)
        login.input_user('')
        login.input_passwd('1')
        login.click_btnlogin()
        self.driver.get_screenshot_as_file(gl.tdresult+"\\"+"login_user_null.jpg")
        toast.is_toast_exist(self.driver,'用户名或者密码不能为空 !')
        #error_message = self.dr.find_element_by_id('tip_btn').text
        #self.assertIn('用户名或密码错误', error_message)  # 用assertIn(a,b)方法来断言 a in b  '用户名或密码错误'在error_message里
    def test_login_password_null(self):
        login=LoginPage.login_page(self.driver)
        login.input_user('1')
        login.input_passwd('')
        login.click_btnlogin()
        toast.is_toast_exist(self.driver,'用户名或者密码不能为空 !')
    def test_login_all_null(self):
        login=LoginPage.login_page(self.driver)
        login.input_user('1')
        login.input_passwd('')
        login.click_btnlogin()
        toast.is_toast_exist(self.driver,'用户名或者密码不能为空 !')
    def test_login_user_error(self):
        login=LoginPage.login_page(self.driver)
        login.input_user('2')
        login.input_passwd('1')
        login.click_btnlogin()
        toast.is_toast_exist(self.driver,'用户名或者密码错误 !')
    def test_login_password_error(self):
        login=LoginPage.login_page(self.driver)
        login.input_user('1')
        login.input_passwd('2')
        login.click_btnlogin()
        toast.is_toast_exist(self.driver,'用户名或者密码错误 !')
if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    suite=unittest.TestSuite()
    suite.addTest(Test('test_login_success'))
    '''
    suite.addTest(Test('test_login_user_null'))
    suite.addTest(Test('test_login_password_null'))
    suite.addTest(Test('test_login_all_null'))
    suite.addTest(Test('test_login_user_error'))
    suite.addTest(Test('test_login_password_error'))
    '''
    runner=unittest.TextTestRunner(verbosity=2)
    runner.run(suite)

    
