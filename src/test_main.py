import unittest
from main import app

class TestCalculatorAPI(unittest.TestCase):
    def setUp(self):
        self.client = app.test_client()

    def test_addition_endpoint(self):
        response = self.client.get("/calculate?op=add&num1=5&num2=3")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.get_json(), {"result": 8})

    def test_divide_by_zero_endpoint(self):
        response = self.client.get("/calculate?op=divide&num1=9&num2=0")
        self.assertEqual(response.status_code, 400)
        self.assertIn("error", response.get_json())
