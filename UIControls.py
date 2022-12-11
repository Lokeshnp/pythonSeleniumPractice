import time

from selenium import webdriver
from selenium.common import StaleElementReferenceException
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

ser_obj = Service("D:\Software\chromedriver.exe")
driver = webdriver.Chrome(service=ser_obj)
driver.get("https://www.amazon.in/")
driver.maximize_window()
driver.find_element(By.CSS_SELECTOR, "div[class='nav-search-field ']").click()
driver.find_element(By.ID, "twotabsearchtextbox").send_keys("watches")
time.sleep(2)
watches = driver.find_elements(By.CSS_SELECTOR, "div[class='autocomplete-results-container'] div")
for watch in watches:
    if watch.text == "watches for women":
        watch.click()
        break

assert driver.find_element(By.ID, "twotabsearchtextbox").get_attribute("value") == 'watches for women'
driver.find_element(By.XPATH, "//div[@id='brandsRefinements']//li//span//div//a//span[text()='See more']").click()
brands = driver.find_elements(By.CSS_SELECTOR, "div[id='brandsRefinements'] ul li")
for brand in brands:
    print(brand.text)
    if brand.text == "helix":
        driver.find_element(By.CSS_SELECTOR,
                            "div[id='brandsRefinements'] li[aria-label=" + brand.text + "] i[class='a-icon "
                                                                                        "a-icon-checkbox']").click()
        break

brands_cat = driver.find_elements(By.CSS_SELECTOR, "div[id='brandsRefinements'] ul li")
for brand_cat in brands_cat:
    print(brand_cat.text)
    if brand_cat.text == "helix":
        assert driver.find_element(By.CSS_SELECTOR,
                                           "div[id='brandsRefinements'] li[aria-label=" + brand_cat.text + "] i[class='a"
                                                                                                        "-icon "
                                                                                                        "a-icon"
                                                                                                        "-checkbox']").is_selected()
        break
driver.close()
