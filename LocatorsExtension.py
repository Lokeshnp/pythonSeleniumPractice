from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

ser_obj = Service("D:/Software/chromedriver.exe")
driver = webdriver.Chrome(service=ser_obj)
driver.maximize_window()
# driver.get("https://rahulshettyacademy.com/client")
# driver.find_element(By.LINK_TEXT, "Forgot password?").click()
# driver.find_element(By.XPATH, "//form/div[1]/input").send_keys("demo@gmail.com")
# driver.find_element(By.CSS_SELECTOR, "form div:nth-child(2) input").send_keys("Welcome@123")
# driver.find_element(By.CSS_SELECTOR, "#confirmPassword").send_keys("Welcome@123")
#driver.find_element(By.XPATH, "//button[@type='submit']").click()
#Finding using text value facility is not present in CSS
# driver.find_element(By.XPATH, "//button[text()='Save New Password']").click()

#select value in static dropdown
driver.get("https://www.amazon.in/")
dropdown=Select(driver.find_element(By.ID, "searchDropdownBox"))
dropdown.select_by_visible_text('Music')
dropdown.select_by_value('search-alias=furniture')
dropdown.select_by_index(0)



