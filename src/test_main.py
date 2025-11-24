import unittest
from main import calculate, app

class TestCalculatorFunction(unittest.TestCase):
    """ Unit tests for the calculate() function """

    def test_addition(self):
        self.assertEqual(calculate("add", 5, 3), 8)

    def test_subtraction(self):
        self.assertEqual(calculate("subtract", 10, 4), 6)

    def test_multiplication(self):
        self.assertEqual(calculate("multiply", 6, 7), 42)

    def test_division(self):
        self.assertEqual(calculate("divide", 8, 2), 4)

    def test_division_by_zero(self):
        self.assertIsNone(calculate("divide", 9, 0))

    def test_invalid_operation(self):
        self.assertIsNone(calculate("wrong", 5, 3))


class TestCalculatorAPI(unittest.TestCase):
    """ Tests for the Flask API endpoints """

    def setUp(self):
        self.client = app.test_client()

    def test_addition_api(self):
        response = self.client.get("/calculate?op=add&num1=5&num2=3")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.get_json(), {"result": 8})

    def test_invalid_operation_api(self):
        response = self.client.get("/calculate?op=wrong&num1=5&num2=3")
        self.assertEqual(response.status_code, 400)

    def test_division_by_zero_api(self):
        response = self.client.get("/calculate?op=divide&num1=8&num2=0")
        self.assertEqual(response.status_code, 400)
        data = response.get_json()
        self.assertIn("error", data)


if __name__ == "__main__":
    unittest.main()
