import time

from selenium import webdriver
from selenium.common import ElementNotInteractableException
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

expectedList = ['Cucumber - 1 Kg', 'Raspberry - 1/4 Kg', 'Strawberry - 1/4 Kg']
actualList = []
serv_obj = Service("D:\Software\chromedriver.exe")
driver = webdriver.Chrome(service=serv_obj)
driver.implicitly_wait(5)
driver.get("https://www.bigbasket.com/ps/?q=cakes%20%26%20pastries#!page=1")
driver.maximize_window()
driver.find_element(By.CSS_SELECTOR, "input[qa='searchBar']").send_keys("cakes & pastries")
driver.find_element(By.XPATH, "//i[@class='icon svg-header svg-search svg-search-dim hidden-sm hidden-xs']").click()
time.sleep(2)  #Implicit wait will not wait for complete products to load, if it gets
#empty list it will continue so we should put static wait for 2 secs
results = driver.find_elements(By.XPATH, "//div[@qa='product']")
count = len(results)
assert count > 0
for result in results:
    try:
        actualList.append(result.find_element(By.XPATH, "h4").text)
        result.find_element(By.XPATH, "//button[@qa='add']").click()
    except ElementNotInteractableException:
        print("Exception caught")

assert expectedList == actualList

# wait = WebDriverWait(driver, 10)
# wait.until(expected_conditions.presence_of_element_located((By.CSS_SELECTOR, ".promoInfo")))


#Sum Validations
prices = driver.find_elements(By.CSS_SELECTOR, "tr td:nth-child(5) p")
Sum=0
for price in prices:
    Sum = Sum + int(price.text)

print(Sum)

totalSum = int(driver.find_element(By.CSS_SELECTOR, ".toAmt").text)

assert Sum == totalSum

discountedAmount = float(driver.find_element(By.CSS_SELECTOR, ".discountText").text)

assert totalSum > discountedAmount

driver.close()
