import pickle
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
import time
driver = webdriver.Chrome()
driver.get("https://facebook.com")
cookies = pickle.load(open("account2.pkl", "rb"))
file = open("account.txt",'r')
abc = file.read()
    
for cookie in cookies:
    driver.add_cookie(cookie)
driver.refresh()
# time.sleep(2)
# abcc = driver.find_element_by_xpath("/html/body/div[1]/div/div[1]/div/div[3]/div/div/div[1]/div[1]/div/div[2]/div/div/div/div[2]/div/div[1]/div/div[2]/div/div/div/a/div/div/div[1]/div")
# abcc.click()

