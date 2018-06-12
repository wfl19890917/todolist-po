'''
Created on 2018楠烇拷4閺堬拷19閺冿拷

@author: admin
'''
# coding:utf-8
from appium import webdriver
from time import sleep 
from appium.webdriver.common.touch_action import TouchAction
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.by import By
def swipeUp(driver, t=500, n=1):
    l = driver.get_window_size()
    x1 = l['width'] * 0.5  # x閸ф劖鐖�
    y1 = l['height'] * 0.75  # 鐠у嘲顫恲閸ф劖鐖�   # 缂佸牏鍋閸ф劖鐖�
    y2 = l['height'] * 0.125 
    for i in range(n):
        driver.swipe(x1, y1, x1, y2, t)

def swipeDown(driver, t=500, n=1):
    l = driver.get_window_size()
    x1 = l['width'] * 0.5  # x閸ф劖鐖�
    y1 = l['height'] * 0.25  # 鐠у嘲顫恲閸ф劖鐖�
    y2 = l['height'] * 0.75  # 缂佸牏鍋閸ф劖鐖�
    for i in range(n):
        driver.swipe(x1, y1, x1, y2, t)

def swipLeft(driver, t=500, n=1):
    l = driver.get_window_size()
    x1 = l['width'] * 0.75
    y1 = l['height'] * 0.5
    x2 = l['width'] * 0.25
    y2 = l['height'] * 0.5
    for i in range(n):
        driver.swipe(x1, y1, x2, y2, t)

def swipRight(driver, t=500, n=1):
    l = driver.get_window_size()
    x1 = l['width'] * 0.25
    y1 = l['height'] * 0.5
    x2 = l['width'] * 0.75
    for i in range(n):
        driver.swipe(x1, y1, x2, y1, t)
def setLock(self):
    time.sleep(5)
    lock_pattern = self.driver.find_element_by_id('com.uniview.app.smb.phone.en.ezview:id/gesturepwd_create_lockview')
    x = lock_pattern.location.get('x')
    y = lock_pattern.location.get('y')
    width = lock_pattern.size.get('width')
    height = lock_pattern.size.get('height')
    print(x, y, width, height)
    offset = width / 6
    p11 = int(x + width / 6), int(y + height / 6)
    p12 = int(x + width / 2), int(y + height / 6)
    p13 = int(x + width - offset), int(y + height / 6)
    p21 = int(x + width / 6), int(y + height / 2)
    p22 = int(x + width / 2), int(y + height / 2)
    p23 = int(x + width - offset), int(y + height / 2)
    p31 = int(x + width / 6), int(y + height - offset)
    p32 = int(x + width / 2), int(y + height - offset)
    p33 = int(x + width - offset), int(y + height - offset)
    p3 = p13[0] - p11[0]
    time.sleep(3)
    TouchAction(self.driver).press(x=p11[0], y=p11[1]).move_to(x=p3, y=0).wait(1000).move_to(x=0, y=p3).wait(1000).release().perform()
def unLock(self):
    time.sleep(5)
    lock_pattern = self.driver.find_element_by_id('com.uniview.app.smb.phone.en.ezview:id/gesturepwd_unlock_lockview')
    x = lock_pattern.location.get('x')
    y = lock_pattern.location.get('y')
    width = lock_pattern.size.get('width')
    height = lock_pattern.size.get('height')
    print(x, y, width, height)
    offset = width / 6
    p11 = int(x + width / 6), int(y + height / 6)
    p12 = int(x + width / 2), int(y + height / 6)
    p13 = int(x + width - offset), int(y + height / 6)
    p21 = int(x + width / 6), int(y + height / 2)
    p22 = int(x + width / 2), int(y + height / 2)
    p23 = int(x + width - offset), int(y + height / 2)
    p31 = int(x + width / 6), int(y + height - offset)
    p32 = int(x + width / 2), int(y + height - offset)
    p33 = int(x + width - offset), int(y + height - offset)
    p3 = p13[0] - p11[0]
    time.sleep(3)
    TouchAction(self.driver).press(x=p11[0], y=p11[1]).move_to(x=p3, y=0).wait(1000).move_to(x=0, y=p3).wait(1000).release().perform()
def gesturepassword(self):
    list_pwd = self.driver.find_elements_by_class_name("android.widget.ImageView")
    TouchAction(self.driver).press(list_pwd[1]).move_to(list_pwd[1]).move_to(list_pwd[4]).wait(100).move_to(list_pwd[7]).wait(100).move_to(list_pwd[8]).release().perform()
    time.sleep(1)
    print("杈撳叆鎵嬪娍瀵嗙爜")
    try:
        ee = self.driver.find_element_by_name("璇峰啀缁樺埗鎵嬪娍瀵嗙爜")
        list_pwd = self.driver.find_elements_by_class_name("android.widget.ImageView")
        TouchAction(self.driver).press(list_pwd[1]).move_to(list_pwd[1]).move_to(list_pwd[4]).wait(100).move_to(list_pwd[7]).wait(100).move_to(list_pwd[8]).release().perform()
    except Exception:
        pass
def is_toast_exist(driver,text,timeout=10,poll_frequency=0.01):
    try:
        toast = (By.XPATH, ".//*[contains(@text,'%s')]"%text)
        WebDriverWait(driver, timeout, poll_frequency).until(expected_conditions.presence_of_element_located(toast))
        return True
    except:
        return False