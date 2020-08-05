import unittest
import tests.test_elimination_sale_associated_with_product
import tests.test_sale_with_different_payment_methods_and_leave
import tests.test_creation_payment_credit_card

loader = unittest.TestLoader()
suite = unittest.TestSuite()

suite.addTest(loader.loadTestsFromModule(tests.test_elimination_sale_associated_with_product))
suite.addTest(loader.loadTestsFromModule(tests.test_creation_payment_credit_card))
suite.addTest(loader.loadTestsFromModule(tests.test_sale_with_different_payment_methods_and_leave))

runner = unittest.TextTestRunner(verbosity=3)
result = runner.run(suite)
