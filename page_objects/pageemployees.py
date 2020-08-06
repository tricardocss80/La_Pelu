from selenium.webdriver.common.by import By
from page_objects.pagecommonmethods import PageCommonMethods
import uuid


class Pageemployees(PageCommonMethods):
    def __init__(self, driver):
        super().__init__(driver)
        self.employees_menu = (By.XPATH, '//a[@href="/employee"]')
        self.intput_name = (By.XPATH, '//input[@name="name"]')
        self.intput_local = (By.XPATH, '//div[@class="css-1pcexqc-container LocationListComponent full-width"]')

        self.save_button = (By.XPATH, '//button[contains(text(),"Guardar")]')
        self.driver = driver

    def menu_click_employees(self):
        self.wait_clickable(self.employees_menu).click()

    def form_employees(self, sale_data):
        self.wait_presence(self.intput_name).send_keys(sale_data['employees'] + uuid.uuid1().hex)
        self.wait_presence(self.intput_local).click()