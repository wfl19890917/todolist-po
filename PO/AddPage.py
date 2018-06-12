'''
Created on 2018年6月11日

@author: admin
'''
from appium import webdriver
from selenium.webdriver.common.by import By
from Public import BasePage
class add_page(BasePage.Base):
    add_loc=(By.ID,'com.example.todolist:id/action_new')
    shuru_loc=(By.ID,'com.example.todolist:id/toDoItemDetailET')
    savebtn_loc=(By.ID,'com.example.todolist:id/saveBtn')
    def click_add_loc(self):
        self.find_element(*self.add_loc).click()
    def input_shuru_loc(self,activity):
        self.find_element(*self.shuru_loc).send_keys(activity)
    def click_savetn_loc(self):
        self.find_element(*self.savebtn_loc).click()
def addActivity(self,activity):
    add=add_page(self.driver)
    add.click_add_loc()
    add.input_shuru_loc(activity)
    add.click_savetn_loc()
