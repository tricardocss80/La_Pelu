from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class Pagelogin:
    def __init__(self, driver):
        self.input_email = (By.NAME, 'email')
        self.input_password = (By.NAME, 'password')
        self.aceptar_button = (By.XPATH, '//button[@type="submit"]')
        self.driver = driver

    def login(self, data):
        email = WebDriverWait(self.driver, 30).until(EC.presence_of_element_located(self.input_email))
        email.clear()
        email.send_keys(data['email'])
        password = WebDriverWait(self.driver, 30).until(EC.presence_of_element_located(self.input_password))
        password.clear()
        password.send_keys(data['password'])
        aceptar_button = WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable(self.aceptar_button))
        aceptar_button.click()


