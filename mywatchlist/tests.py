# Create your tests here.
import unittest
from django.test import Client

class MyWatchlistTestCase(unittest.TestCase):
    def test_html(self):
        client = Client()
        response = client.get('/mywatchlist/html/')
        self.assertEqual(response.status_code, 200)

    def test_xml(self):
        client = Client()
        response = client.get('/mywatchlist/xml/')
        self.assertEqual(response.status_code, 200)

    def test_json(self):
        client = Client()
        response = client.get('/mywatchlist/json/')
        self.assertEqual(response.status_code, 200)