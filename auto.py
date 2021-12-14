from selenium import webdriver
import time
import random

from selenium.webdriver.common.keys import Keys
file = open("account.txt",'r')
Filelist = file.readlines()
email = Filelist[0]
Pass = Filelist[1]
driver = webdriver.Chrome()
driver.set_window_size(300, 700)

driver.get("https://www.facebook.com")
driver.find_element_by_id("email").send_keys(email)
time.sleep(3)
driver.find_element_by_id("pass").send_keys(Pass)
time.sleep(2)
driver.find_element_by_name("login").click()

while True :
    driver.execute_script('window.scrollBy(0,400)')
    time.sleep(1)
