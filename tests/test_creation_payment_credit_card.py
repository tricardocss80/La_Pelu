# -*- coding: utf-8 -*-
import unittest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options  
from page_objects.pageindex import Pageindex
from page_objects.pagelogin import Pagelogin
from page_objects.pagepayment import PagePayment


class PaymentCasesSuit(unittest.TestCase):
    @classmethod
    def setUpClass(self):
        option = Options()
        option.add_argument('--headless')
        self.driver = webdriver.Chrome('../drivers/chromedriver.exe', options=option)
        self.driver.get('https://stg-admin.lapelu.com.ar/')
        self.driver.set_window_size(1920, 1080)
        self.IndexPage = Pageindex(self.driver)
        self.LoginPage = Pagelogin(self.driver)
        self.PaymentPage = PagePayment(self.driver)
        data = {'email': 'tricardocss@gmail.com', 'password': 'Velez300'}
        self.LoginPage.login(data)

    #Intentar crear metodo de pago  dejando el campo vacio
    def test_001_try_create_credit_card_payment_method(self):
        data = {'name': ''}
        self.PaymentPage.wait_overlay()
        self.PaymentPage.click_button_config()
        self.PaymentPage.click_button_payment()
        self.PaymentPage.wait_overlay()
        self.PaymentPage.click_new_button()
        self.PaymentPage.intput_payment_method(data)
        self.PaymentPage.click_save_button()
        self.PaymentPage.wait_overlay()
        self.assertEqual('Error!', self.PaymentPage.asser_block_error())
        self.assertEqual('El nombre debe tener al menos 3 letras', self.PaymentPage.asser_error())
        self.PaymentPage.click_cancel_button()

    #Crear un metodo de pago con tarjeta de crédito(Camino feliz)
    def test_002_create_credit_card_payment_method(self):
        data = {'name': 'Tarjeta de crédito'}
        quantity_initial = self.PaymentPage.quantity()
        self.PaymentPage.click_new_button()
        self.PaymentPage.intput_payment_method(data)
        self.PaymentPage.click_save_button()
        self.PaymentPage.wait_overlay()
        quantity_final = self.PaymentPage.quantity()
        self.assertEqual(quantity_final, quantity_initial + 1)

     # Eliminar el metodo de pago tarjeta de crédito(Camino feliz)
    def test_003_delete_credit_card_payment_method(self):
        quantity_initial = self.PaymentPage.quantity()
        self.PaymentPage.deactivate_button()
        self.PaymentPage.click_accept_button()
        self.PaymentPage.wait_overlay()
        quantity_final = self.PaymentPage.quantity()
        self.assertEqual(quantity_final, quantity_initial - 1)
        self.PaymentPage.close_browser()


if __name__ == '__main__':
    unittest.main()
