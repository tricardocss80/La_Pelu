from selenium.webdriver.common.by import By
from pagecommonmethods import PageCommonMethods
import time


class PagePayment(PageCommonMethods):
    def __init__(self, driver):
        super().__init__(driver)
        self.config_button = (By.XPATH, '//a[contains(.,"Configuración")]')
        self.payment_method_button = (By.XPATH, '//li[@class="nav-item"][contains(.,"Métodos de pago")]')
        self.intput_name = (By.XPATH, '//input[@placeholder="Nombre"]')
        self.driver = driver

    def click_button_config(self):
        self.wait_clickable(self.config_button).click()

    def click_button_payment(self):
        self.wait_clickable(self.payment_method_button).click()

    def intput_payment_method(self, data):
        self.wait_presence(self.intput_name).send_keys(data['name'])



        time.sleep(2)


