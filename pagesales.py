from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

class Pagesales:
    def __init__(self, driver):
        self.ventas_menu = (By.XPATH, '//li[@class="nav-item"][contains(.,"Ventas")]')
        self.button_new = (By.XPATH, '//a[contains(.,"Nueva")]')
        self.intput_client_locator = (By.XPATH, '//input[contains(@autocomplete,"off")]')
        self.intput_client_list = (By.XPATH, '//input[contains(@aria-autocomplete,"list")]')
        self.button_plus_product = (By.XPATH, '//button[contains(text(),"+ Producto")]')
        self.intput_item_employees = (By.XPATH, '//div[contains(@class,"EmployeesListComponent")]')
        self.intput_item_employees_list = (By.XPATH, '//div[contains(@class,"css-b8bncs-singleValue")]')
        self.intput_item_products_locator = (By.XPATH, '//div[@class="css-1pcexqc-container ProductsListComponent '
                                                       'full-width"]//div[@class="css-bg1rzq-control"]//div[@class="'
                                                       'css-1hwfws3"]//div[@class="css-1g6gooi"]//input')
        self.intput_item_products_list = (By.XPATH, '//div[@class="css-dpec0i-option"]')

        self.intput_item_products_quantity = (By.XPATH, '//input[@name="quantity"]')

        self.intput_item_products_price = (By.XPATH, '//input[contains(@name,"price")]')


        self.quantity_ventas = (By.XPATH, '//div[@class="pagination"]//ul[@class="nav"]')
        self.loading = (By.XPATH, '//div[@class="overlay"]')
        self.eliminar_button = (By.XPATH, '(//button[contains(text(),"Eliminar")])[1]')
        self.aceptar_button = (By.XPATH, '//button[@class="btn btn-danger"]')
        self.driver = driver

    def venta_menu(self):
        menu_venta = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(self.ventas_menu))
        WebDriverWait(self.driver, 10).until(EC.invisibility_of_element(self.loading))
        menu_venta.click()

    def click_new_sale(self):
        button_new = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(self.button_new))
        button_new.click()

    def form_new_sales(self, client):
        self.driver.find_element(*self.intput_client_locator).send_keys(client)
        self.driver.find_element(*self.intput_client_list).click()
        button_plus_product = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(self.button_plus_product))
        button_plus_product.click()

    def sub_form_product(self, product):
        self.driver.find_element(*self.intput_item_employees).click()
        self.driver.find_element(*self.intput_item_employees_list).click()
        self.driver.find_element(*self.intput_item_products_locator).send_keys(product['product'])
        self.driver.find_element(*self.intput_item_products_list).click()
        self.driver.find_element(*self.intput_item_products_quantity).clear()
        self.driver.find_element(*self.intput_item_products_quantity).send.keys(product['quantity'])
        #    self.driver.find_element(*self.intput_item_products_price).send.keys(product['price'])
        #    time.sleep(3)

    def quantity_sale(self):
        quantity_venta = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(self.quantity_ventas))
        return int(quantity_venta.text.replace('Total: ', ''))

    def click_delete_venta(self):
        eliminar_button = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(self.eliminar_button))
        eliminar_button.click()
        aceptar_button = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(self.aceptar_button))
        aceptar_button.click()



