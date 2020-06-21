import unittest
from selenium import webdriver
from pageindex import Pageindex
from pagelogin import Pagelogin
from pagesales import Pagesales
from pageproduct import Pageproduct
from pageclient import Pageclient
from pageemployees import Pageemployees
from pagesalesforms import Pagesalesforms


class VentaCases(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome('Chromedriver.exe')
        self.driver.get('https://www.lapelu.com.ar/')
        self.IndexPage = Pageindex(self.driver)
        self.LoginPage = Pagelogin(self.driver)
        self.SalesPage = Pagesales(self.driver)
        self.ProductPage = Pageproduct(self.driver)
        self.Clientpage = Pageclient(self.driver)
        self.EmployeesPage = Pageemployees(self.driver)
        self.FormsSalesPage = Pagesalesforms(self.driver)
        self.driver.implicitly_wait(15)
        data = {'email': 'ricardonicolastasovac@gmail.com', 'password': 'velezcapo'}
        self.IndexPage.Enterokay()
        self.LoginPage.login(data)

        # Crear un nuevo producto
    def test_create_product(self):
        data_product = {
            'name': 'shampoo',
            'cost': '100',
            'price': '250',
            'total': '5',
            'minimum': '2',
        }
        self.ProductPage.menu_click_producto()
        self.ProductPage.new_producto()
        self.ProductPage.form_new_producto(data_product)
        self.ProductPage.quantity_products()
        quantity_productos = self.ProductPage.quantity_products()
        self.assertEqual(quantity_productos, 1)

    # Crear un cliente
    def test_create_client(self):
        data_client = {
            'nickname': 'Silvita',
            'name': 'Silvia',
            'surname': 'Tronchet',
            'email': 'silvita@gmail.com',
            'phone': '1133964554',
            'direction': 'Carabelas 1013'
        }
        self.Clientpage.menu_click_client()
        self.Clientpage.new_client()
        self.Clientpage.form_client(data_client)
        self.Clientpage.quantity_client()
        quantity_clientes = self.Clientpage.quantity_client()
        self.assertEqual(quantity_clientes, 1)

    # Crear un empleado
    def test_crate_employees(self):
        name = 'Victor Satriano'
        self.EmployeesPage.menu_click_employees()
        self.EmployeesPage.new_employees()
        self.EmployeesPage.form_employees(name)
        quantity_employees = self.EmployeesPage.quantity_employee()
        self.assertEqual(quantity_employees, 1)

    # Crear una venta con cliente, producto y empleado existentes
    def test_Create_sale_with_existing_customer_product_employee(self):
        client = 'sil'
        product = {
            'product': 'sha',
            'quantity': '1'
        }
        self.SalesPage.venta_menu()
        self.SalesPage.click_button_new_sale()
        self.FormsSalesPage.form_new_sales(client)
        self.FormsSalesPage.sub_form_product(product)
        self.SalesPage.click_button_save_new_sale()

        #quantity_sales = self.SalesPage.quantity_venta()
        #self.assertEqual(quantity_sales, 1)




     #eliminar una venta asociada a un producto eliminado
    def test_remove_sale_associated_with_removed_product(self):
        self.SalesPage.venta_menu()
        quantity_ventas = self.SalesPage.quantity_sale()
        self.SalesPage.click_delete_venta()
        quantity_ventas_delete = self.SalesPage.quantity_sale()
        quantity_ventas_final = quantity_ventas - quantity_ventas_delete
        self.assertEqual(quantity_ventas_final, 10)


    def tearDown(self):
        self.driver.close()
        self.driver.quit()


if __name__ == '__main__':
    unittest.main()
