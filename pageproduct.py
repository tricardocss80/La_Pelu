from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class Pageproduct:
    def __init__(self, driver):
        self.productos_menu = (By.XPATH, '//li[@class="nav-item nav-dropdown"][contains(.,"Productos")]')
        self.loading = (By.XPATH, '//div[@class="overlay"]')
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

    def menu_click_producto(self):
        menu_productos = WebDriverWait(self.driver, 30).until(EC.presence_of_element_located(self.productos_menu))
        WebDriverWait(self.driver, 30).until(EC.invisibility_of_element(self.loading))
        menu_productos.click()
        listado = WebDriverWait(self.driver, 30).until(EC.presence_of_element_located(self.listado))
        WebDriverWait(self.driver, 30).until(EC.invisibility_of_element(self.loading))
        listado.click()

    def new_product(self):
        new_botton = WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable(self.new_botton))
        new_botton.click()

    def form_new_product(self, data_product):
        intput_name = WebDriverWait(self.driver, 30).until(EC.presence_of_element_located(self.input_name))
        intput_name.send_keys(data_product['name'])
        intput_cost = WebDriverWait(self.driver, 30).until(EC.presence_of_element_located(self.input_cost))
        intput_cost.send_keys(data_product['cost'])
        intput_price = WebDriverWait(self.driver, 30).until(EC.presence_of_element_located(self.intput_price))
        intput_price.send_keys(data_product['price'])
        intput_total = WebDriverWait(self.driver, 30).until(EC.presence_of_element_located(self.intput_total))
        intput_total.send_keys(data_product['total'])
        intput_minimum = WebDriverWait(self.driver, 30).until(EC.presence_of_element_located(self.intput_minimum))
        intput_minimum.send_keys(data_product['minimum'])
        button_guardar = WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable(self.button_guardar))
        button_guardar.click()

    def quantity_products(self):
        quantity_products = WebDriverWait(self.driver, 30).until(EC.presence_of_element_located(self.quantity_product))
        return int(quantity_products.text.replace('Total: ', ''))
