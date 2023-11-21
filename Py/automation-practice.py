from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep

# launch browser
driver = webdriver.Chrome()

# maximize browser
driver.maximize_window()

# navigate to website
driver.get('https://www.saucedemo.com')

# wait for page to load before execute
# driver.implicitly_wait(5)




# find the elements
username = driver.find_element(By.ID, 'user-name')
password = driver.find_element(By.ID, 'password')
login_button = driver.find_element(By.ID, 'login-button')

##### TEST STEPS #####
#  enter username and password and click login

username.send_keys('standard_user') 
password.send_keys('secret_sauce')
login_button.click()


# verification
driver.implicitly_wait(5)
if 'products' in driver.page_source.lower():
    print('Test Case Passed')
    driver.save_screenshot('login_pass.png')
else:
    print('Test Case Failed')
    driver.save_screenshot('login_fail.png')

# pause

sleep(5)
