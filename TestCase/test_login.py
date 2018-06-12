'''
Created on 2018��6��9��

@author: fanglli
'''
import unittest
import time
from PO import LoginPage
from Public import BasePage
from appium import webdriver
import HTMLTestRunner
from Public import send_email
#from Public.send_mail import  send_mail,new_report
class Test(unittest.TestCase):
    def setUp(self):
        #driver_configure.driver_configure.get_driver(self)
        self.driver=webdriver.Remote('http://127.0.0.1:4723/wd/hub',BasePage.Base.desired_caps)
    def tearDown(self):
        self.driver.quit()
    def test_login_success(self):
        login=LoginPage.login_page(self.driver)
        login.input_user('1')
        login.input_passwd('1')
        login.click_btnlogin()
        print("登录成功")
if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    suite=unittest.TestSuite()
    suite.addTest(Test('test_login_success'))
    test_report="D:\\report"
    filename="D:/report/report.html"
    fb=open(filename,'wb')
    runner = HTMLTestRunner.HTMLTestRunner(
        stream=fb,
        title=u'88APP自动化测试报告',
        description=u'项目描述：生产环境'
    )
    runner.run(suite)
    fb.close()
    time.sleep(5)
    #send_email.main2()
    new_report=send_email.new_report(test_report)
    send_email.send_report()
