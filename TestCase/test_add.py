'''
Created on 2018年6月11日

@author: admin
'''
import unittest
import time
from PO import LoginPage,AddPage
from Public import BasePage,SwipeTo
from appium import webdriver

class Test(unittest.TestCase):
    def setUp(self):
        #driver_configure.driver_configure.get_driver(self)
        self.driver=webdriver.Remote('http://127.0.0.1:4723/wd/hub',BasePage.Base.desired_caps)
        LoginPage.userlogin(self)
    def tearDown(self):
        self.driver.quit()
    def test_add(self):
        AddPage.add_page(self.driver).click_add_loc()
        AddPage.add_page(self.driver).input_shuru_loc('开车')
        AddPage.add_page(self.driver).click_savetn_loc()
        #找到最后一个元素
        AddPage.add_page(self.driver).is_add_activity_exist(-1)
    def test_add_more(self):
        for i in range(3):
            AddPage.addActivity(self,'吃饭')
        activity=self.driver.find_elements_by_xpath('//android.widget.TextView[@resource-id="com.example.todolist:id/toDoItemDetailTv"]')[-1]
        self.assertIn(u'吃饭', activity.text) 
        print("添加活动成功 "+activity.text)     
    def test_swipe(self):
        SwipeTo.swipeUp(self.driver,500,2)
        time.sleep(2)      
if __name__ == "__main__":
    
    #import sys;sys.argv = ['', 'Test.testName']
    suite = unittest.TestSuite()
    suite.addTest(Test('test_add'))
    suite.addTest(Test('test_add_more'))
    suite.addTest(Test('test_swipe'))
    '''鎵ц娴嬭瘯'''
    runner=unittest.TextTestRunner(verbosity=2)
    runner.run(suite)