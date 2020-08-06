# -*- coding: utf-8 -*-
import unittest
from selenium import webdriver
import json
from page_objects.pageindex import Pageindex
from page_objects.pagelogin import Pagelogin
from page_objects.pagesales import Pagesales
from page_objects.pageproduct import Pageproduct
from page_objects.pageclient import Pageclient
from page_objects.pageemployees import Pageemployees
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
        self.ProductPage = Pageproduct(self.driver)
        self.ClientPage = Pageclient(self.driver)
        self.EmployeesPage = Pageemployees(self.driver)
        self.FormsSalesPage = Pagesalesforms(self.driver)
        with open("../jsons/sale_data.json") as sale:
            self.sale_data = json.loads(sale.read())
        self.LoginPage.login(self.sale_data)

        # Crear un nuevo producto
    def test001_create_product(self):
        self.ProductPage.wait_overlay()
        self.ProductPage.menu_click_products()
        self.ProductPage.menu_click_products_list()
        self.ProductPage.wait_overlay()
        quantity_initial = self.ProductPage.quantity()
        self.ProductPage.click_new_button()
        self.ProductPage.form_new_product(self.sale_data)
        self.ProductPage.click_save_button()
        self.ProductPage.wait_overlay()
        quantity_final = self.ProductPage.quantity()
        self.assertEqual(quantity_final, quantity_initial + 1)

    # Crear un cliente
    def test002_create_client(self):
        self.ClientPage.wait_overlay()
        self.ClientPage.menu_click_client()
        self.ClientPage.wait_overlay()
        quantity_initial = self.ClientPage.quantity()
        self.ClientPage.click_new_button()
        self.ClientPage.form_client(self.sale_data)
        self.ClientPage.click_save_button()
        self.ClientPage.wait_overlay()
        quantity_final = self.ClientPage.quantity()
        self.assertEqual(quantity_final, quantity_initial + 1)

    # Crear un empleado
    def test003_crate_employees(self):
        self.EmployeesPage.wait_overlay()
        self.EmployeesPage.menu_click_employees()
        self.EmployeesPage.wait_overlay()
        quantity_initial = self.EmployeesPage.quantity()
        self.EmployeesPage.click_new_button()
        self.EmployeesPage.form_employees(self.sale_data)
        self.EmployeesPage.dropdown_item_list()
        self.EmployeesPage.click_save_button()
        self.EmployeesPage.wait_overlay()
        quantity_final = self.EmployeesPage.quantity()
        self.assertEqual(quantity_final, quantity_initial + 1)

    # Crear una venta con cliente, producto y empleado existentes
    def test004_Create_sale_with_existing_customer_product_employee(self):
        self.SalesPage.wait_overlay()
        self.SalesPage.sale_menu()
        self.SalesPage.wait_overlay()
        quantity_initial = self.SalesPage.quantity()
        self.SalesPage.click_button_new_sale()
        self.FormsSalesPage.form_new_sales(self.sale_data)
        self.FormsSalesPage.add_product()
        self.FormsSalesPage.sub_form_employees()
        self.FormsSalesPage.sub_form_product(self.sale_data)
        self.FormsSalesPage.dropdown_item_list()
        self.FormsSalesPage.sub_form_quantity(self.sale_data)
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