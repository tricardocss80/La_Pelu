# -*- coding: utf-8 -*-
import unittest
from selenium import webdriver
from pageindex import Pageindex
from pagelogin import Pagelogin
from pagesales import Pagesales
from pageproduct import Pageproduct
from pageclient import Pageclient
from pageemployees import Pageemployees
from pagesalesforms import Pagesalesforms
from selenium.webdriver.chrome.options import Options
import uuid


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
        self.ProductPage = Pageproduct(self.driver)
        self.ClientPage = Pageclient(self.driver)
        self.EmployeesPage = Pageemployees(self.driver)
        self.FormsSalesPage = Pagesalesforms(self.driver)
        data = {'email': 'ricardonicolastasovac@gmail.com', 'password': 'Pia1juli'}
        self.LoginPage.login(data)

        # Crear un nuevo producto
    def test001_create_product(self):
        data_product = {'name': 'shampoo', 'cost': '100', 'price': '250', 'total': '5', 'minimum': '2'}
        self.ProductPage.wait_overlay()
        self.ProductPage.menu_click_products()
        self.ProductPage.menu_click_products_list()
        self.ProductPage.wait_overlay()
        quantity_initial = self.ProductPage.quantity()
        self.ProductPage.click_new_button()
        self.ProductPage.form_new_product(data_product)
        self.ProductPage.click_save_button()
        self.ProductPage.wait_overlay()
        quantity_final = self.ProductPage.quantity()
        self.assertEqual(quantity_final, quantity_initial + 1)

    # Crear un cliente
    def test002_create_client(self):
        data_client = {'nickname': 'Maria-' + uuid.uuid1().hex, 'name': 'Maria', 'surname': 'Lopez',
                       'email': 'martitalopez@gmail.com',
                       'phone': '1133551331', 'direction': 'Marcopolo 1013'}
        self.ClientPage.wait_overlay()
        self.ClientPage.menu_click_client()
        self.ClientPage.wait_overlay()
        quantity_initial = self.ClientPage.quantity()
        self.ClientPage.click_new_button()
        self.ClientPage.form_client(data_client)
        self.ClientPage.click_save_button()
        self.ClientPage.wait_overlay()
        quantity_final = self.ClientPage.quantity()
        self.assertEqual(quantity_final, quantity_initial + 1)

    # Crear un empleado
    def test003_crate_employees(self):
        name = 'Andres Sosa-'+uuid.uuid1().hex
        self.EmployeesPage.wait_overlay()
        self.EmployeesPage.menu_click_employees()
        self.EmployeesPage.wait_overlay()
        quantity_initial = self.EmployeesPage.quantity()
        self.EmployeesPage.click_new_button()
        self.EmployeesPage.form_employees(name)
        self.EmployeesPage.click_save_button()
        self.EmployeesPage.wait_overlay()
        quantity_final = self.EmployeesPage.quantity()
        self.assertEqual(quantity_final, quantity_initial + 1)

    # Crear una venta con cliente, producto y empleado existentes
    def test004_Create_sale_with_existing_customer_product_employee(self):
        data_sale = {'client': 'mar', 'product': 'sha', 'quantity': '1'}
        self.SalesPage.wait_overlay()
        self.SalesPage.sale_menu()
        self.SalesPage.wait_overlay()
        quantity_initial = self.SalesPage.quantity()
        self.SalesPage.click_button_new_sale()
        self.FormsSalesPage.form_new_sales(data_sale)
        self.FormsSalesPage.add_product()
        self.FormsSalesPage.sub_form_employees()
        self.FormsSalesPage.sub_form_product(data_sale)
        self.FormsSalesPage.dropdown_item_list()
        self.FormsSalesPage.sub_form_quantity(data_sale)
        self.FormsSalesPage.item_add_save()
        self.SalesPage.click_save_button()
        self.SalesPage.wait_overlay()
        quantity_final = self.SalesPage.quantity()
        self.assertEqual(quantity_final, quantity_initial + 1)

     #Eliminar una venta asociada a un producto eliminado
    def test005_remove_sale_associated_with_removed_product(self):
        quantity_initial = self.SalesPage.quantity()
        self.SalesPage.click_delete_sale()
        self.SalesPage.click_accept_button()
        self.SalesPage.wait_overlay()
        quantity_final = self.SalesPage.quantity()
        self.assertEqual(quantity_final, quantity_initial - 1)
        self.SalesPage.close_browser()


if __name__ == '__main__':
    unittest.main()