import unittest
from main_div import divide

class TestDivideFunction(unittest.TestCase):

    def test_divide_positive_numbers(self):
        self.assertEqual(divide(10, 2), 5)

    def test_divide_negative_numbers(self):
        self.assertEqual(divide(-10, -2), 5)

    def test_divide_positive_by_negative(self):
        self.assertEqual(divide(10, -2), -5)

    def test_divide_negative_by_positive(self):
        self.assertEqual(divide(-10, 2), -5)

    def test_divide_by_zero(self):
        self.assertEqual(divide(10, 0), "Division by zero is not allowed")

    def test_divide_zero_by_number(self):
        self.assertEqual(divide(0, 5), 0)

    def test_divide_floats(self):
        self.assertAlmostEqual(divide(5.5, 2.2), 2.5)

    def test_divide_large_numbers(self):
        self.assertEqual(divide(1000000000, 2), 500000000)

    def test_divide_with_one(self):
        self.assertEqual(divide(7, 1), 7)

if __name__ == '__main__':
    unittest.main()