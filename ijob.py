from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service


execuble_path = "/Users/csaba/Desktop/development/selenium webdriver/chromedriver"

driver = webdriver.Chrome(executable_path=execuble_path)

driver.implicitly_wait(10)

driver.get("https://ijob.hu/kapcsolat/")

jobs = driver.find_element(By.XPATH, '/html/body/div[2]/div[2]/header/div[1]/div[3]/div/nav[1]/ul/li[5]/a/span')
jobs.click()
driver.implicitly_wait(20)

search_field = driver.find_element(By.XPATH, '/html/body/div[2]/div[2]/main/div/section/div/div/div[1]/div/div[2]/div/form/div[1]/div[1]/label/input')
search_field.click()
search_field.send_keys('Junior')
search_field.send_keys(Keys.ENTER)