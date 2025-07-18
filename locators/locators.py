from selenium.webdriver.common.by import By

authorization = (By.CLASS_NAME, 'authorization-link')
input_email = (By.XPATH, '//*[@id="email"]')
input_password = (By.XPATH, '//*[@id="pass"]')
submit = (By.XPATH, '//*[@id="send2"]')
message = (By.XPATH, '//*[@id="maincontent"]/div[2]/div[2]/div/div/div/text()')