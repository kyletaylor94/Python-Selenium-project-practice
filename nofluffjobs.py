from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from bs4 import BeautifulSoup
import requests
import xml

'''Its just a practice with selenium,
it does not work every method yet!'''

#nofluffjobs

execuble_path = "/Users/csaba/Desktop/development/selenium webdriver/chromedriver"
options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)

driver = webdriver.Chrome(executable_path=execuble_path, options=options)





driver.get("https://nofluffjobs.com/hu")
driver.implicitly_wait(10)
cookies_accept = driver.find_element(By.XPATH, '/html/body/div/div[3]/div/div/div[2]/div/div/button')
cookies_accept.click()
try:
    search_field = driver.find_element(By.XPATH, '/html/body/nfj-root/nfj-layout/div[2]/div/div/nfj-search-box/form/mat-form-field')
    search_field.send_keys('junior developer')
finally:
    another_field = driver.find_element(By.CSS_SELECTOR, '#mat-chip-list-input-1')
    another_field.send_keys('junior developer')
search_field_button = driver.find_element(By.XPATH, '/html/body/nfj-root/nfj-layout/div[2]/div/div/nfj-search-box/form/mat-form-field/div/div[1]/div[1]/mat-chip-list/div/div[1]/button')
search_field_button.click()