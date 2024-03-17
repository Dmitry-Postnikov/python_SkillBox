import unittest
from primer import app

class TestAccountingOfFinances(unittest.TestCase):
    def setUp(self) -> None:
        app.config['TESTING'] = True
        app.config['DEBUG'] = True
        self.app = app.test_client()

    def test_endpoint_add(self):
        date = "20240407"
        summ = "4400"
        url = "/add/" + date + "/" + summ
        response = self.app.get(url)
        response_data = response.data.decode()
        self.assertTrue("8800" in response_data)

    def test_endpoint_calculate_month(self):
        year = "2024"
        month = "04"
        url = "/calculate/" + year + "/" + month
        response = self.app.get(url)
        response_data = response.data.decode()
        self.assertTrue("13600" in response_data)

    def test_endpoint_calculate_year(self):
        year = "2024"
        url = "/calculate/" + year
        response = self.app.get(url)
        response_data = response.data.decode()
        self.assertTrue("18110" in response_data)

    def test_invalid_data_in_endpoint_add(self):
        date = "202d4d04dd07"
        summ = "4400"
        url = "/add/" + date + "/" + summ
        try:
            response = self.app.get(url)
        except:
            self.assertRaises(ValueError)