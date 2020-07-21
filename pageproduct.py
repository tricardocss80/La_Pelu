from selenium.webdriver.common.by import By
from pagecommonmethods import PageCommonMethods


class Pageproduct(PageCommonMethods):
    def __init__(self, driver):
        super().__init__(driver)
        self.productos_menu = (By.XPATH, '//li[@class="nav-item nav-dropdown"][contains(.,"Productos")]')
        self.listado = (By.XPATH, '//a[@class="nav-link"][contains(.,"Listado")]')
        self.input_name = (By.XPATH, '//input[@name="name"]')
        self.input_cost = (By.XPATH, '//input[@name="cost"]')
        self.intput_price = (By.XPATH, '//input[@name="price"]')
        self.intput_total = (By.XPATH, '//input[@placeholder="Cantidad"]')
        self.intput_minimum = (By.XPATH, '//input[@placeholder="Mínimo"]')
        self.driver = driver

    def menu_click_products(self):
        self.wait_clickable(self.productos_menu).click()

    def menu_click_products_list(self):
        self.wait_clickable(self.listado).click()

    def form_new_product(self, data_product):
        self.wait_presence(self.input_name).send_keys(data_product['name'])
        self.wait_presence(self.input_cost).send_keys(data_product['cost'])
        self.wait_presence(self.intput_price).send_keys(data_product['price'])
        self.wait_presence(self.intput_total).send_keys(data_product['total'])
        self.wait_presence(self.intput_minimum).send_keys(data_product['minimum'])
