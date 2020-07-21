from selenium.webdriver.common.by import By
from pagecommonmethods import PageCommonMethods


class Pagesales(PageCommonMethods):
    def __init__(self, driver):
        super().__init__(driver)
        self.sales_menu = (By.XPATH, '//li[@class="nav-item"][contains(.,"Ventas")]')
        self.button_new = (By.XPATH, '//a[contains(.,"Nueva")]')
        self.quantity_sales_locator = (By.XPATH, '//div[@class="pagination"]//ul[@class="nav"]')
        self.loading = (By.XPATH, '//div[@class="overlay"]')
        self.eliminar_button = (By.XPATH, '(//button[contains(text(),"Eliminar")])[1]')
        self.aceptar_button = (By.XPATH, '//button[@class="btn btn-danger"]')
        self.driver = driver

    def sale_menu(self):
        self.wait_clickable(self.sales_menu).click()

    def click_button_new_sale(self):
        self.wait_clickable(self.button_new).click()

    def click_delete_sale(self):
        self.wait_clickable(self.eliminar_button).click()
        self.wait_clickable(self.aceptar_button).click()

    def quantity_sales(self):
        try:
            quantity_sale = self.driver.find_element(*self.quantity_sales_locator)
            return int(quantity_sale.text.replace('Total: ', ''))
        except Exception as e:
            print(e)
            return 0


