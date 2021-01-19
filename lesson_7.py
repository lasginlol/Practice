from selenium import webdriver
import time
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))



try:
    browser = webdriver.Firefox()
    browser.get("http://suninjuly.github.io/get_attribute.html")
    x_element = browser.find_element_by_id("treasure")
    x = x_element.get_attribute("valuex")
    y = calc(x)
    option0 = browser.find_element_by_id("answer")
    option0.send_keys(y)
    option1 = browser.find_element_by_id("robotsRule").click()
    option2 = browser.find_element_by_id("robotCheckbox").click()
    option3 = browser.find_element_by_class_name("btn").click()

finally:
    time.sleep(30)
    browser.quit()

