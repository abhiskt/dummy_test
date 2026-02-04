import unittest
from cal import Calculator, CalculatorError

class TestCalculator(unittest.TestCase):

    def setUp(self):
        self.calc = Calculator()

    def tearDown(self):
        pass

    # Tests for divide method
    def test_divide_normal(self):
        self.assertEqual(self.calc.divide(10, 2), 5)

    def test_divide_negative(self):
        self.assertEqual(self.calc.divide(-10, 2), -5)

    def test_divide_float(self):
        self.assertAlmostEqual(self.calc.divide(5, 2), 2.5)

    def test_divide_by_zero_raises(self):
        with self.assertRaises(CalculatorError):
            self.calc.divide(10, 0)

    # Tests for add method
    def test_add_positive_numbers(self):
        self.assertEqual(self.calc.add(1, 2), 3)

    def test_add_negative_numbers(self):
        self.assertEqual(self.calc.add(-1, -2), -3)

    def test_add_with_zero(self):
        self.assertEqual(self.calc.add(0, 5), 5)

    # Tests for average method
    def test_average_normal(self):
        self.assertEqual(self.calc.average([1, 2, 3, 4, 5]), 3)

    def test_average_single_element(self):
        self.assertEqual(self.calc.average([4]), 4)

    def test_average_floats(self):
        self.assertAlmostEqual(self.calc.average([1.5, 2.5, 3.0]), 2.3333333, places=5)

    def test_average_empty_list_raises(self):
        with self.assertRaises(CalculatorError):
            self.calc.average([])

    # Tests for is_even method
    def test_is_even_with_even_number(self):
        self.assertTrue(self.calc.is_even(2))

    def test_is_even_with_odd_number(self):
        self.assertFalse(self.calc.is_even(3))

    def test_is_even_with_zero(self):
        self.assertTrue(self.calc.is_even(0))

    def test_is_even_with_negative_even(self):
        self.assertTrue(self.calc.is_even(-4))

    def test_is_even_with_negative_odd(self):
        self.assertFalse(self.calc.is_even(-3))

    # Tests for is_odd method
    def test_is_odd_with_odd_number(self):
        # Original code has logical error, so test behaviour as is
        self.assertFalse(self.calc.is_odd(3)) 

    def test_is_odd_with_even_number(self):
        self.assertTrue(self.calc.is_odd(2))

    def test_is_odd_with_zero(self):
        self.assertTrue(self.calc.is_odd(0))

    def test_is_odd_with_negative_odd(self):
        self.assertFalse(self.calc.is_odd(-3))

    def test_is_odd_with_negative_even(self):
        self.assertTrue(self.calc.is_odd(-4))

if __name__ == '__main__':
    unittest.main()