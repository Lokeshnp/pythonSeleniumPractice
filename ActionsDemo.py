import time

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

serv_obj = Service("D:\Software\chromedriver.exe")
driver = webdriver.Chrome(service=serv_obj)
driver.implicitly_wait(5)
driver.get("https://www.amazon.in/")
driver.maximize_window()
action = ActionChains(driver)
# action.double_click(driver.find_element(By.))
# action.context_click()
# action.drag_and_drop()
# action.click_and_hold()
action.move_to_element(driver.find_element(By.CSS_SELECTOR, ".icp-nav-link-inner")).perform()
# action.context_click(driver.find_element(By.LINK_TEXT, "See all offers")).perform()
action.context_click(driver.find_element(By.LINK_TEXT, "Learn more")).click().perform()

driver.close()

