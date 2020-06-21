from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


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
        self.intput_minimo = (By.XPATH, '//input[@placeholder="Mínimo"]')
        self.button_guardar = (By.XPATH, '//button[contains(@type,"submit")]')
        self.quantity_product = (By.XPATH, '//div[@class="pagination"]//ul[@class="nav"]')




        self.driver = driver



    def menu_click_producto(self):
        menu_productos = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(self.productos_menu))
        WebDriverWait(self.driver, 10).until(EC.invisibility_of_element(self.loading))
        menu_productos.click()
        listado = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(self.listado))
        listado.click()

    def new_producto(self):
        new_botton = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(self.new_botton))
        WebDriverWait(self.driver, 10).until(EC.invisibility_of_element(self.loading))
        new_botton.click()
        time.sleep(2)

    def form_new_producto(self, data_product):
        self.driver.find_element(*self.input_name).send_keys(data_product['name'])
        self.driver.find_element(*self.input_cost).send_keys(data_product['cost'])
        self.driver.find_element(*self.intput_price).send_keys(data_product['price'])
        self.driver.find_element(*self.intput_total).send_keys(data_product['total'])
        self.driver.find_element(*self.intput_minimo).send_keys(data_product['minimum'])
        button_guardar = WebDriverWait(self.driver, 4).until(EC.element_to_be_clickable(self.button_guardar))
        button_guardar.click()
        time.sleep(2)

    def quantity_products(self):
        quantity_products = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(self.quantity_product))
        return int(quantity_products.text.replace('Total: ', ''))
