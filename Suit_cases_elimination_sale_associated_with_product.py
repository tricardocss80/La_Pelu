import unittest
from selenium import webdriver
from pageindex import Pageindex
from pagelogin import Pagelogin
from pagesales import Pagesales
from pageproduct import Pageproduct
from pageclient import Pageclient
from pageemployees import Pageemployees
from pagesalesforms import Pagesalesforms


class SalesCaseSuite(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome('Chromedriver.exe')
        self.driver.get('https://www.lapelu.com.ar/')
        self.IndexPage = Pageindex(self.driver)
        self.LoginPage = Pagelogin(self.driver)
        self.SalesPage = Pagesales(self.driver)
        self.ProductPage = Pageproduct(self.driver)
        self.ClientPage = Pageclient(self.driver)
        self.EmployeesPage = Pageemployees(self.driver)
        self.FormsSalesPage = Pagesalesforms(self.driver)
        data = {
            'email': 'ricardonicolastasovac@gmail.com',
            'password': 'velezcapo'}
        self.IndexPage.Enterokay()
        self.LoginPage.login(data)

        # Crear un nuevo producto
    def test001_create_product(self):
        data_product = {
            'name': 'shampoo',
            'cost': '100',
            'price': '250',
            'total': '5',
            'minimum': '2',
        }
        self.ProductPage.menu_click_producto()
        self.ProductPage.new_product()
        self.ProductPage.form_new_product(data_product)
        self.ProductPage.quantity_products()
        quantity_products = self.ProductPage.quantity_products()
        self.assertEqual(quantity_products, 1)

    # Crear un cliente
    def test002_create_client(self):
        data_client = {
            'nickname': 'Martita',
            'name': 'Marta',
            'surname': 'Lopez',
            'email': 'martitalopez@gmail.com',
            'phone': '1133551331',
            'direction': 'Marcopolo 1013'
        }
        self.ClientPage.menu_click_client()
        self.ClientPage.new_client()
        self.ClientPage.form_client(data_client)
        self.ClientPage.quantity_client()
        quantity_clients = self.ClientPage.quantity_client()
        self.assertEqual(quantity_clients, 1)

    # Crear un empleado
    def test003_crate_employees(self):
        name = 'Victor Satriano'
        self.EmployeesPage.menu_click_employees()
        self.EmployeesPage.new_employees()
        self.EmployeesPage.form_employees(name)
        quantity_employees = self.EmployeesPage.quantity_employee()
        self.assertEqual(quantity_employees, 1)

    # Crear una venta con cliente, producto y empleado existentes
    def test004_Create_sale_with_existing_customer_product_employee(self):
        data_sale = {
            'client': 'mar',
            'product': 'sha',
            'quantity': '1'
        }
        self.SalesPage.sale_menu()
        self.SalesPage.click_button_new_sale()
        self.FormsSalesPage.form_new_sales(data_sale)
        self.FormsSalesPage.sub_form_product(data_sale)
        self.SalesPage.click_button_save_new_sale()
        quantity_sales = self.SalesPage.quantity_sale()
        self.assertEqual(quantity_sales, 1)

     #eliminar una venta asociada a un producto eliminado
    def test005_remove_sale_associated_with_removed_product(self):
        self.SalesPage.sale_menu()
        quantity_sales = self.SalesPage.quantity_sale()
        self.SalesPage.click_delete_sale()
        quantity_sales_delete = self.SalesPage.quantity_sale()
        quantity_sales_total = quantity_sales - quantity_sales_delete
        self.assertEqual(quantity_sales_total, 0)

    def tearDown(self):
        self.driver.close()
        self.driver.quit()


if __name__ == '__main__':
    unittest.main()
