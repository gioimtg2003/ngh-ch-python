from selenium import webdriver
import time
import pickle
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome(executable_path="")
# login
driver.get("https://www.facebook.com")
cookies = pickle.load(open("cookie.pkl", "rb"))

for cookie in cookies:
    driver.add_cookie(cookie)
driver.refresh()

time.sleep(2)

driver.get("https://www.facebook.com/chuyencuamay.26/posts/442512897440854")

time.sleep(3)
comment = driver.find_element_by_xpath('/html/body/div[1]/div/div[1]/div/div[3]/div/div/div[1]/div[1]/div[4]/div[1]/div/div/div/div/div/div/div/div/div/div[1]/div/div[2]/div/div[4]/div/div/div[2]/div[4]/div[1]/div[2]/span/span')
comment.click()
commentlist = driver.find_elements_by_xpath('//*[@id="mount_0_0_6s"]/div/div[1]/div/div[3]/div/div/div[1]/div[1]/div[4]/div[1]/div/div/div/div/div/div/div/div/div/div[1]/div/div[2]/div/div[4]/div/div/div[2]/ul/li[1]/div[1]/div[2]/div')
print(commentlist)