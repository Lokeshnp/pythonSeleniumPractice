import time

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

serv_obj=Service("D:\Software\chromedriver.exe")
driver=webdriver.Chrome(service=serv_obj)

# Checking whether the web element is displaying or not using isDisplayed method

# driver.get("https://www.amazon.in/")
# driver.maximize_window()
# driver.find_element(By.ID, "nav-al-container").is_displayed()
# assert not driver.find_element(By.ID, "nav-al-container").is_displayed()


# a = ActionChains(driver)
# m= driver.find_element(By.ID, "nav-link-accountList")
# a.move_to_element(m).perform()
# assert driver.find_element(By.ID, "nav-al-container").is_displayed()
# driver.close()

# Handling Alert
# name = "Rahul"
driver.get("https://retail.onlinesbi.sbi/retail/login.htm")
driver.maximize_window()
time.sleep(5)
driver.find_element(By.CSS_SELECTOR, ".login_button").click()
driver.find_element(By.CSS_SELECTOR, "input[title='Login']").click()
alert=driver.switch_to.alert
# print(alert.text)
# assert name in alert.text
alert.accept()
# alert.dismiss()
# alert.send_keys("String value")
