import unittest
from cal import Calculator, CalculatorError

class TestCalculator(unittest.TestCase):

    def setUp(self):
        self.calc = Calculator()

    def tearDown(self):
        del self.calc

    def test_divide_normal(self):
        self.assertEqual(self.calc.divide(10, 2), 5)
        self.assertAlmostEqual(self.calc.divide(7, 3), 7/3)

    def test_divide_zero_division_error(self):
        with self.assertRaises(CalculatorError) as context:
            self.calc.divide(10, 0)
        self.assertEqual(str(context.exception), "Division by zero")

    def test_add_positive_numbers(self):
        self.assertEqual(self.calc.add(5, 7), 12)

    def test_add_negative_numbers(self):
        self.assertEqual(self.calc.add(-3, -6), -9)

    def test_add_mixed_sign_numbers(self):
        self.assertEqual(self.calc.add(-2, 3), 1)

    def test_average_normal(self):
        self.assertEqual(self.calc.average([1, 2, 3, 4]), 2.5)
        self.assertAlmostEqual(self.calc.average([1.5, 2.5, 3.0]), (1.5+2.5+3.0)/3)

    def test_average_empty_list_error(self):
        with self.assertRaises(CalculatorError) as context:
            self.calc.average([])
        self.assertEqual(str(context.exception), "Empty list")

    def test_is_even_true(self):
        self.assertTrue(self.calc.is_even(0))
        self.assertTrue(self.calc.is_even(2))
        self.assertTrue(self.calc.is_even(-4))

    def test_is_even_false(self):
        self.assertFalse(self.calc.is_even(3))
        self.assertFalse(self.calc.is_even(-1))

if __name__ == "__main__":
    unittest.main()