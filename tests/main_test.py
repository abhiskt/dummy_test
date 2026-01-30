import unittest
from main import divide

class TestDivideFunction(unittest.TestCase):
    def setUp(self):
        # Setup can be used if needed, not required here
        pass

    def tearDown(self):
        # Cleanup resources if needed, not required here
        pass

    def test_divide_positive_numbers(self):
        self.assertEqual(divide(10, 2), 5)

    def test_divide_negative_dividend(self):
        self.assertEqual(divide(-10, 2), -5)

    def test_divide_negative_divisor(self):
        self.assertEqual(divide(10, -2), -5)

    def test_divide_negative_both(self):
        self.assertEqual(divide(-10, -2), 5)

    def test_divide_float_result(self):
        self.assertEqual(divide(7, 2), 3.5)

    def test_divide_by_one(self):
        self.assertEqual(divide(10, 1), 10)

    def test_divide_zero_dividend(self):
        self.assertEqual(divide(0, 5), 0)

    def test_divide_raises_zero_division_error(self):
        with self.assertRaises(ZeroDivisionError):
            divide(10, 0)

if __name__ == '__main__':
    unittest.main()