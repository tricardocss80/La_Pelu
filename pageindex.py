from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class Pageindex:
    def __init__(self, driver):
        self.ingresar_button = (By.XPATH, '//*[@id="nav"]/div/ul/li[6]/a')
        self.driver = driver

    def Enterokay(self):
        button_ingresar = WebDriverWait(self.driver, 4).until(EC.element_to_be_clickable(self.ingresar_button))
        button_ingresar.click()
