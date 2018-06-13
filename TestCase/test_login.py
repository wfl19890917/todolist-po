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
import os
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
    def test_login_user_null(self):
        login=LoginPage.login_page(self.driver)
        login.input_user('')
        login.input_passwd('1')
        login.click_btnlogin()
        print("用户名为空")
if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    suite=unittest.TestSuite()
    suite.addTest(Test('test_login_success'))
    suite.addTest(Test('test_login_user_null'))
    report_dir="E:\\test\\todolist_po\\Result\\"
    #获取系统当前时间
    now = time.strftime('%Y-%m-%d-%H_%M_%S', time.localtime(time.time()))
    day = time.strftime('%Y-%m-%d', time.localtime(time.time()))
    #定义单个测试报告的存放路径，支持相对路径
    tdresult = report_dir + day
    #os.mkdir(tdresult)
    filename = tdresult + "\\" + now + "_result.html"
    #filename="D:/report/report.html"
    fb=open(filename,'wb')
    runner = HTMLTestRunner.HTMLTestRunner(
        stream=fb,
        title=u'todolist自动化测试报告',
        description=u'执行结果总结'
    )
    runner.run(suite)
    fb.close()
    time.sleep(5)
    new_report=send_email.get_NewReport(tdresult)
    send_email.send_email(new_report)
