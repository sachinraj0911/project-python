import csv
import os
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome('C:\\Users\\sackuma3\\Desktop\\sachin\\Python\\chromedriver_win32_105\\chromedriver.exe')
driver.get("http://www.google.com")
driver.maximize_window()
driver.implicitly_wait(30)
#driver.find_element_by_id('gb_70').click() /html/body/div[1]/div[1]/div/div/div/div[2]/a
driver.find_element_by_partial_link_text('Sign in').click()
driver.find_element_by_id("identifierId").send_keys("sachinraj0911")
#driver.find_element_by_id("identifierNext").click() VfPpkd-vQzf8d
driver.find_element_by_class_name('VfPpkd-vQzf8d').click()
driver.find_element_by_name("password").send_keys("Sachin@0911")
driver.find_element_by_id("passwordNext").click()

driver.get_screenshot_as_file("..\\screenshots\\google1.png")
