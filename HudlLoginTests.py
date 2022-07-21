from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import NoSuchElementException
import time

"""Testing Login with Valid Email and Password"""

emailStr = 'ENTER A VALID E-MAIL ADDRESS'
passwordStr = 'ENTER YOUR PASSWORD'

# Open browser to hudl
driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get("http://hudl.com/")
driver.maximize_window()

# Locate and select 'Log In' button
Log_In = driver.find_element(By.CSS_SELECTOR, 'body > div.outer > header > div > a.mainnav__btn.mainnav__btn--primary').click()

# Input valid email and password
email = driver.find_element(By.ID, 'email').send_keys(emailStr)
password = driver.find_element(By.ID, 'password').send_keys(passwordStr)

# Locate and submit 'Log In' button
LoginButton = driver.find_element(By.ID, 'logIn').click()
time.sleep(5)

# Validate the 'Home' button is now present on page to ensure User is logged in successfully
try:
    driver.find_element(By.CSS_SELECTOR,
                        '#ssr-webnav > div > div.hui-webnav__grid.hui-navcontainer > nav.hui-webnav__grid-col--onewhole.hui-globalnav.uni-env--dark.uni-environment--dark > div:nth-child(2) > a.hui-globalnav__item.hui-globalnav__home')
    print('Successfully logged in!')

except NoSuchElementException:
    print('Login failed.')

"""Testing a Log Out"""

# Hover over dropdown and select 'Log Out'
a = ActionChains(driver)
m = driver.find_element(By.CSS_SELECTOR,
                        '#ssr-webnav > div > div.hui-webnav__grid.hui-navcontainer > nav.hui-webnav__grid-col--onewhole.hui-globalnav.uni-env--dark.uni-environment--dark > div:nth-child(4) > div.hui-globalusermenu > div.hui-globaluseritem > div.hui-globaluseritem__display-name > svg')
a.move_to_element(m).perform()
n = driver.find_element(By.CSS_SELECTOR,
                        '#ssr-webnav > div > div.hui-webnav__grid.hui-navcontainer > nav.hui-webnav__grid-col--onewhole.hui-globalnav.uni-env--dark.uni-environment--dark > div:nth-child(4) > div.hui-globalusermenu > div.hui-globalusermenu__items > div.hui-globaladditionalitems.hui-globaladditionalitems--not-phone > a')
a.move_to_element(n).click().perform()

# Validate you are back on hudl.com home page
try:
    driver.find_element(By.CSS_SELECTOR,
                        'body > div.outer > header > div > a.mainnav__btn.mainnav__btn--primary')
    print('Successfully logged out')

except NoSuchElementException:
    print('Still logged in :(')

driver.close()


"""Testing Login with Invalid Email and Password"""

class InvalidUserLogin:

    url = 'https://www.hudl.com/'
    invalid_email = 'abc@randomemail.com'
    invalid_password = 'abcdefg123'

    # Open browser
    def __init__(self):
        self.driver = webdriver.Chrome(ChromeDriverManager().install())
        self.driver.implicitly_wait(10)
        self.driver.maximize_window()

    # Navigate to Hudl
    def go_to_url(self):
        self.driver.get(self.url)

    # Find and select 'Log In' button
    def go_to_login(self):
        self.driver.find_element(By.CSS_SELECTOR,
                                 'body > div.outer > header > div > a.mainnav__btn.mainnav__btn--primary').click()

    # Enter an invalid email
    def input_email(self):
        field = self.driver.find_element(By.ID, 'email')
        field.send_keys(self.invalid_email)

    # Enter an invalid password
    def input_password(self):
        field = self.driver.find_element(By.ID, 'password')
        field.send_keys(self.invalid_password)

    # Submit 'Log In' button
    def click_login(self):
        self.driver.find_element(By.ID, 'logIn').click()

    # Verify the error message is displayed and validate user isn't logged in
    def verify_error_message(self):
        try:
            self.driver.find_element(By.CSS_SELECTOR,
                                     '#app > section > div.styles_pageContainer_31NnIgZuiQzDKnKlPaGLsi > div > form > div > div.styles_errorDisplayContainer_3nEnTm0RU51coAPEZflqgB.styles_fadeInAndExpand_3sKGRFzwMPUqIvcy9T4nFM > div > p')
            print('Invalid email and/or password.')
            return False
        except NoSuchElementException:
            print('Login successful!')
            return True


    def main(self):
        self.go_to_url()
        self.go_to_login()
        self.input_email()
        self.input_password()
        self.click_login()
        time.sleep(3)
        self.verify_error_message()
        self.driver.quit()


if __name__ == '__main__':

    object = InvalidUserLogin()
    object.main()


"""Testing Login when No Email or Password are given"""

class NoEmailOrPasswordProvided:

    url = 'https://www.hudl.com/'
    invalid_email = ''
    invalid_password = ''

    # Open browser
    def __init__(self):
        self.driver = webdriver.Chrome(ChromeDriverManager().install())
        self.driver.implicitly_wait(10)
        self.driver.maximize_window()

    # Navigate to Hudl
    def go_to_url(self):
        self.driver.get(self.url)

    # Find and select 'Log In' button
    def go_to_login(self):
        self.driver.find_element(By.CSS_SELECTOR,
                                 'body > div.outer > header > div > a.mainnav__btn.mainnav__btn--primary').click()

    # Enter an invalid email
    def input_email(self):
        field = self.driver.find_element(By.ID, 'email')
        field.send_keys(self.invalid_email)

    # Enter an invalid password
    def input_password(self):
        field = self.driver.find_element(By.ID, 'password')
        field.send_keys(self.invalid_password)

    # Submit 'Log In' button
    def click_login(self):
        self.driver.find_element(By.ID, 'logIn').click()

    # Verify the error message is displayed and validate user isn't logged in
    def verify_error_message(self):
        try:
            self.driver.find_element(By.CSS_SELECTOR,
                                     '#app > section > div.styles_pageContainer_31NnIgZuiQzDKnKlPaGLsi > div > form > div > div.styles_errorDisplayContainer_3nEnTm0RU51coAPEZflqgB.styles_fadeInAndExpand_3sKGRFzwMPUqIvcy9T4nFM > div > p')
            print('No email or password given.')
            return False
        except NoSuchElementException:
            print('Login successful!')
            return True


    def main(self):
        self.go_to_url()
        self.go_to_login()
        self.input_email()
        self.input_password()
        self.click_login()
        time.sleep(3)
        self.verify_error_message()
        self.driver.quit()


if __name__ == '__main__':

    object = NoEmailOrPasswordProvided()
    object.main()
