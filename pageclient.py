from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


class Pageclient:
    def __init__(self, driver):
        self.clientes_menu = (By.XPATH, '//a[@href="/client"]')
        self.loading = (By.XPATH, '//div[@class="overlay"]')
        self.new_button = (By.XPATH, '//button[contains(.,"Nuevo")]')
        self.intput_nickname = (By.XPATH, '//input[contains(@name,"nickname")]')
        self.intput_name = (By.XPATH, '//input[@name="name"]')
        self.intput_surname = (By.XPATH, '//input[contains(@name,"surname")]')
        self.intput_email = (By.XPATH, '//input[@name="email"]')
        self.intput_phone = (By.XPATH, '//input[@name="phone"]')
        self.intput_direction = (By.XPATH, '//input[@name="direction"]')
        self.button_guardar = (By.XPATH, '//button[contains(.,"Guardar")]')
        self.quantity_clients = (By.XPATH, '//div[@class="pagination"]//ul[@class="nav"]')
        self.driver = driver

    def menu_click_client(self):
        menu_clientes = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(self.clientes_menu))
        WebDriverWait(self.driver, 10).until(EC.invisibility_of_element(self.loading))
        menu_clientes.click()

    def new_client(self):
        new_button = WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable(self.new_button))
        new_button.click()

    def form_client(self, data_client):
        self.driver.find_element(*self.intput_nickname).send_keys(data_client['nickname'])
        self.driver.find_element(*self.intput_name).send_keys(data_client['name'])
        self.driver.find_element(*self.intput_surname).send_keys(data_client['surname'])
        self.driver.find_element(*self.intput_email).send_keys(data_client['email'])
        self.driver.find_element(*self.intput_phone).send_keys(data_client['phone'])
        self.driver.find_element(*self.intput_direction).send_keys(data_client['direction'])
        button_guardar = WebDriverWait(self.driver, 4).until(EC.element_to_be_clickable(self.button_guardar))
        button_guardar.click()

    def quantity_client(self):
        quantity_client = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(self.quantity_clients))
        return int(quantity_client.text.replace('Total: ', ''))
