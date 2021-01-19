import time
from selenium import webdriver

driver = webdriver.Firefox()
link = "https://tomsk.hh.ru/"

driver.get(link)
driver.find_element_by_class_name("bloko-input").send_keys("Тестировщик ПО")
driver.find_element_by_class_name("supernova-search-submit-text").click()




