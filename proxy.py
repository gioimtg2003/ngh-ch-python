from selenium import webdriver
PROXY = "27.79.131.31:4003" # IP:PORT or HOST:PORT
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('--proxy-server=%s' % PROXY)
chrome = webdriver.Chrome(options=chrome_options)
chrome.get("http://whatismyipaddress.com")