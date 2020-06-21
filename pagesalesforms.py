from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


class Pagesalesforms:
    def __init__(self, driver):
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
        self.button_item_products_save = (By.XPATH, '//button[contains(.,"Agregar")]')
        self.driver = driver

    def form_new_sales(self, client):
        self.driver.find_element(*self.intput_client_locator).send_keys(client)
        self.driver.find_element(*self.intput_client_list).click()
        button_plus_product = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.button_plus_product))
        button_plus_product.click()

    def sub_form_product(self, product):
        self.driver.find_element(*self.intput_item_employees).click()
        self.driver.find_element(*self.intput_item_employees_list).click()
        self.driver.find_element(*self.intput_item_products_locator).send_keys(product['product'])
        self.driver.find_element(*self.intput_item_products_list).click()
        self.driver.find_element(*self.intput_item_products_quantity).clear()
        self.driver.find_element(*self.intput_item_products_quantity).send_keys(product['quantity'])
        button_save = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(self.button_item_products_save))
        button_save.click()
        time.sleep(3)
