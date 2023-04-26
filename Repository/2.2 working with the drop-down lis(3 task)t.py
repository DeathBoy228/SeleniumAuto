from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time


try:
    browser = webdriver.Chrome()
    browser.get("http://suninjuly.github.io/selects1.html")
    a = int(browser.find_element(By.ID, "num1").text)
    b = int(browser.find_element(By.ID, "num2").text)
    Select(browser.find_element(By.TAG_NAME, "select")).select_by_visible_text(str(a + b))
    browser.find_element(By.CSS_SELECTOR, ".btn-default").click()

finally:
    time.sleep(10)
    browser.quit()

