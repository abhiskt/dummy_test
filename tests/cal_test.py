import unittest
from cal import Calculator, CalculatorError

class TestCalculator(unittest.TestCase):
    def setUp(self):
        self.calc = Calculator()
    
    def tearDown(self):
        pass

    # Tests for add method
    def test_add_positive_numbers(self):
        self.assertEqual(self.calc.add(2, 3), 5)

    def test_add_negative_numbers(self):
        self.assertEqual(self.calc.add(-2, -3), -5)

    def test_add_zero(self):
        self.assertEqual(self.calc.add(0, 5), 5)
        self.assertEqual(self.calc.add(5, 0), 5)

    # Tests for divide method
    def test_divide_positive_numbers(self):
        self.assertEqual(self.calc.divide(10, 2), 5)

    def test_divide_negative_numbers(self):
        self.assertEqual(self.calc.divide(-10, 2), -5)
        self.assertEqual(self.calc.divide(10, -2), -5)
        self.assertEqual(self.calc.divide(-10, -2), 5)

    def test_divide_result_float(self):
        self.assertAlmostEqual(self.calc.divide(7, 2), 3.5)

    def test_divide_by_zero_raises(self):
        with self.assertRaises(CalculatorError) as context:
            self.calc.divide(10, 0)
        self.assertEqual(str(context.exception), "Division by zero")

    # Tests for average method
    def test_average_normal_list(self):
        self.assertEqual(self.calc.average([1, 2, 3, 4, 5]), 3)

    def test_average_single_element(self):
        self.assertEqual(self.calc.average([10]), 10)

    def test_average_floats(self):
        self.assertAlmostEqual(self.calc.average([1.5, 2.5, 3.5]), 2.5)

    def test_average_empty_list_raises(self):
        with self.assertRaises(CalculatorError) as context:
            self.calc.average([])
        self.assertEqual(str(context.exception), "Empty list")

    # Tests for is_even method
    def test_is_even_with_even_number(self):
        self.assertTrue(self.calc.is_even(2))
        self.assertTrue(self.calc.is_even(0))
        self.assertTrue(self.calc.is_even(-4))

    def test_is_even_with_odd_number(self):
        self.assertFalse(self.calc.is_even(1))
        self.assertFalse(self.calc.is_even(-3))
        self.assertFalse(self.calc.is_even(7))

if __name__ == '__main__':
    unittest.main()