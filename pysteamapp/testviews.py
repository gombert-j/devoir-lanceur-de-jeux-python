from django.test import TestCase, Client
from bs4 import BeautifulSoup


class ViewsTest(TestCase):
    fixtures = ['init']

    def setUp(self):
        self.client = Client()

    def test_index(self):
        response = self.client.get('/')
        self.assertEqual(200, response.status_code)

    def test_une_collection(self):
        response = self.client.get('/')
        soup = BeautifulSoup(response.content, 'html.parser')
        self.assertEqual(1, len(soup.find_all('li')))

    def test_collection_contient_jeu(self):
        response = self.client.get('/bibliotheques/1')
        soup = BeautifulSoup(response.content, 'html.parser')
        self.assertLessEqual(1, len(soup.find_all('li')))
