'''
Created on 2018��6��9��

@author: fanglli
'''
from appium import webdriver
from selenium.webdriver.common.by import By
from Public import BasePage
class login_page(BasePage.Base):
    user_loc=(By.ID,'com.example.todolist:id/nameET')
    passwd_loc=(By.ID,'com.example.todolist:id/passwordET')
    logbtn_loc=(By.CLASS_NAME,'android.widget.Button')
    def input_user(self,username):
        self.find_element(*self.user_loc).send_keys(username)
    def input_passwd(self,password):
        self.find_element(*self.passwd_loc).send_keys(password)
    def click_btnlogin(self):
        self.find_element(*self.logbtn_loc).click()
    #登录业务流程 
def userlogin(self):
    login=login_page(self.driver)
    login.input_user('1')
    login.input_passwd('1')
    login.click_btnlogin()
    
    
        
    
    
        