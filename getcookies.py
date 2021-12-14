from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys
import pickle

soluongaccgetcookie = int(input("Nhập Số nick muốn getcookies: "))

for t in range(soluongaccgetcookie):
    taikhoancuaban = input("Nhập tài khoản facebook: ")
    matkhaucuaban = input("Nhập mật khẩu của bạn: ")
    driver = webdriver.Firefox()
    driver.get("https://facebook.com")
    
    driver.find_element_by_name("email").send_keys(taikhoancuaban)
    time.sleep(0.5)
    driver.find_element_by_name("pass").send_keys(matkhaucuaban)
    driver.find_element_by_name("pass").send_keys(Keys.ENTER)
    time.sleep(4)
    file1 = str(t)
    file2 = 'account' + file1 + '.pkl'
    pickle.dump(driver.get_cookies(), open(file2, "wb"))
    driver.close()
