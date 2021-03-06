from selenium.webdriver.common.by import By
from page_objects.pagecommonmethods import PageCommonMethods


class Pagesalesforms(PageCommonMethods):
    def __init__(self, driver):
        super().__init__(driver)
        self.intput_client_locator = (By.XPATH, '//input[@autocomplete="off"]')
        self.intput_client_list = (By.XPATH, '//div[contains(@class,"css-dpec0i-option option")]')
        self.intput_item_employees = (By.XPATH, '//div[contains(@class,"EmployeesListComponent")]')
        self.intput_item_employees_list = (By.XPATH, '//div[contains(@class,"css-1eyv3xi-option")]')
        self.intput_item_products_locator = (By.XPATH, '//div[@class="css-1pcexqc-container ProductsListComponent '
                                                       'full-width"]//input')
        self.intput_item_service_locator = (By.XPATH, '// div[ @class ="css-1pcexqc-container ServiceListComponent'
                                                      ' full-width"]//input')
        self.intput_item_products_quantity = (By.XPATH, '//input[@name="quantity"]')
        self.intput_item_products_price = (By.XPATH, '//input[contains(@name,"price")]')
        self.button_item_products_save = (By.XPATH, '//button[contains(.,"Agregar")]')
        self.debt = (By.XPATH, '//label[@for="generate-due"]')
        self.price = (By.XPATH, '//div[@class="text-right alert alert-primary fade show"]')
        self.driver = driver

    def form_new_sales(self, sale_data):
        self.wait_presence(self.intput_client_locator).send_keys(sale_data['sale']['client'])
        self.wait_presence(self.intput_client_list).click()

    def sub_form_employees(self):
        self.wait_presence(self.intput_item_employees).click()
        self.wait_presence(self.intput_item_employees_list).click()

    def sub_form_product(self, sale_data):
        self.wait_presence(self.intput_item_products_locator).send_keys(sale_data['sale']['product'])

    def sub_form_service(self, sale_data):
        self.wait_presence(self.intput_item_service_locator).send_keys(sale_data['sale']['service'])

    def sub_form_quantity(self, sale_data):
        intput_item_product_quantity = self.wait_presence(self.intput_item_products_quantity)
        intput_item_product_quantity.clear()
        intput_item_product_quantity.send_keys(sale_data['sale']['quantity'])

    def payment_cash(self, index, data_sale):
        self.driver.find_elements(*self.payment_method)[index].clear()
        self.driver.find_elements(*self.payment_method)[index].send_keys(data_sale['payment']['cash'])

    def payment_credit_card(self, index, data_sale):
        self.driver.find_elements(*self.payment_method)[index].clear()
        self.driver.find_elements(*self.payment_method)[index].send_keys(data_sale['payment']['card'])

    def price_total(self):
        price = self.driver.find_element(*self.price).text.replace('Total de la venta: $', '')
        result = price.replace('.', '')
        result_int = result.split(',')[0]
        return int(result_int)

    def price_debt(self):
        price = self.driver.find_element(*self.debt).text.replace('Generar deuda por: $ ', '')
        result = price.replace('.', '')
        result_int = result.split(',')[0]
        return int(result_int)
