from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


class PageCommonMethods:
    def __init__(self, driver):
        self.loading = (By.XPATH, '//div[@class="overlay"]')
        self.new_button = (By.XPATH, '//button[contains(.,"Nuevo")]')
        self.save_button = (By.XPATH, '//button[contains(text(),"Guardar")]')
        self.block_error = (By.XPATH, '//div[@class="toast-title"]')
        self.quantity_items = (By.XPATH, '//div[@class="pagination"]//ul[@class="nav"]')
        self.accept_button = (By.XPATH, '//button[@class="btn btn-danger"]')
        self.driver = driver

    def wait_overlay(self):
        WebDriverWait(self.driver, 30).until(EC.invisibility_of_element_located(self.loading))
        time.sleep(1)

    def click_new_button(self):
        self.wait_clickable(self.new_button).click()

    def click_save_button(self):
        self.wait_clickable(self.save_button).click()

    def wait_clickable(self, locator):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable(locator))

    def wait_presence(self, locator):
        return WebDriverWait(self.driver, 30).until(EC.presence_of_element_located(locator))

    def asser_block_error(self):
        return self.wait_presence(self.block_error).text

    def quantity(self):
        try:
            quantity = self.driver.find_element(*self.quantity_items)
            return int(quantity.text.replace('Total: ', ''))
        except Exception as e:
            print(e)
            return 0

    def click_accept_button(self):
        self.wait_clickable(self.accept_button).click()


    def close_browser(self):
        self.driver.close()
        self.driver.quit()