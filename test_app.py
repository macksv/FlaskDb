# Unit test for app
import unittest
from app import app


class FlaskDbTest(unittest.TestCase):

    # Check if response is 200
    def test_index(self):
        # test_client is a method provided by flask app
        tester = app.test_client(self)
        response = tester.get("/")
        statuscode = response.status_code
        self.assertEqual(statuscode, 200)

    # Check if content-type is text/html
    def test_index_content_type(self):
        tester = app.test_client(self)
        response = tester.get("/")
        #self.assertEqual(response.content_type, "text/html")
        assert "text/html" in response.content_type

    # Check for data content - for this case we just check for the title as an example
    def test_index_content_data(self):
        tester = app.test_client(self)
        response = tester.get("/")
        self.assertTrue(b"My Flask App" in response.data)


if __name__ == "__main__":
    unittest.main()
