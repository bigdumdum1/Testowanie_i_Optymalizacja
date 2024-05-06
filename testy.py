import unittest
from unittest.mock import patch, MagicMock
from app import app, get_comments, create_photos, create_posts, create_albums
from io import StringIO
import coverage
import requests
import pytest
from locust import HttpUser, task, between

class TestApp(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()

    def test_index_links(self):
        # Testowanie linków
        response = self.app.get('/')
        decoded_response = response.data.decode('utf-8')
        self.assertIn('<a href="komentarze"><button class="large-button"> Komentarze</button></a>', decoded_response)
        # Testowanie linku do zdjęć
        self.assertIn('<a href="zdjecia"><button class="large-button">Zdjęcia</button></a>', decoded_response)
        # Testowanie linku do albumów
        self.assertIn('<a href="albumy"><button class="large-button">Albumy</button></a>', decoded_response)
        # Testowanie linku do postów
        self.assertIn('<a href="posty"><button class="large-button">Posty</button></a>', decoded_response)
    def test_komentarze_route(self):
        # Testowanie poprawności ścieżki komentarzy
        response = self.app.get('/komentarze')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'id', response.data)
        self.assertIn(b'Nazwa uzytkownika', response.data)
        self.assertIn(b'email', response.data)
        self.assertIn(b'Tresc komentarza', response.data)

    def test_albumy_route(self):
        # Testowanie poprawności ścieżki albumów
        response = self.app.get('/albumy')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Id', response.data)
        self.assertIn(b'Tytul', response.data)

    def test_index(self):
        with app.test_client() as client:
            response = client.get('/')
            self.assertEqual(response.status_code, 200)
            self.assertIn(b'<title>Index</title>', response.data)

    # Test dla funkcji komentarze() czy się otwiera
    def test_komentarze(self):
        with app.test_client() as client:
            response = client.get('/komentarze')
            self.assertEqual(response.status_code, 200)
            self.assertIn(b'id', response.data)
            self.assertIn(b'Nazwa uzytkownika', response.data)
            self.assertIn(b'email', response.data)
            self.assertIn(b'Tresc komentarza', response.data)

    def test_posty_route(self):
        # Testowanie poprawności ścieżki postów
        response = self.app.get('/posty')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'User id', response.data)
        self.assertIn(b'Nazwa uzytkownika', response.data)
        self.assertIn(b'Tresc postu', response.data)
    def test_create_albums_empty_data(self):
        # Testowanie funkcji create_albums() z pustymi danymi wejściowymi
        data = []
        html_template = create_albums(data)
        expected_html = """
        <!DOCTYPE html>
    <html>
    <head>
    <title>{filename}</title>
    </head>
    <body>
        <h1>{filename}</h1>
        <table>
            <thead>
                <tr>
                    <th>Właściciel albumu</th>
                    <th>Cover albumu</th>
                    <th>Opis albumu</th>
                </tr>
            </thead>
            <tbody>
                {table_rows}
            </tbody>
        </table>
    </body>
    </html>
        """
        self.assertEqual(html_template.strip(), expected_html.strip())


    def test_create_photos_without_data(self):
        data = []

        html_template = create_photos(data)
class WebsiteUser(HttpUser):

    wait_time = between(1, 5)
    @task
    def view_homepage(self):
        self.client.get("/")
    @task
    def view_albums(self):
        self.client.get("/albumy")

    @task
    def view_comments(self):
        self.client.get("/komentarze")

    @task
    def view_posts(self):
        self.client.get("/posty")

    @task
    def view_images(self):
        self.client.get("/zdjecia")

if __name__ == '__main__':
    unittest.main()

# locust -f testy.py
