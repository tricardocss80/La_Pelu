# -*- coding: utf-8 -*-
import unittest
from selenium import webdriver
from pageindex import Pageindex
from pagelogin import Pagelogin
from pagesales import Pagesales
from pagedebt import PageDebt
from pagesalesforms import Pagesalesforms
from selenium.webdriver.chrome.options import Options


class SalesCaseSuite(unittest.TestCase):
    @classmethod
    def setUpClass(self):
        option = Options()
        #option.add_argument('--headless')
        self.driver = webdriver.Chrome('Chromedriver.exe', options=option)
        self.driver.get('https://stg-admin.lapelu.com.ar/')
        self.driver.set_window_size(1920, 1080)
        self.IndexPage = Pageindex(self.driver)
        self.LoginPage = Pagelogin(self.driver)
        self.SalesPage = Pagesales(self.driver)
        self.FormsSalesPage = Pagesalesforms(self.driver)
        self.DebtPage = PageDebt(self.driver)
        data = {'email': 'ricardonicolastasovac@gmail.com', 'password': 'Pia1juli'}
        self.LoginPage.login(data)

    # Crear una venta pagando con dos metodos de pago diferentes y dejando una deuda
    def test001_create_sale_with_different_payment_methods(self):
        data_sale = {
            'client': 'mar',
            'service': 'tin',
            'cash': '400',
            'credit card': '500'
        }
        self.SalesPage.wait_overlay()
        self.SalesPage.sale_menu()
        self.SalesPage.wait_overlay()
        quantity_initial = self.SalesPage.quantity()
        self.SalesPage.click_button_new_sale()
        self.FormsSalesPage.form_new_sales(data_sale)
        self.FormsSalesPage.add_service()
        self.FormsSalesPage.sub_form_employees()
        self.FormsSalesPage.sub_form_service(data_sale)
        self.FormsSalesPage.dropdown_item_list()
        self.FormsSalesPage.item_add_save()
        price_total = self.FormsSalesPage.price_total()
        self.FormsSalesPage.payment_cash(0, data_sale)
        price_cash = self.FormsSalesPage.return_price(0)
        self.FormsSalesPage.payment_credit_card(1, data_sale)
        price_card = self.FormsSalesPage.return_price(1)
        self.assertEqual(self.FormsSalesPage.assert_debt(), (price_total - price_cash - price_card))
        self.SalesPage.click_save_button()
        self.SalesPage.wait_overlay()
        quantity_final = self.SalesPage.quantity()
        self.assertEqual(quantity_final, quantity_initial + 1)

    # Saldar deuda adquirida
    def test002_pay_off_acquired_debt(self):
        self.DebtPage.click_menu_report()
        self.DebtPage.click_menu_dedt()
        self.DebtPage.wait_overlay()
        quantity_initial = self.DebtPage.quantity()
        self.DebtPage.click_button_pay()
        self.DebtPage.click_method()
        self.DebtPage.click_accept_button()
        self.DebtPage.wait_overlay()
        quantity_final = self.DebtPage.quantity()
        self.assertEqual(quantity_final, quantity_initial - 1)
        self.DebtPage.close_browser()


if __name__ == '__main__':
    unittest.main()


