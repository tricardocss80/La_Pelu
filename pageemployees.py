from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


class Pageemployees:
    def __init__(self, driver):
        self.employees_menu = (By.XPATH, '//a[@href="/employee"]')
        self.loading = (By.XPATH, '//div[@class="overlay"]')
        self.new_button = (By.XPATH, '//button[contains(.,"Nuevo")]')
        self.intput_name = (By.XPATH, '//input[@name="name"]')
        self.intput_local = (By.XPATH, '//div[@class="css-1pcexqc-container LocationListComponent full-width"]')
        self.intput_local_selected = (By.XPATH, '//div[@id="react-select-5-option-0" and contains(@class, "css-dpec0i-option")]')
        self.button_guardar = (By.XPATH, '//button[contains(.,"Guardar")]')
        self.quantity_employees = (By.XPATH, '//div[@class="pagination"]//ul[@class="nav"]')
        self.driver = driver

    def menu_click_employees(self):
        menu_employees = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(self.employees_menu))
        WebDriverWait(self.driver, 10).until(EC.invisibility_of_element(self.loading))
        menu_employees.click()

    def new_employees(self):
        new_button = WebDriverWait(self.driver, 4).until(EC.element_to_be_clickable(self.new_button))
        WebDriverWait(self.driver, 10).until(EC.invisibility_of_element(self.loading))
        new_button.click()

    def form_employees(self, name):
        self.driver.find_element(*self.intput_name).send_keys(name)
        button_guardar = WebDriverWait(self.driver, 4).until(EC.element_to_be_clickable(self.button_guardar))
        self.driver.find_element(*self.intput_local).click()
        self.driver.find_element(*self.intput_local_selected).click()
        button_guardar.click()

    def quantity_employee(self):
        quantity_employee = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(self.quantity_employees))
        return int(quantity_employee.text.replace('Total: ', ''))