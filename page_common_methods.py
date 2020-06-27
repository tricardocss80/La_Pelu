from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


class PageCommonMethods:
    def __init__(self, driver):
        self.loading = (By.XPATH, '//div[@class="overlay"]')
        self.driver = driver

    def wait_overlay(self):
        WebDriverWait(self.driver, 30).until(EC.invisibility_of_element_located(self.loading))
        time.sleep(1)

    def wait_clickable(self, locator):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable(locator))

    def wait_presence(self, locator):
        return WebDriverWait(self.driver, 30).until(EC.presence_of_element_located(locator))

    def close_browser(self):
        self.driver.close()
        self.driver.quit()
