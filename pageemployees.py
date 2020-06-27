from selenium.webdriver.common.by import By
from page_common_methods import PageCommonMethods
import time


class Pageemployees(PageCommonMethods):
    def __init__(self, driver):
        super().__init__(driver)
        self.employees_menu = (By.XPATH, '//a[@href="/employee"]')
        self.loading = (By.XPATH, '//div[@class="overlay"]')
        self.new_button = (By.XPATH, '//button[contains(.,"Nuevo")]')
        self.intput_name = (By.XPATH, '//input[@name="name"]')
        self.intput_local = (By.XPATH, '//div[@class="css-1pcexqc-container LocationListComponent full-width"]')
        self.intput_local_selected = (By.XPATH, '//div[contains(@class,"css-dpec0i-option")]')
        self.button_guardar = (By.XPATH, '//button[contains(.,"Guardar")]')
        self.quantity_employees = (By.XPATH, '//div[@class="pagination"]//ul[@class="nav"]')
        self.driver = driver

    def menu_click_employees(self):
        self.wait_clickable(self.employees_menu).click()

    def new_employees(self):
        self.wait_clickable(self.new_button).click()

    def form_employees(self, name):
        self.wait_presence(self.intput_name).send_keys(name)
        self.wait_presence(self.intput_local).click()
        self.driver.save_screenshot('hola.png')
        self.wait_presence(self.intput_local_selected).click()
        self.wait_clickable(self.button_guardar).click()

    def quantity_employee(self):
        try:
            quantity_employee = self.driver.find_element(*self.quantity_employees)
            self.driver.save_screenshot('time_error.png')
            return int(quantity_employee.text.replace('Total: ', ''))
        except Exception as e:
            print(e)
            return 0
