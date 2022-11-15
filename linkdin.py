from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
import time
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.ui import WebDriverWait

'''Its just a practice with selenium,
it does not work every method yet!'''

#linkdin

EMAIL = "example" 
PASSWORLD = "example2"

execuble_path = "/Users/csaba/Desktop/development/selenium webdriver/chromedriver"

driver = webdriver.Chrome(executable_path=execuble_path)



driver.get("https://www.linkedin.com/feed/")


#find elements:

def search_elements_and_execute():
    sign_button1 = driver.find_element(By.XPATH, '/html/body/div[2]/main/p[1]/a')
    driver.implicitly_wait(8)
    sign_button1.send_keys(Keys.ENTER)
    email_field = driver.find_element(By.XPATH, '/html/body/div/main/div[3]/div[1]/form/div[1]/input')
    email_field.click()
    email_field.send_keys(EMAIL)
    password_field = driver.find_element(By.XPATH, '/html/body/div/main/div[3]/div[1]/form/div[2]/input')
    password_field.click()
    password_field.send_keys(PASSWORLD)
    sign_button2 = driver.find_element(By.XPATH, '/html/body/div/main/div[3]/div[1]/form/div[3]/button')
    sign_button2.click()
    sign_button2.send_keys(Keys.ENTER)

    driver.refresh()
    try:
        WebDriverWait(driver, 90)
        search_field= driver.find_element(By.XPATH, "/html/body/div[6]/header/div/div/div/div[1]/input")
        search_field.send_keys('Junior Python developer')
        search_field.send_keys(Keys.ENTER)
    finally:
        pass




search_elements_and_execute()