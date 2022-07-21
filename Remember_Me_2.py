from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
import selenium.webdriver
import time
import os
import pickle

service = Service(r'C:\Users\Jakade\Python\chromedriver.exe')
driver = webdriver.Chrome(service=service)
emailStr = 'ENTER A VALID EMAIL ADDRESS'
passwordStr = 'ENTER YOUR PASSWORD'


driver.get("http://hudl.com/")
driver.maximize_window()
Log_In = driver.find_element(By.CSS_SELECTOR, 'body > div.outer > header > div > a.mainnav__btn.mainnav__btn--primary').click()
email = driver.find_element(By.ID, 'email').send_keys(emailStr)
password = driver.find_element(By.ID, 'password').send_keys(passwordStr)
rememberMe = driver.find_element(By.CSS_SELECTOR, '#app > section > div.styles_pageContainer_31NnIgZuiQzDKnKlPaGLsi > div > form > div > div.styles_footerContainer_bNIg7bOb-wpsYiG0CCy0M > div > label > svg > rect.uni-form__check-indicator__background').click()
LoginButton = driver.find_element(By.ID, 'logIn').click()
time.sleep(5)


pickle.dump(driver.get_cookies(), open(r"C:\Users\Andrea\PycharmProjects\pythonProject\venv\my_file.pkl", "wb"))
driver.close()

time.sleep(2)

cookies = pickle.load(open(r"C:\Users\Andrea\PycharmProjects\pythonProject\venv\my_file.pkl", "rb"))
for cookie in cookies:
    driver.add_cookie(cookie)
driver.get("https://hudl.com/")
time.sleep(2)
# driver.close()


