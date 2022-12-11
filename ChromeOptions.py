import time

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--start-maximized")
chrome_options.add_argument("--headless")
chrome_options.add_argument("--ignore-certificate-errors")
driver = webdriver.Chrome(executable_path="D:\Software\chromedriver.exe", options=chrome_options)

driver.get("https://the-internet.herokuapp.com")

print(driver.title)