from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import random
file = open("account.txt")
driver = webdriver.Chrome()
driver.get("https://facebook.com")
for i in range(5):
    taikhoan = file.readline()
    matkhau = file.readline()
    driver.set_window_size(200, 700)
    driver.execute_script(
        "window.open('https://facebook.com', '_blank', 'toolbar=0,location=,menubar=0')")
    x = 0
    driver.set_window_position(x, 0)
    x = x+300
    driver.get_window_size
