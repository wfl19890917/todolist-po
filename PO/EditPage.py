'''
Created on 2018年6月11日

@author: admin
'''
from appium import webdriver
from selenium.webdriver.common.by import By
from Public import BasePage
from appium.webdriver.common.touch_action import TouchAction
import time
class edit_page(BasePage.Base):
    act_loc=(By.ID,'com.example.todolist:id/toDoItemDetailTv')
    text_loc=(By.ID,'com.example.todolist:id/toDoItemDetailET')
    shuru_loc=(By.ID,'com.example.todolist:id/toDoItemDetailET')
    save_loc=(By.ID,'com.example.todolist:id/saveToDoItemBtn')
    sure_loc=(By.ID,'android:id/button1')
    cancel_loc=(By.ID,'android:id/button2')
    def touch_act_loc(self):
        action=self.find_element(*self.act_loc)
        TouchAction(self.driver).press(action).wait(2000).release().perform()
    def clear_text_loc(self):
        self.find_element(*self.text_loc).clear()
    def input_shuru_loc(self,activity):
        self.find_element(*self.shuru_loc).send_keys(activity)
    def click_save_loc(self):
        self.find_element(*self.save_loc).click()
    def click_sure_loc(self):
        self.find_element(*self.sure_loc).click()
    def click_cancel_loc(self):
        self.find_element(*self.cancel_loc).click()
    
