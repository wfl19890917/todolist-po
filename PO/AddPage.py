'''
Created on 2018年6月11日

@author: admin
'''
from appium import webdriver
from selenium.webdriver.common.by import By
from Public import BasePage
from selenium import webdriver
import unittest
class add_page(BasePage.Base):
    add_loc=(By.ID,'com.example.todolist:id/action_new')
    shuru_loc=(By.ID,'com.example.todolist:id/toDoItemDetailET')
    savebtn_loc=(By.CLASS_NAME,'android.widget.Button')
    add_activity_loc=(By.XPATH,'//android.widget.TextView[@resource-id="com.example.todolist:id/toDoItemDetailTv"]')
    #activity_loc=(By.XPATH,'//android.widget.TextView[@resource-id="com.example.todolist:id/toDoItemDetailTv"]')
    def click_add_loc(self):
        self.find_element(*self.add_loc).click()
    def input_shuru_loc(self,activity):
        self.find_element(*self.shuru_loc).send_keys(activity)
    def click_savetn_loc(self):
        self.find_element(*self.savebtn_loc).click()
    def is_add_activity_exist(self,num):
        e=self.find_elements(*self.add_activity_loc)[num]
        print(e.text)
def addActivity(self,activity):
    add=add_page(self.driver)
    add.click_add_loc()
    add.input_shuru_loc(activity)
    add.click_savetn_loc()
