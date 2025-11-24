import unittest
from unittest.mock import patch
from io import StringIO
import calculator   # <-- This should match your filename (calculator.py)


class TestCalculator(unittest.TestCase):

    @patch('builtins.input', side_effect=['1', '5', '3'])
    @patch('sys.stdout', new_callable=StringIO)
    def test_addition(self, mock_stdout, mock_input):
        calculator.calculator()
        output = mock_stdout.getvalue()
        self.assertIn("Result: 8.0", output)

    @patch('builtins.input', side_effect=['2', '10', '4'])
    @patch('sys.stdout', new_callable=StringIO)
    def test_subtraction(self, mock_stdout, mock_input):
        calculator.calculator()
        output = mock_stdout.getvalue()
        self.assertIn("Result: 6.0", output)

    @patch('builtins.input', side_effect=['3', '6', '7'])
    @patch('sys.stdout', new_callable=StringIO)
    def test_multiplication(self, mock_stdout, mock_input):
        calculator.calculator()
        output = mock_stdout.getvalue()
        self.assertIn("Result: 42.0", output)

    @patch('builtins.input', side_effect=['4', '8', '2'])
    @patch('sys.stdout', new_callable=StringIO)
    def test_division(self, mock_stdout, mock_input):
        calculator.calculator()
        output = mock_stdout.getvalue()
        self.assertIn("Result: 4.0", output)

    @patch('builtins.input', side_effect=['4', '9', '0'])
    @patch('sys.stdout', new_callable=StringIO)
    def test_division_by_zero(self, mock_stdout, mock_input):
        calculator.calculator()
        output = mock_stdout.getvalue()
        self.assertIn("Error: Cannot divide by zero!", output)

    @patch('builtins.input', side_effect=['9'])
    @patch('sys.stdout', new_callable=StringIO)
    def test_invalid_choice(self, mock_stdout, mock_input):
        calculator.calculator()
        output = mock_stdout.getvalue()
        self.assertIn("Invalid choice!", output)


if __name__ == '__main__':
    unittest.main()
