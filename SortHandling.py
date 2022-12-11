import time

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

browserSortedFirstNames = []
serv_obj = Service("D:\Software\chromedriver.exe")
driver = webdriver.Chrome(service=serv_obj)

# Click on column header
# Collect all column values -> BrowserSortedValueList(A,B,C)

driver.implicitly_wait(5)
driver.maximize_window()
driver.get("https://the-internet.herokuapp.com/tables")
driver.find_element(By.XPATH, "//span[text()='First Name']").click()
first_names = driver.find_elements(By.XPATH, "//table[1]/tbody/tr/td[2]")
for firstname in first_names:
    browserSortedFirstNames.append(firstname.text)

originalBrowserSortedList = browserSortedFirstNames.copy()
# slice, copy will be used to copy list, copy is latest one its faster than slice
#originalBrowserSortedList1 = browserSortedFirstNames.slice()
# Sort this BrowserSortedValueList => newSortedValueList -> (A,B,C)
browserSortedFirstNames.sort()
print(browserSortedFirstNames)
print()
print(originalBrowserSortedList)
# BrowserSortedValueList == newSortedValueList
assert browserSortedFirstNames == originalBrowserSortedList
driver.close()

