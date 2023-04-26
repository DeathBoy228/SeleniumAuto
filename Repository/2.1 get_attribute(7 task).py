from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

with webdriver.Chrome() as browser:
    browser.get('http://suninjuly.github.io/get_attribute.html')
    x= browser.find_element('id', 'treasure').get_attribute('valuex')
    browser.find_element(By.TAG_NAME, "input").send_keys(str(math.log(abs(12*math.sin(int(x))))))
    browser.find_element('id','robotCheckbox').click()
    browser.find_element('id', 'robotsRule').click()
    browser.find_element(By.TAG_NAME, 'button').click()
    time.sleep(3000)