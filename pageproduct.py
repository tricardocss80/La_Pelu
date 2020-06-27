from selenium.webdriver.common.by import By
from page_common_methods import PageCommonMethods


class Pageproduct(PageCommonMethods):
    def __init__(self, driver):
        super().__init__(driver)
        self.productos_menu = (By.XPATH, '//li[@class="nav-item nav-dropdown"][contains(.,"Productos")]')
        self.listado = (By.XPATH, '//a[@class="nav-link"][contains(.,"Listado")]')
        self.new_botton = (By.CLASS_NAME, 'card-header-actions')
        self.input_name = (By.XPATH, '//input[@name="name"]')
        self.input_cost = (By.XPATH, '//input[@name="cost"]')
        self.intput_price = (By.XPATH, '//input[@name="price"]')
        self.intput_total = (By.XPATH, '//input[@placeholder="Cantidad"]')
        self.intput_minimum = (By.XPATH, '//input[@placeholder="Mínimo"]')
        self.button_guardar = (By.XPATH, '//button[contains(@type,"submit")]')
        self.quantity_product = (By.XPATH, '//div[@class="pagination"]//ul[@class="nav"]')
        self.driver = driver

    def menu_click_products(self):
        self.wait_clickable(self.productos_menu).click()

    def menu_click_products_list(self):
        self.wait_clickable(self.listado).click()

    def new_product(self):
        self.wait_clickable(self.new_botton).click()

    def form_new_product(self, data_product):
        self.wait_presence(self.input_name).send_keys(data_product['name'])
        self.wait_presence(self.input_cost).send_keys(data_product['cost'])
        self.wait_presence(self.intput_price).send_keys(data_product['price'])
        self.wait_presence(self.intput_total).send_keys(data_product['total'])
        self.wait_presence(self.intput_minimum).send_keys(data_product['minimum'])
        self.wait_clickable(self.button_guardar).click()

    def quantity_products(self):
        try:
            quantity_products = self.driver.find_element(*self.quantity_product)
            self.driver.save_screenshot('time_error.png')
            return int(quantity_products.text.replace('Total: ', ''))
        except Exception as e:
            print(e)
            return 0

