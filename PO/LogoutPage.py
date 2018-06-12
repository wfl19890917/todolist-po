'''
Created on 2018年6月11日

@author: admin
'''
from appium import webdriver
from selenium.webdriver.common.by import By
from Public import BasePage
class logout_page(BasePage.Base):
    more_loc=(By.CLASS_NAME,'android.widget.ImageButton')
    logout_loc=(By.ID,'android:id/title')
    sure_loc=(By.ID,'android:id/button1')
    cancel_loc=(By.ID,'android:id/button2')
    def click_more_loc(self):
        self.find_ClassName(*self.more_loc).click()
    def click_logout_loc(self):
        self.findAU(self.logout_loc).click()
    def click_sure_loc(self):
        self.find_element(self.sure_loc)
    def click_cancel_loc(self):
        self.find_element(self.cancel_loc).click()
def logout(self):
    logout=logout_page(self.driver)
    logout.click_more_loc()
    logout.click_logout_loc()
    logout.click_sure_loc()
        
