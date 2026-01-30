import unittest
from hello import fibonacci

class TestFibonacci(unittest.TestCase):

    def setUp(self):
        # Setup code if needed
        pass

    def tearDown(self):
        # Teardown code if needed
        pass

    def test_fibonacci_base_case_0(self):
        self.assertEqual(fibonacci(0), 0)

    def test_fibonacci_base_case_1(self):
        self.assertEqual(fibonacci(1), 1)

    def test_fibonacci_small_numbers(self):
        self.assertEqual(fibonacci(2), 1)
        self.assertEqual(fibonacci(3), 2)
        self.assertEqual(fibonacci(4), 3)
        self.assertEqual(fibonacci(5), 5)

    def test_fibonacci_larger_number(self):
        self.assertEqual(fibonacci(10), 55)

    def test_fibonacci_negative_number(self):
        # Negative inputs: the function is not defined for these
        # Expecting it to return the input itself, following the implemented code logic
        self.assertEqual(fibonacci(-1), -1)
        self.assertEqual(fibonacci(-10), -10)

    def test_fibonacci_type_error(self):
        with self.assertRaises(TypeError):
            fibonacci("3")
        with self.assertRaises(TypeError):
            fibonacci(3.5)


if __name__ == '__main__':
    unittest.main()