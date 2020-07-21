from selenium.webdriver.common.by import By
from pagecommonmethods import PageCommonMethods


class Pageindex(PageCommonMethods):
    def __init__(self, driver):
        super().__init__(driver)
        self.ingresar_button = (By.XPATH, '//a[contains(.,"Ingresar")]')
        self.driver = driver

    def Enterok(self):
        self.wait_clickable(self.ingresar_button).click()
