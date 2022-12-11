import time

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

serv_obj = Service("D:\Software\chromedriver.exe")
driver = webdriver.Chrome(service=serv_obj)
driver.implicitly_wait(5)
driver.maximize_window()
driver.get("https://the-internet.herokuapp.com/iframe")
driver.switch_to.frame("mce_0_ifr")
driver.find_element(By.CSS_SELECTOR, "body[id='tinymce'] p").clear()
driver.find_element(By.CSS_SELECTOR, "body[id='tinymce'] p").send_keys("Practicing automation")
driver.switch_to.default_content()
print(driver.find_element(By.TAG_NAME, "h3").text)