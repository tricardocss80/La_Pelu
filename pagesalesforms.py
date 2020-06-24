from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


class Pagesalesforms:
    def __init__(self, driver):
        self.intput_client_locator = (By.XPATH, '//input[@autocomplete="off"]')
        self.intput_client_list = (By.XPATH, '//div[@id="react-select-4-option-0" and contains(@class, "css-dpec0i-option")]/span[contains(@class, "select-option-label")]')
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

    def form_new_sales(self, data_sale):
        input_client_locator = WebDriverWait(self.driver, 30).until(EC.presence_of_element_located(self.intput_client_locator))
        input_client_locator.send_keys(data_sale['client'])
        input_client_list = WebDriverWait(self.driver, 30).until(EC.presence_of_element_located(self.intput_client_list))
        input_client_list.click()
        button_plus_product = WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable(self.button_plus_product))
        button_plus_product.click()

    def sub_form_product(self, data_sale):
        intput_item_employees = WebDriverWait(self.driver, 30).until(EC.presence_of_element_located(self.intput_item_employees))
        intput_item_employees.click()
        intput_item_employees_list = WebDriverWait(self.driver, 30).until(EC.presence_of_element_located(self.intput_item_employees_list))
        intput_item_employees_list.click()
        intput_item_product_locator = WebDriverWait(self.driver, 30).until(EC.presence_of_element_located(self.intput_item_products_locator))
        intput_item_product_locator.send_keys(data_sale['product'])
        intput_item_product_list = WebDriverWait(self.driver, 30).until(EC.presence_of_element_located(self.intput_item_products_list))
        intput_item_product_list.click()
        intput_item_product_quantity = WebDriverWait(self.driver, 30).until(EC.presence_of_element_located(self.intput_item_products_quantity))
        intput_item_product_quantity.clear()
        intput_item_product_quantity.send_keys(data_sale['quantity'])
        button_save = WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable(self.button_item_products_save))
        button_save.click()