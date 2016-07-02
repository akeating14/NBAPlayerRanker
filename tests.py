from flask.ext.testing import TestCase
from project import app
import unittest


class BaseTestCase(TestCase):

    def create_app(self):

        app.config['TESTING'] = True
        return app


class Flask_TestCase(BaseTestCase):

    def test_index(self):
        response = self.client.get('/', content_type='html/text')
        self.assertEqual(response.status_code, 200)


if __name__ == '__main__':
    unittest.main()
