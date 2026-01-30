import unittest
from main_div import divide

class TestDivideFunction(unittest.TestCase):

    def test_divide_positive_numbers(self):
        self.assertEqual(divide(10, 2), 5)

    def test_divide_negative_numbers(self):
        self.assertEqual(divide(-10, -2), 5)

    def test_divide_positive_by_negative(self):
        self.assertEqual(divide(10, -2), -5)

    def test_divide_zero_numerator(self):
        self.assertEqual(divide(0, 5), 0)

    def test_divide_float_result(self):
        self.assertAlmostEqual(divide(7, 2), 3.5)

    def test_divide_by_zero(self):
        self.assertEqual(divide(5, 0), "Division by zero is not allowed")

    def test_divide_large_numbers(self):
        self.assertEqual(divide(10**10, 10**5), 10**5)

    def test_divide_result_precision(self):
        result = divide(1, 3)
        self.assertTrue(abs(result - 0.3333) < 0.0001)

if __name__ == "__main__":
    unittest.main()