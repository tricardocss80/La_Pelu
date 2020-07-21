# -*- coding: utf-8 -*-
import unittest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from pageindex import Pageindex
from pagelogin import Pagelogin
from pagepayment import PagePayment


class PaymentCasesSuit(unittest.TestCase):
    def setUp(self):
        option = Options()
        # option.add_argument('--headless')
        self.driver = webdriver.Chrome('Chromedriver.exe', options=option)
        self.driver.get('https://www.lapelu.com.ar/')
        self.driver.set_window_size(1920, 1080)
        self.IndexPage = Pageindex(self.driver)
        self.LoginPage = Pagelogin(self.driver)
        self.PaymentPage = PagePayment(self.driver)
        data = {'email': 'ricardonicolastasovac@gmail.com', 'password': 'Pia1juli'}
        self.IndexPage.Enterok()
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

    #Intentar crear metodo de pago  ingresando caracteres especiales
    @unittest.skip
    def test_002_try_create_credit_card_payment_method(self):
        data = {'name': '???@¿¿¿'}
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

    #Intentar crear metodo de pago  ingresando numeros
    @unittest.skip
    def test_003_try_create_credit_card_payment_method(self):
        data = {'name': '???@¿¿¿'}
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

    #Camino feliz
    def test_004_create_credit_card_payment_method(self):
        data = {'name': 'Tarjeta de crédito'}
        self.PaymentPage.wait_overlay()
        self.PaymentPage.click_button_config()
        self.PaymentPage.click_button_payment()
        self.PaymentPage.wait_overlay()
        quantity_initial = self.PaymentPage.quantity()
        self.PaymentPage.click_new_button()
        self.PaymentPage.intput_payment_method(data)
        self.PaymentPage.click_save_button()
        self.PaymentPage.wait_overlay()
        quantity_final = self.PaymentPage.quantity()
        self.assertEqual(quantity_final, quantity_initial + 1)

     # Camino feliz
    def test_005_create_credit_card_payment_method(self):
        self.PaymentPage.click_button_config()
        self.PaymentPage.click_button_payment()
        self.PaymentPage.wait_overlay()

        print('hola')
        print(self.driver.find_element_by_class_name('btn btn-primary[0]').text)
        print('hola')