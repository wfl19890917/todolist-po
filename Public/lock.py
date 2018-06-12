'''
Created on 2018年6月12日

@author: admin
'''
import time
from appium.webdriver.common.touch_action import TouchAction
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

