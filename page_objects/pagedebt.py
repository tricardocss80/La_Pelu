from selenium.webdriver.common.by import By
from page_objects.pagecommonmethods import PageCommonMethods


class PageDebt(PageCommonMethods):
    def __init__(self, driver):
        super().__init__(driver)
        self.button_report = (By.XPATH, '//a[contains(text(),"Reporte")]')
        self.button_debt = (By.XPATH, '//a[contains(text(),"Deudas")]')
        self.button_pay = (By.XPATH, '//button[contains(.,"Pagar")]')
        self.intput_method_payment = (By.XPATH, '//div[contains(text(),"Efectivo")]')
        self.driver = driver

    def click_menu_report(self):
        self.wait_clickable(self.button_report).click()

    def click_menu_dedt(self):
        self.wait_clickable(self.button_debt).click()

    def click_button_pay(self):
        self.wait_clickable(self.button_pay).click()

    def click_method(self):
        self.wait_clickable(self.intput_method_payment).click()


