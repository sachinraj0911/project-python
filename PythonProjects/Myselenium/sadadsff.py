import csv
import os
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome('C:\\Users\\sackuma3\\Desktop\\sachin\\Python\\chromedriver.exe')
driver.get("http://www.google.com")
driver.maximize_window()
driver.implicitly_wait(30)
driver.find_element_by_id('gb_70').click()
