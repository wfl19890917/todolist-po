'''
Created on 2018年6月12日

@author: admin
'''
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
def is_toast_exist(driver,text,timeout=10,poll_frequency=0.01):
    try:
        toast = (By.XPATH, ".//*[contains(@text,'%s')]"%text)
        WebDriverWait(driver, timeout, poll_frequency).until(EC.presence_of_element_located(toast))
        return True
    except:
        return False
