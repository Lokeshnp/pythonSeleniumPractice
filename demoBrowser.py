from selenium import webdriver
from selenium.webdriver.chrome.service import Service

# chrome driver
# ser_obj = Service("D:/Software/chromedriver.exe")
# driver = webdriver.Chrome(service=ser_obj)

#firefox
# ser_obj = Service("D:/Software/geckodriver.exe")
# driver = webdriver.Firefox(service=ser_obj)

#Edge
ser_obj = Service("D:/Software/msedgedriver.exe")
driver = webdriver.Edge(service=ser_obj)
driver.maximize_window()
driver.get("https://www.google.com")
print(driver.title)
print(driver.current_url)
driver.get("https://twitter.com/")
print(driver.title)
print(driver.current_url)
driver.minimize_window()
driver.back()
print(driver.title)
print(driver.current_url)
driver.refresh()
driver.forward()
driver.maximize_window()
print(driver.title)
print(driver.current_url)
driver.close()
