from selenium.webdriver.common.by import By
from pagecommonmethods import PageCommonMethods


class Pageclient(PageCommonMethods):
    def __init__(self, driver):
        super().__init__(driver)
        self.clientes_menu = (By.XPATH, '//a[@href="/client"]')
        self.loading = (By.XPATH, '//div[@class="overlay"]')
        self.intput_nickname = (By.XPATH, '//input[contains(@name,"nickname")]')
        self.intput_name = (By.XPATH, '//input[@name="name"]')
        self.intput_surname = (By.XPATH, '//input[contains(@name,"surname")]')
        self.intput_email = (By.XPATH, '//input[@name="email"]')
        self.intput_phone = (By.XPATH, '//input[@name="phone"]')
        self.intput_direction = (By.XPATH, '//input[@name="direction"]')
        self.driver = driver

    def menu_click_client(self):
        self.wait_clickable(self.clientes_menu).click()

    def form_client(self, data_client):
        self.wait_presence(self.intput_nickname).send_keys(data_client['nickname'])
        self.wait_presence(self.intput_name).send_keys(data_client['name'])
        self.wait_presence(self.intput_surname).send_keys(data_client['surname'])
        self.wait_presence(self.intput_email).send_keys(data_client['email'])
        self.wait_presence(self.intput_phone).send_keys(data_client['phone'])
        self.wait_presence(self.intput_direction).send_keys(data_client['direction'])