from selenium.webdriver.common.by import By
from page_objects.pagecommonmethods import PageCommonMethods


class PagePayment(PageCommonMethods):
    def __init__(self, driver):
        super().__init__(driver)
        self.config_button = (By.XPATH, '//a[contains(.,"Configuración")]')
        self.payment_method_button = (By.XPATH, '//li[@class="nav-item"][contains(.,"Métodos de pago")]')
        self.intput_name = (By.XPATH, '//input[@placeholder="Nombre"]')
        self.assert_new_payment = (By.XPATH, '//td[contains(text(),"Tarjeta de crédito")]')
        self.error = (By.XPATH, '//div[@class="toast-message"]')
        self.button_deactivate = (By.XPATH, '(//button[contains(.,"Desactivar")])[2]')
        self.driver = driver

    def click_button_config(self):
        self.wait_clickable(self.config_button).click()

    def click_button_payment(self):
        self.wait_clickable(self.payment_method_button).click()

    def intput_payment_method(self, sale_data):
        self.wait_presence(self.intput_name).send_keys(sale_data)

    def asser_error(self):
        return self.wait_presence(self.error).text

    def assert_new_payment_method(self):
        return self.wait_presence(self.assert_new_payment).text

    def deactivate_button(self):
        self.wait_clickable(self.button_deactivate).click()


