import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

ser_obj = Service("D:/Software/chromedriver.exe")
driver = webdriver.Chrome(service=ser_obj)
driver.maximize_window()

# Handling dynamic web elements
# select value in static dropdown
driver.get("https://www.amazon.in/")
driver.find_element(By.CSS_SELECTOR, "div[class='nav-search-field ']").click()
driver.find_element(By.ID, "twotabsearchtextbox").send_keys("hotspot")
time.sleep(2)
watches = driver.find_elements(By.CSS_SELECTOR, "div[class='autocomplete-results-container'] div")
for watch in watches:
    if watch.text == "hotspot jiofi":
        watch.click()
        break

#this is for getting text from static text box
# print(driver.find_element(By.ID, "twotabsearchtextbox").text)

#This is for getting text from dynamically updated values in text box
#print(driver.find_element(By.ID, "twotabsearchtextbox").get_attribute("value"))

assert driver.find_element(By.ID, "twotabsearchtextbox").get_attribute("value") == 'hotspot jiofi'
driver.close()
