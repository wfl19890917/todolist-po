'''
Created on 2018年6月11日

@author: admin
'''
from appium import webdriver
from selenium.webdriver.common.by import By
from Public import BasePage
import time
class detail_page(BasePage.Base):
    act_loc=(By.ID,'com.example.todolist:id/toDoItemDetailTv')
    back_loc=(By.ID,'com.example.todolist:id/action_back')
    def click_act_loc(self):
        self.find_element(*self.act_loc).click()
        time.sleep(5)
    def click_back_loc(self):
        self.find_element(*self.back_loc).click()
        time.sleep(5)
    
    
