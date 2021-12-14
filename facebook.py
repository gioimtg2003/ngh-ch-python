from selenium import webdriver
import pickle
import time
import random

PROXY = "113.160.214.22:8080" # IP:PORT or HOST:PORT
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('--proxy-server=%s' % PROXY)
driver = webdriver.Chrome(options=chrome_options)
driver.get("https://www.tiktok.com")
time.sleep(3)
driver.refresh()
driver.find_element_by_xpath("/html").click()
driver.close()
driver = webdriver.Chrome()
driver.get("https://facebook.com")
