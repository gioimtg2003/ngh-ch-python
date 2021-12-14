from selenium import webdriver
from selenium.webdriver.common.keys import Keys

chrome_options = webdriver.ChromeOptions()
driver = webdriver.Chrome()
driver.set_window_size(250,700)
driver.set_window_position(300,0)
body = driver.find_element_by_tag_name("body")
driver.find_element_by_tag_name("body").send_keys(Keys.CONTROL + 't')
