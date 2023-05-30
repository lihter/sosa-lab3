import math
import unittest
from Dodatak_A import OperationsManager

class OperationsManagerTestCase(unittest.TestCase):

    def setUp(self) -> None:
        self.ops_manager = OperationsManager(14, 2)
        return super().setUp()

    def test_perform_division(self):
        calculated_value = self.ops_manager.perform_division()
        self.assertEqual(calculated_value, 7)
    
    def test_perform_division_with_zero(self):
        ops_manager = OperationsManager(14, 0)
        calculated_value = ops_manager.perform_division()
        self.assertTrue(math.isnan(calculated_value))

    def test_perform_multiplication(self):
        calculated_value = self.ops_manager.perform_multiplication()
        self.assertEqual(calculated_value, 28)
    
    def test_perform_subtraction(self):
        calculated_value = self.ops_manager.perform_subtraction()
        self.assertEqual(calculated_value, 12)

    def test_perform_addition(self):
        calculated_value = self.ops_manager.perform_addition()
        self.assertEqual(calculated_value, 16)

if __name__ == '__main__':
    unittest.main()
