import unittest
from io import StringIO
import sys

class TestHelloWorldOutput(unittest.TestCase):
    def setUp(self):
        self.captured_output = StringIO()          # Create StringIO object to capture output
        sys.stdout = self.captured_output          # Redirect stdout.

    def tearDown(self):
        sys.stdout = sys.__stdout__                # Reset redirect.

    def test_print_hello_world(self):
        # Re-import the module to trigger print statement
        import importlib
        import hello
        importlib.reload(hello)
        self.assertEqual(self.captured_output.getvalue().strip(), "hello world")

if __name__ == '__main__':
    unittest.main()