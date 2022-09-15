from django.test import TestCase, Client
from django.urls import resolve
from .views import show_katalog

# Create your tests here.
class KatalogTestCase(TestCase):
    def test_katalog_app_url_exists(self):
        response = Client().get("/katalog/")
        self.assertEqual(response.status_code, 200)
    
    def test_katalog_app_using_correct_template(self):
        response = Client().get('/katalog/')
        self.assertTemplateUsed(response, 'katalog.html')

    
