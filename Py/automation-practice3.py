from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from time import sleep

driver = webdriver.Chrome()
driver.maximize_window()

driver.get('https://demo.seleniumeasy.com/basic-first-form-demo.html')

driver.implicitly_wait(8)

# find elements

single_input_text = 'Hello World'
two_input_text1 = 15
two_input_text2 = 20

# find elements

single_input = driver.find_element(By.ID, 'user-message')
single_input_display = driver.find_element(By.ID, 'display')
show_message = driver.find_element(By.XPATH, "//button[contains(text(), 'Show Message')]")

two_input_field1 = driver.find_element(By.ID, 'value1')
two_input_field2 = driver.find_element(By.ID, 'value2')
two_input_field_display = driver.find_element(By.ID, 'displayvalue')
get_total = driver.find_element(By.XPATH, "//button[contains(text(), 'Get Total')]")


# enter on input fields and click button

single_input.send_keys(single_input_text)
show_message.click()

two_input_field1.send_keys(two_input_text1)
two_input_field2.send_keys(two_input_text2)
get_total.click()

# calculate total
total = two_input_text1 + two_input_text2

# Verify output
try:
    if single_input_display.text == single_input_text and str(total) == two_input_field_display.text:
        print('Test Passed')
    else:
        print('Test Failed')
except Exception as e:
    print('An error occurred:', str(e))

sleep(5)