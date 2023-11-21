from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()

driver.maximize_window()

driver.get('https://demo.seleniumeasy.com/jquery-download-progress-bar-demo.html')

driver.implicitly_wait(8)

download_button = driver.find_element(By.ID, 'downloadButton')
download_button.click()



try:
    progress_bar = WebDriverWait(driver, 30).until(
        EC.text_to_be_present_in_element(
            (By.CLASS_NAME, 'progress-label'), # element filtration
            'Complete!' # text result
        )
    )
    print('Test Passed')
except Exception as e:
    print('Test Failed', e)