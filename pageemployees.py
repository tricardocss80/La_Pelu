from selenium.webdriver.common.by import By
from pagecommonmethods import PageCommonMethods
import time


class Pageemployees(PageCommonMethods):
    def __init__(self, driver):
        super().__init__(driver)
        self.employees_menu = (By.XPATH, '//a[@href="/employee"]')
        self.intput_name = (By.XPATH, '//input[@name="name"]')
        self.intput_local = (By.XPATH, '//div[@class="css-1pcexqc-container LocationListComponent full-width"]')
        self.intput_local_selected = (By.XPATH, '//div[@class="css-dpec0i-option"][contains(.,"Mi Negocio")]')
        self.save_button = (By.XPATH, '//button[contains(text(),"Guardar")]')
        self.driver = driver

    def menu_click_employees(self):
        self.wait_clickable(self.employees_menu).click()

    def form_employees(self, name):
        self.wait_presence(self.intput_name).send_keys(name)
        self.wait_presence(self.intput_local).click()
        self.wait_presence(self.intput_local_selected).click()
