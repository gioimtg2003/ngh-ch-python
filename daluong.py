import random
import time
from selenium import webdriver
from threading import Thread
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
import pickle
from selenium.webdriver.common.by import By

#file = open("account.txt")


def func(number):
    driver = webdriver.Firefox()
    x = number*250
    y = 0
    driver.set_window_rect(x, y, width=200, height=600)

    Options = webdriver.FirefoxOptions()

    # Options.add_argument('--app=https://www.facebook.com')
    driver.get(url)
    # driver.set_window_size(200,600)
    # tk = file.readline()
    # mk = file.readline()
    if ((number == 0) or (number == 1) or (number == 2) or (number == 3)):
        driver.find_element_by_id("email").send_keys(
            "lihivav318@kingsready.com")
        time.sleep(2)
        driver.find_element_by_id("pass").send_keys("pass12345")
        # time.sleep(2)
        driver.find_element_by_id("pass").send_keys(Keys.ENTER)
    if ( (number == 4) or (number == 5)):
        driver.find_element_by_id("email").send_keys("email")
        time.sleep(2)
        driver.find_element_by_id("pass").send_keys("pass")
        # time.sleep(2)
        driver.find_element_by_id("pass").send_keys(Keys.ENTER)
    # if (number == 0):
    #     filee = "account0.pkl"
    # if (number == 1):
    #     filee = "account1.pkl"
    # cookies = pickle.load(open(filee, "rb"))
    # # if (number == 2):
    # #     filee = "account0.pkl"
    # # if (number == 3):
    # #     filee = "account0.pkl"
    # for cookie in cookies:
    #     driver.add_cookie(cookie)
    # driver.refresh()
    # time.sleep(2)
    # driver.get("https://www.facebook.com/bumbum26.4/posts/632449937904329")
    # time.sleep(2)
    # driver.execute_script('window.scrollBy(0,200)')
    # driver.find_element_by_xpath('/html/body/div[1]/div/div[1]/div[1]/div[3]/div/div/div[1]/div[1]/div[4]/div[2]/div/div[2]/div[2]/div/div/div[2]/div[%d]/div/div/div/div/div/div/div/div/div/div[2]/div/div[4]/div/div/div[1]/div/div[1]/div/div[1]/div/span/div/span[2]/span/span').click()
    # likeButton =  WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "[class='rq0escxv l9j0dhe7 du4w35lb j83agx80 cbu4d94t pfnyh3mw d2edcug0 hpfvmrgz ph5uu5jm b3onmgus iuny7tx3 ipjc6fyt']")))
    # likeButton.click()
    # for j in range(100):1
    #     driver.execute_script('window.scrollBy(0,200)')
    #     time.sleep(2)
    time.sleep(10000)
    # y = 0
    # driver.set_window_rect(x, y, width=300, height=700)
# ---


url = 'https://www.facebook.com'

soluong = int(input("Nhập số nick chạy: "))

# buttons = [False * number_of_threads] # create place

threads = []

for number in range(soluong):
    # get number for place in list `buttons`
    t = Thread(target=func, args={number},)

    time.sleep(1)
    t.start()


for t in threads:
    t.join()
