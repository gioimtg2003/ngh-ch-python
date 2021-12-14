from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium_stealth import stealth
from time import sleep
from win32gui import *
import autoit
import random
login =False
browser = webdriver.Chrome()
browser.set_window_rect(100, 0, width=300, height=800)
class set_up():
    global browser, list_lastName, list_firstName, username, Passwd
    Passwd = "10102001a!"
    list_lastName = ("Nguyễn","Trần","Lê","Phạm","Đặng","Võ","Bùi","Ngô")
    list_firstName = ("Thành","Thảo","Dương","Hoàng","Thiện","Hiếu","Trang","My","Nam","Bình")
    username = "simplelove" + str(random.randint(10000,99999))

browser.get("https://accounts.google.com/signup/v2/webcreateaccount?continue=https%3A%2F%2Fwww.google.com%2Fsearch%3Fq%3Dgmail.com%26rlz%3D1C1ONGR_enVN974VN974%26oq%3Dgm%26aqs%3Dchrome.2.69i57j0i271l3j69i61l2.2480j0j1%26sourceid%3Dchrome%26ie%3DUTF-8&hl=vi&dsh=S1863273047%3A1637509273883115&biz=false&flowName=GlifWebSignIn&flowEntry=SignUp")
sleep(5)

# tab số 1
browser.find_element_by_id("lastName").send_keys(random.choice(list_lastName))
browser.find_element_by_id("firstName").send_keys(random.choice(list_firstName))
browser.find_element_by_id("username").send_keys(username)
browser.find_element_by_name("Passwd").send_keys(Passwd)
browser.find_element_by_name("ConfirmPasswd").send_keys(Passwd)
print("done tab 1")