'''
Created on 2018年6月11日

@author: admin
'''
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from appium import webdriver
class Base:
    desired_caps={}
    desired_caps['platformName']='Android'
    desired_caps['platformVersion']='6.0.1'
    desired_caps['deviceName']='aeacb854'
    desired_caps['appPackage']='com.example.todolist'
    desired_caps['appActivity']='.LoginActivity'
    desired_caps['app']='C:\\Users\\admin\\Desktop\\apk\\todolist.apk'
    desired_caps['unicodeKeyboard']='True'
    desired_caps['resetKeyboard']='True'
    desired_caps['noReset']='true'
    desired_caps['automationName']='Uiautomator2'
    def __init__(self,driver):
        self.driver=driver
    def find_element(self,*loc):
        '''重写find_element方法，显式等待'''
        try:
            WebDriverWait(self.driver,10).until(EC.visibility_of_element_located(loc))
            return self.driver.find_element(*loc)
        except Exception as e:
            raise e
    def find_elements(self,*loc):
        '''
        find elements.
        Usage:
        driver.find_elements((By.XPATH,"//a"))
        '''
        try:
            WebDriverWait(self.driver,10).until(EC.visibility_of_all_elements_located(loc))
            return self.driver.find_elements(*loc)
        except Exception as e:
            raise e
 
    def send_keys(self,value,*loc):
        try:
            self.find_element(*loc).clear()
            self.find_element(*loc).send_keys(value)
        except AttributeError as e:
            raise e
    def asserin(self,excp,actual):
        try:
            return self.asserin(excp, actual)
        except Exception as e:
            raise e
         
            
            
