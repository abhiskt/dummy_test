import unittest
from unittest import mock
import builtins

class TestHelloPrint(unittest.TestCase):
    
    @mock.patch('builtins.print')
    def test_hello_world_printed(self, mock_print):
        # Ensure that print is called once with "hello world"
        import hello  # Import the module to execute the print
        mock_print.assert_called_once_with("hello world")

if __name__ == '__main__':
    unittest.main()