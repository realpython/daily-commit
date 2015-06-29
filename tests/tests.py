import unittest
from project import app


class TestApp(unittest.TestCase):
    """ Tests for the git_text API """

    def setUp(self):
        """ Test setup """
        # Configure our app to use the testing database
        app.config.from_object('project.config.TestingConfig')
        self.client = app.test_client()

    def tearDown(self):
        """ Test teardown """
        pass

    def test_app_is_testing(self):
        self.assertTrue(app.config['TESTING'])

    def test_ping_route(self):
        response = self.client.get('/ping')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data, b'pong!')
        self.assertEqual(response.mimetype, "text/html")
