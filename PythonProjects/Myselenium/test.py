import csv
import os
from selenium import webdriver
from selenium.webdriver.common.by import By
driver = webdriver.Chrome('C:\\Users\\sackuma3\\Desktop\\sachin\\Python\\chromedriver_win32_105\\chromedriver.exe')
driver.get("http://www.google.com")
driver.maximize_window()
driver.implicitly_wait(30)
driver.find_element(By.PARTIAL_LINK_TEXT, 'Sign in').click()
driver.find_element(by=By.ID, )