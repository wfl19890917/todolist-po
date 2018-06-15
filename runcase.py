'''
Created on 2018��6��9��
# coding:utf-8
@author: fanglli
'''
import unittest
import HTMLTestRunner
import time
import os
from Public import send_email
from Data import globalparameter as gl
test_dir='E:\\test\\todolist_po\\TestCase'
report_dir='E:\\test\\todolist_po\\Result'
def CreatSuite():
    #定义单元测试容器
    suite=unittest.TestSuite()
    #定搜索用例文件的方法
    discover=unittest.defaultTestLoader.discover(test_dir, pattern='test_*.py', top_level_dir=None)
    #将discover方法筛选出来的用例，循环添加到测试套件中,打印出的用例信息会递增
    for test_case in discover:
            suite.addTests(test_case)           
    print (suite)         
    return suite

if __name__ == "__main__":
    #所有的用例集合
    all_test_cases = CreatSuite()
    #获取系统当前时间
    print(gl.filename)
    if os.path.exists(gl.tdresult):
        fp = open(gl.filename,'wb')
        #定义测试报告
        runner = HTMLTestRunner.HTMLTestRunner(stream=fp, title=u'小牛在线APP2.4.0-UI自动化测试报告', description=u'用例执行情况如下：')
        #运行测试用例
        runner.run(all_test_cases)
        #关闭报告文件
        fp.close()
        time.sleep(10)
        new_report=send_email.get_NewReport(gl.tdresult)
        send_email.send_email(new_report)
    else:
        os.mkdir(gl.tdresult)
        fp = open(gl.filename,'wb')
        #定义测试报告
        runner = HTMLTestRunner.HTMLTestRunner(stream=fp, title=u'小牛在线APP2.4.0-UI自动化测试报告', description=u'用例执行情况如下：')
        #运行测试用例
        runner.run(all_test_cases)
        #关闭报告文件
        fp.close()
        time.sleep(10)
        new_report=send_email.get_NewReport(gl.tdresult)
        send_email.send_email(new_report)
        