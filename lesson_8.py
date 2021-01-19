from selenium import webdriver
import time
from selenium.webdriver.support.ui import Select
import math


try:
    browser = webdriver.Firefox()
    browser.get("http://suninjuly.github.io/selects1.html")
    one_element = browser.find_element_by_id("num1").text
    print(one_element)
    two_element = browser.find_element_by_id("num2").text
    print(two_element)
    x = int(one_element) + int(two_element)
    x = str(x)
    # x = "[value='" + str(x) +  "']"
    print(x)

    select = Select(browser.find_elements_by_class_name("custom-select"))
    select.select_by_value(x)

    # browser.find_element_by_class_name("custom-select").click()
    # browser.find_elements_by_css_selector(x).click()
    browser.find_element_by_class_name("btn").click()



finally:
    time.sleep(30)
    browser.quit()
