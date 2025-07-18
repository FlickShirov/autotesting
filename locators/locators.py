from selenium.webdriver.common.by import By

authorization = (By.CLASS_NAME, 'authorization-link')
input_email = (By.XPATH, '//*[@id="email"]')
input_password = (By.XPATH, '//*[@id="pass"]')
submit = (By.XPATH, '//*[@id="send2"]')