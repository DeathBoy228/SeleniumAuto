import math
from selenium import webdriver
from selenium.webdriver.common.by import By
import time


link = "http://suninjuly.github.io/math.html"
browser = webdriver.Chrome()
browser.get(link)
def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))

try:
    x_element = browser.find_element(By.XPATH,"//*[@id='input_value']")
    x = x_element.text
    y = calc(x)
    input1 = browser.find_element(By.XPATH, "//*[@id='answer']")
    input1.send_keys(y)
    option1 = browser.find_element(By.XPATH, "//*[@id='robotCheckbox']")
    option1.click()
    option2 = browser.find_element(By.XPATH, "//*[@id='robotsRule']")
    option2.click()
    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()
finally:
    time.sleep(15)
    browser.quit()
