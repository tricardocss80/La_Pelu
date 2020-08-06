# -*- coding: utf-8 -*-
import unittest
from selenium import webdriver
import json
from page_objects.pageindex import Pageindex
from page_objects.pagelogin import Pagelogin
from page_objects.pagesales import Pagesales
from page_objects.pagedebt import PageDebt
from page_objects.pagesalesforms import Pagesalesforms
from selenium.webdriver.chrome.options import Options


class SalesCaseSuite(unittest.TestCase):
    @classmethod
    def setUpClass(self):
        option = Options()
        option.add_argument('--headless')
        self.driver = webdriver.Chrome('../drivers/chromedriver.exe', options=option)
        self.driver.get('https://stg-admin.lapelu.com.ar/')
        self.driver.set_window_size(1920, 1080)
        self.IndexPage = Pageindex(self.driver)
        self.LoginPage = Pagelogin(self.driver)
        self.SalesPage = Pagesales(self.driver)
        self.FormsSalesPage = Pagesalesforms(self.driver)
        self.DebtPage = PageDebt(self.driver)
        with open("../jsons/sale_data.json") as sale:
            self.sale_data = json.loads(sale.read())
        self.LoginPage.login(self.sale_data)

    # Crear una venta pagando con dos metodos de pago diferentes y dejando una deuda
    def test001_create_sale_with_different_payment_methods(self):
        self.SalesPage.wait_overlay()
        self.SalesPage.sale_menu()
        self.SalesPage.wait_overlay()
        quantity_initial = self.SalesPage.quantity()
        self.SalesPage.click_button_new_sale()
        self.FormsSalesPage.form_new_sales(self.sale_data)
        self.FormsSalesPage.add_service()
        self.FormsSalesPage.sub_form_employees()
        self.FormsSalesPage.sub_form_service(self.sale_data)
        self.FormsSalesPage.dropdown_item_list()
        self.FormsSalesPage.item_add_save()
        price_total = self.FormsSalesPage.price_total()
        self.FormsSalesPage.payment_cash(0, self.sale_data)
        price_cash = self.FormsSalesPage.return_price(0)
        self.FormsSalesPage.payment_credit_card(1, self.sale_data)
        price_card = self.FormsSalesPage.return_price(1)
        self.FormsSalesPage.wait_overlay(0.1)
        price_debt = self.FormsSalesPage.price_debt()
        self.assertEqual(price_debt, (price_total - price_cash - price_card))
        self.SalesPage.click_save_button()
        self.SalesPage.wait_overlay()
        quantity_final = self.SalesPage.quantity()
        self.assertEqual(quantity_final, quantity_initial + 1)

    # Saldar deuda adquirida
    def test002_pay_off_acquired_debt(self):
        self.SalesPage.wait_overlay()
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