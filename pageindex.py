from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from page_common_methods import PageCommonMethods


class Pageindex(PageCommonMethods):
    def __init__(self, driver):
        super().__init__(driver)
        self.ingresar_button = (By.XPATH, '//a[contains(.,"Ingresar")]')
        self.driver = driver

    def Enterokay(self):
        self.wait_clickable(self.ingresar_button).click()
