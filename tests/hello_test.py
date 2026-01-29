import unittest
from io import StringIO
import sys

class TestHelloPrint(unittest.TestCase):
    def setUp(self):
        # Redirect stdout to capture print output
        self.held_stdout = sys.stdout
        sys.stdout = StringIO()

    def tearDown(self):
        # Restore stdout
        sys.stdout = self.held_stdout

    def test_hello_world_printed(self):
        # Importing the module here triggers the print statement
        import hello
        output = sys.stdout.getvalue()
        self.assertEqual(output, "hello world\n")

if __name__ == '__main__':
    unittest.main()