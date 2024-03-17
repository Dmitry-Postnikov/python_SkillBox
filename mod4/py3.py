import unittest
from hw1_registration import app


class TestRegistrationApp(unittest.TestCase):
    def setUp(self):
        app.config["TESTING"] = True
        app.config["DEBUG"] = True
        app.config["WTF_CSRF_ENABLED"] = False
        self.app = app.test_client()
        self.base_url = "/registration"
        self.valid_args = dict(email="dima.postnikov.04@mail.ru", phone=9223352924,
                               name="Dmitry", address="Lenina 4",
                               index=413722, comment="коммент")

    def test_email_valid(self):
        response = self.app.post(self.base_url, data=self.valid_args)
        self.assertIn("Successfully", response.data.decode())
        self.valid_args["email"] = "dima.postnikov.04@mail.ru"
        response = self.app.post(self.base_url, data=self.valid_args)
        self.assertIn("Successfully", response.data.decode())

    def test_email_invalid(self):
        self.valid_args["email"] = "dima.postnikov.04"
        response = self.app.post(self.base_url, data=self.valid_args)
        self.assertNotIn("Successfully", response.data.decode())
        self.valid_args["email"] = "dima.postnikov.04@mail"
        response = self.app.post(self.base_url, data=self.valid_args)
        self.assertNotIn("Successfully", response.data.decode())

    def test_email_empty(self):
        self.valid_args.pop("email")
        response = self.app.post(self.base_url, data=self.valid_args)
        self.assertNotIn("Successfully", response.data.decode())

    def test_phone_valid(self):
        response = self.app.post(self.base_url, data=self.valid_args)
        self.assertIn("Successfully", response.data.decode())
        self.valid_args["phone"] = 9223352924
        response = self.app.post(self.base_url, data=self.valid_args)
        self.assertIn("Successfully", response.data.decode())

    def test_phone_invalid_length(self):
        self.valid_args["phone"] = 92233529
        response = self.app.post(self.base_url, data=self.valid_args)
        self.assertNotIn("Successfully", response.data.decode())

    def test_phone_invalid_negative(self):
        self.valid_args["phone"] = -9223352924
        response = self.app.post(self.base_url, data=self.valid_args)
        self.assertNotIn("Successfully", response.data.decode())

    def test_phone_invalid_type(self):
        self.valid_args["phone"] = "srftcv"
        response = self.app.post(self.base_url, data=self.valid_args)
        self.assertNotIn("Successfully", response.data.decode())

    def test_phone_empty(self):
        self.valid_args.pop("phone")
        response = self.app.post(self.base_url, data=self.valid_args)
        self.assertNotIn("Successfully", response.data.decode())

    def test_name_valid(self):
        response = self.app.post(self.base_url, data=self.valid_args)
        self.assertIn("Successfully", response.data.decode())
        self.valid_args["name"] = "Dmitry"
        response = self.app.post(self.base_url, data=self.valid_args)
        self.assertIn("Successfully", response.data.decode())

    def test_name_empty(self):
        self.valid_args.pop("name")
        response = self.app.post(self.base_url, data=self.valid_args)
        self.assertNotIn("Successfully", response.data.decode())

    def test_address_valid(self):
        response = self.app.post(self.base_url, data=self.valid_args)
        self.assertIn("Successfully", response.data.decode())
        self.valid_args["address"] = "Lenina 4"
        response = self.app.post(self.base_url, data=self.valid_args)
        self.assertIn("Successfully", response.data.decode())

    def test_address_empty(self):
        self.valid_args.pop("address")
        response = self.app.post(self.base_url, data=self.valid_args)
        self.assertNotIn("Successfully", response.data.decode())

    def test_index_valid(self):
        response = self.app.post(self.base_url, data=self.valid_args)
        self.assertIn("Successfully", response.data.decode())
        self.valid_args["index"] = 413722
        response = self.app.post(self.base_url, data=self.valid_args)
        self.assertIn("Successfully", response.data.decode())

    def test_index_invalid_type(self):
        self.valid_args["index"] = "fsabdz"
        response = self.app.post(self.base_url, data=self.valid_args)
        self.assertNotIn("Successfully", response.data.decode())

    def test_index_empty(self):
        self.valid_args.pop("index")
        response = self.app.post(self.base_url, data=self.valid_args)
        self.assertNotIn("Successfully", response.data.decode())

    def test_comment_valid(self):
        response = self.app.post(self.base_url, data=self.valid_args)
        self.assertIn("Successfully", response.data.decode())
        self.valid_args["comment"] = "коммент"
        response = self.app.post(self.base_url, data=self.valid_args)
        self.assertIn("Successfully", response.data.decode())

    def test_comment_valid_none(self):
        self.valid_args.pop("comment")
        response = self.app.post(self.base_url, data=self.valid_args)
        self.assertIn("Successfully", response.data.decode())


if __name__ == '__main__':
    unittest.main()
