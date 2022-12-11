from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

ser_obj = Service("D:/Software/chromedriver.exe")
driver = webdriver.Chrome(service=ser_obj)
driver.maximize_window()
#ID, XPATH, CSSSelector, Classname, name, text


# driver.get("https://login.yahoo.com/account/create?.intl=in&src=ym&specId=yidregsimplified&done=https%3A%2F%2Fmail.yahoo.com")


# driver.find_element(By.ID, "usernamereg-firstName").send_keys("Lokesh")
# driver.find_element(By.ID, "usernamereg-lastName").send_keys("Np")
# # driver.find_element(By.NAME, "userId").send_keys("nplokesh89")
# driver.find_element(By.XPATH, "//input[@type='tel']").send_keys("1993")
# driver.find_element(By.NAME, "signup").click()
# message=driver.find_element(By.CLASS_NAME, "oneid-error-message").text
# print(message)
# assert "This is required" in message
# assert "required" in message
# driver.close()




#Best Chrome Plugin Selector Hub
driver.get("https://in.search.yahoo.com/?fr2=inr")
# driver.find_element(By.XPATH, "(//a[@class='thmb '])[2]").click()
# message=driver.title
# print(message)
# assert "coronavirus" in message


driver.find_element(By.XPATH, "//div[@title='Sign In']").click()
driver.find_element(By.CLASS_NAME, "phone-no").send_keys("lokeshnp7679@gmail.com")
# driver.find_element(By.CLASS_NAME, "phone-no").clear()
# # XPATH -> //tagNAme[@attribute='value'] -> //input[@type='checkbox']
#XPATH -> (//a[@class='thmb '])[2] by giving index number top to bottom when more element with same tag value
# # CSS -> tagNAme[attribute='value'] -> //input[@type='checkbox'],
# # CSS For ID -> #id -> #mbr-forgot-link
# # CSS For Class -> .Classname -> .phone-no
# flag = driver.find_element(By.NAME, "persistent").is_enabled()
# print(flag)
# driver.find_element(By.CSS_SELECTOR, "label[for='persistent']").click()
# driver.find_element(By.ID, "login-signin").click()
driver.close()

