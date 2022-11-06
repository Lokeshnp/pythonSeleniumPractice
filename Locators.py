from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

ser_obj = Service("D:/Software/chromedriver.exe")
driver = webdriver.Chrome(service=ser_obj)
driver.maximize_window()
driver.get("https://login.yahoo.com/?.intl=in&rl=1&.src=ym")

#ID, XPATH, CSSSelector, Classname, name, text

driver.find_element(By.NAME, "username").send_keys("lokeshnp77@gmail.com")
flag = driver.find_element(By.NAME, "persistent").is_enabled()
print(flag)
driver.find_element(By.NAME, "persistent").click()
driver.find_element(By.ID, "login-signin").click()
driver.close()

