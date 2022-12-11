import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

ser_obj = Service("D:\Software\chromedriver.exe")
driver = webdriver.Chrome(service=ser_obj)
driver.get("https://www.myntra.com/myntra-fashion-store?rf=Discount%20Range%3A90.0_100.0_90.0%20TO%20100.0")
driver.maximize_window()
gender_list = driver.find_elements(By.XPATH,
                                   "//ul[@class='gender-list']//label[@class='common-customRadio gender-label']")

# for gender in gender_list:
#     print(gender.text)
#     if gender.text == "Girls":
#         gender.click()
#         time.sleep(15)
#         flag = driver.find_element(By.XPATH, "//ul[@class='gender-list']//label[@class='common-customRadio gender-label undefined']//input[@type='radio']").is_selected()
#         print(flag)
#         assert flag
#         break

gender_list[2].click()
time.sleep(15)
flag = driver.find_element(By.XPATH, "//ul[@class='gender-list']//label[@class='common-customRadio gender-label undefined']//input[@type='radio']").is_selected()
print(flag)
assert flag

driver.close()
