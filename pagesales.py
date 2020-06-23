from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class Pagesales:
    def __init__(self, driver):
        self.ventas_menu = (By.XPATH, '//li[@class="nav-item"][contains(.,"Ventas")]')
        self.button_new = (By.XPATH, '//a[contains(.,"Nueva")]')
        self.quantity_ventas = (By.XPATH, '//div[@class="pagination"]//ul[@class="nav"]')
        self.loading = (By.XPATH, '//div[@class="overlay"]')
        self.eliminar_button = (By.XPATH, '(//button[contains(text(),"Eliminar")])[1]')
        self.aceptar_button = (By.XPATH, '//button[@class="btn btn-danger"]')
        self.button_save = (By.XPATH, '//button[contains(.,"Guardar")]')
        self.driver = driver

    def sale_menu(self):
        menu_venta = WebDriverWait(self.driver, 20).until(EC.presence_of_element_located(self.ventas_menu))
        WebDriverWait(self.driver, 20).until(EC.invisibility_of_element(self.loading))
        menu_venta.click()

    def click_button_new_sale(self):
        button_new = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(self.button_new))
        button_new.click()

    def click_button_save_new_sale(self):
        button_save = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(self.button_save))
        button_save.click()

    def quantity_sale(self):
        quantity_venta = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(self.quantity_ventas))
        return int(quantity_venta.text.replace('Total: ', ''))

    def click_delete_sale(self):
        eliminar_button = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(self.eliminar_button))
        eliminar_button.click()
        aceptar_button = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(self.aceptar_button))
        aceptar_button.click()



