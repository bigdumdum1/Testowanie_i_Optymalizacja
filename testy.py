import unittest
from app import app, get_comments, create_html_table


class TestApp(unittest.TestCase):

    def setUp(self):
        self.app = app.test_client()


    def test_create_html_table(self):
        comments = [{'name': 'user1', 'email': 'user1@example.com', 'body': 'comment1'}]
        html_table = create_html_table(comments)
        expected_table = """
        <table>
        <thead>
            <tr>
                <th>Nazwa użytkownika</th>
                <th>Email</th>
                <th>Treść</th>
            </tr>
        </thead>
        <tbody id="comments-table-body">
        </tbody>
    </table>
        """
        self.assertEqual(html_table.strip(), expected_table.strip())

        # Test dla funkcji index()
    def test_index(self):
        with app.test_client() as client:
            response = client.get('/')
            self.assertEqual(response.status_code, 200)
            self.assertIn(b'<title>Index</title>', response.data)

    # Test dla funkcji komentarze()
    def test_komentarze(self):
        with app.test_client() as client:
            response = client.get('/komentarze')
            self.assertEqual(response.status_code, 200)
            self.assertIn(b'<title>Komentarze</title>', response.data)

    # Test dla funkcji albumy()
    def test_albumy(self):
        with app.test_client() as client:
            response = client.get('/Albumy')
            self.assertEqual(response.status_code, 200)
            self.assertIn(b'<title>albumy</title>', response.data)

    # Test dla funkcji zdjecia()
    def test_zdjecia(self):
        with app.test_client() as client:
            response = client.get('/Zdjecia')
            self.assertEqual(response.status_code, 200)
            self.assertIn(b'<title>Zdjecia</title>', response.data)

    # Test dla funkcji posty()
    def test_posty(self):
        with app.test_client() as client:
            response = client.get('/posty')
            self.assertEqual(response.status_code, 200)
            self.assertIn(b'<title>Posty</title>', response.data)

    if __name__ == '__main__':
        unittest.main()