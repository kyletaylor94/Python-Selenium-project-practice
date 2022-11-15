from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from bs4 import BeautifulSoup
import requests
import xml

'''Its just a practice with selenium,
it does not work every method yet!'''

#profession.hu

execuble_path = "/Users/csaba/Desktop/development/selenium webdriver/chromedriver"
options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)

driver = webdriver.Chrome(executable_path=execuble_path, options=options)

driver.implicitly_wait(10)



driver.get("https://www.profession.hu/")
driver.implicitly_wait(60)
cookie = driver.find_element(By.XPATH, '/html/body/div[1]/div[2]/div[2]/div[2]/a[1]')
cookie.click()
jobs_input = driver.find_element(By.XPATH, '/html/body/div[1]/header/div/div[5]/div/form/div[1]/div/input')
jobs_input.click()
jobs_input.send_keys('programozó')
city = driver.find_element(By.XPATH, '/html/body/div[1]/header/div/div[5]/div/form/div[2]/div/input')
city.click()
city.send_keys('Budapest')
search_button = driver.find_element(By.XPATH, '/html/body/div[1]/header/div/div[5]/div/form/div[3]/input')
search_button.click()

#detailed searching by salary
detailed_searching_button = driver.find_element(By.XPATH, '/html/body/div[1]/header/div/div[5]/div/form/div[4]/a')
detailed_searching_button.click()
with_salary_button = driver.find_element(By.XPATH, '/html/body/div[1]/main/div[2]/div/form/div/div[1]/div[7]/div/div[1]/div/div[2]/label')
with_salary_button.click()
start_searching = driver.find_element(By.XPATH, '/html/body/div[1]/main/div[2]/div/form/div/div[2]/input')
start_searching.click()

prices = driver.find_elements(By.CLASS_NAME, 'advertisement_tag job-card__tag job-card__tag--stress-call')
print(prices)

