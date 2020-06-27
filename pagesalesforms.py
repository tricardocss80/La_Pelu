from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from page_common_methods import PageCommonMethods


class Pagesalesforms(PageCommonMethods):
    def __init__(self, driver):
        super().__init__(driver)
        self.intput_client_locator = (By.XPATH, '//input[@autocomplete="off"]')
        self.intput_client_list = (By.XPATH, '//div[contains(@class,"css-dpec0i-option option")]')
        self.button_plus_product = (By.XPATH, '//button[contains(text(),"+ Producto")]')
        self.intput_item_employees = (By.XPATH, '//div[contains(@class,"EmployeesListComponent")]')
        self.intput_item_employees_list = (By.XPATH, '//div[contains(@class,"css-1eyv3xi-option")]')
        self.intput_item_products_locator = (By.XPATH, '//div[@class="css-1pcexqc-container ProductsListComponent '
                                                       'full-width"]//div[@class="css-bg1rzq-control"]//div[@class="'
                                                       'css-1hwfws3"]//div[@class="css-1g6gooi"]//input')
        self.intput_item_products_list = (By.XPATH, '//div[@class="css-dpec0i-option"]')
        self.intput_item_products_quantity = (By.XPATH, '//input[@name="quantity"]')
        self.intput_item_products_price = (By.XPATH, '//input[contains(@name,"price")]')
        self.button_item_products_save = (By.XPATH, '//button[contains(.,"Agregar")]')
        self.driver = driver

    def form_new_sales(self, data_sale):
        self.wait_presence(self.intput_client_locator).send_keys(data_sale['client'])
        self.wait_presence(self.intput_client_list).click()
        self.wait_clickable(self.button_plus_product).click()

    def sub_form_product(self, data_sale):
        self.wait_presence(self.intput_item_employees).click()
        self.wait_presence(self.intput_item_employees_list).click()
        self.wait_presence(self.intput_item_products_locator).send_keys(data_sale['product'])
        self.wait_presence(self.intput_item_products_list).click()
        intput_item_product_quantity = self.wait_presence(self.intput_item_products_quantity)
        intput_item_product_quantity.clear()
        intput_item_product_quantity.send_keys(data_sale['quantity'])
        self.wait_clickable(self.button_item_products_save).click()
