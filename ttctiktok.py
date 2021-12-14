from selenium import webdriver
import time 
from selenium.webdriver.common.keys import Keys
import time
import random


driver = webdriver.Firefox()
driver.get("https://tuongtaccheo.com")

driver.execute_script('document.querySelector(".btn.btn-primary").click()')

#logintuongtaccheo
driver.find_element_by_id('name').send_keys("gamemaxde4")
driver.find_element_by_id('password').send_keys("gioimtg2003")
driver.find_element_by_id('password').send_keys(Keys.ENTER)

time.sleep(1.5)
driver.get("https://tuongtaccheo.com/tiktok/kiemtien/subcheo/")
time.sleep(2)

#clickfollow

driver.execute_script('document.querySelector(".btn.btn-default").click()')

driver.find_element_by_class_name('jsx-1854768220 follow-button-wrap button').click()