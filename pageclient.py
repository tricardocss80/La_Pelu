from selenium.webdriver.common.by import By
from page_common_methods import PageCommonMethods


class Pageclient(PageCommonMethods):
    def __init__(self, driver):
        super().__init__(driver)
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
        self.wait_clickable(self.clientes_menu).click()

    def new_client(self):
        self.wait_clickable(self.new_button).click()

    def form_client(self, data_client):
        self.wait_presence(self.intput_nickname).send_keys(data_client['nickname'])
        self.wait_presence(self.intput_name).send_keys(data_client['name'])
        self.wait_presence(self.intput_surname).send_keys(data_client['surname'])
        self.wait_presence(self.intput_email).send_keys(data_client['email'])
        self.wait_presence(self.intput_phone).send_keys(data_client['phone'])
        self.wait_presence(self.intput_direction).send_keys(data_client['direction'])
        self.wait_clickable(self.button_guardar).click()

    def quantity_client(self):
        try:
            quantity_client = self.driver.find_element(*self.quantity_clients)
            self.driver.save_screenshot('time_error.png')
            return int(quantity_client.text.replace('Total: ', ''))
        except Exception as e:
            print(e)
            return 0
