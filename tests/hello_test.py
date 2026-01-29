import unittest
from io import StringIO
import sys

class TestHelloWorldPrint(unittest.TestCase):
    def setUp(self):
        # Capture output during the test
        self.held_stdout = StringIO()
        self.original_stdout = sys.stdout
        sys.stdout = self.held_stdout

    def tearDown(self):
        # Restore original stdout
        sys.stdout = self.original_stdout

    def test_hello_world_output(self):
        # Run the hello.py code in isolated namespace
        namespace = {}
        with open('hello.py') as f:
            code = f.read()
            exec(code, namespace)
        self.assertEqual(self.held_stdout.getvalue(), "hello world\n")

if __name__ == '__main__':
    unittest.main()