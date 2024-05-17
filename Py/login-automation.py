from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from time import sleep

#storing url and credentials
url = 'https://www.saucedemo.com'
valid_username = 'standard_user'
valid_password = 'secret_sauce'
invalid_username = 'user_user'
invalid_password = 'secret_secret'

#initialize webdriver
def initialize_driver():
    options = Options()
    options.add_experimental_option('detach', True)
    driver = webdriver.Chrome(options=options)
    driver.maximize_window()
    driver.get(url)
    return driver

def find_elements(driver):
    login_elements = {
    "username": driver.find_element(By.XPATH, '//*[@id="user-name"]'),
    "password": driver.find_element(By.XPATH, '//*[@id="password"]'),
    "login_button": driver.find_element(By.XPATH, '//*[@id="login-button"]')
    }
    return login_elements

def valid_login(elements):
    elements["username"].send_keys(valid_username)
    elements["password"].send_keys(valid_password)
    elements["login_button"].click()
    driver.implicitly_wait(30)
    if 'products' in driver.page_source.lower():
        print('\033[32mTest 1 Passed\033[0m')
        driver.save_screenshot('test1-login_pass.png')
    else:
        print('\033[31mTest 1 Failed\033[0m')
        driver.save_screenshot('test1-login_fail.png')
    sleep(3)
    driver.quit()
    return

def invalid_login(elements):
    elements["username"].send_keys(invalid_username)
    elements["password"].send_keys(invalid_password)
    elements["login_button"].click()
    driver.implicitly_wait(30)
    if 'username and password do not match any user in this service' in driver.page_source.lower():
        print('\033[32mTest 2 Passed\033[0m')
        driver.save_screenshot('test2-login_pass.png')
    else:
        print('\033[31mTest 2 Failed\033[0m')
        driver.save_screenshot('test2-login_fail.png')
    return

#start of test execution
driver = initialize_driver()
elements = find_elements(driver)
test_1 = valid_login(elements)

#test 2 execution
driver = initialize_driver()
elements = find_elements(driver)
test_2 = invalid_login(elements)




