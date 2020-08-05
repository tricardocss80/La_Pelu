from selenium.webdriver.common.by import By
from page_objects.pagecommonmethods import PageCommonMethods


class Pagelogin(PageCommonMethods):
    def __init__(self, driver):
        super().__init__(driver)
        self.input_email = (By.NAME, 'email')
        self.input_password = (By.NAME, 'password')
        self.aceptar_button = (By.XPATH, '//button[@type="submit"]')
        self.driver = driver

    def login(self, data):
        email = self.wait_presence(self.input_email)
        email.clear()
        email.send_keys(data['email'])
        password = self.wait_presence(self.input_password)
        password.clear()
        password.send_keys(data['password'])
        self.wait_clickable(self.aceptar_button).click()


