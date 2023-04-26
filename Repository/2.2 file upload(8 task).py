from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import os


with webdriver.Chrome() as browser:
    with open('text.txt','w') as t:
        pass
    browser.get('http://suninjuly.github.io/file_input.html')
    file_path = os.path.join(os.path.abspath(os.path.dirname(__file__)), 'text.txt')
    [i.send_keys('1')for i in browser.find_elements(By.CLASS_NAME,'form-control')]
    browser.find_element('id','file').send_keys(file_path)
    browser.find_element(By.TAG_NAME, 'button').click()
    time.sleep(100)


time.sleep(10)
browser.quit()

