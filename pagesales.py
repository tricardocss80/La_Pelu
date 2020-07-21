from selenium.webdriver.common.by import By
from pagecommonmethods import PageCommonMethods


class Pagesales(PageCommonMethods):
    def __init__(self, driver):
        super().__init__(driver)
        self.sales_menu = (By.XPATH, '//li[@class="nav-item"][contains(.,"Ventas")]')
        self.button_new = (By.XPATH, '//a[contains(.,"Nueva")]')
        self.loading = (By.XPATH, '//div[@class="overlay"]')
        self.delete_button = (By.XPATH, '(//button[contains(text(),"Eliminar")])[1]')
        self.accept_button = (By.XPATH, '//button[@class="btn btn-danger"]')
        self.driver = driver

    def sale_menu(self):
        self.wait_clickable(self.sales_menu).click()

    def click_button_new_sale(self):
        self.wait_clickable(self.button_new).click()

    def click_delete_sale(self):
        self.wait_clickable(self.delete_button).click()
        self.wait_clickable(self.accept_button).click()

