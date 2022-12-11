import time

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("headless")
#Handling/ignorig SSL certificate/privacy errors
chrome_options.add_argument("--ignore-certificate-errors")

serv_obj = Service("D:\Software\chromedriver.exe")
driver = webdriver.Chrome(service=serv_obj, options=chrome_options)
driver.implicitly_wait(5)
driver.maximize_window()
driver.get("https://the-internet.herokuapp.com")
driver.execute_script("window.scrollBy(0, 500)")
driver.execute_script("window.scrollBy(0, document.body.scrollHeight)")
driver.get_screenshot_as_file("screen.png")
