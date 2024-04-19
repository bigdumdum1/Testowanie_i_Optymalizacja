import unittest
from app import app, create_html_table
#7/12 testów
class TestApp(unittest.TestCase):
    maxDiff = None
    def setUp(self):
        self.app = app.test_client()



        # Test dla funkcji index() czy się otwiera
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
            self.assertIn(b'<title>Komentarze</title>', response.data)

    #Test dla Index czy działają linki
    def test_index_links(self):
        # Testowanie linku do komentarzy
        response = self.app.get('/')
        decoded_response = response.data.decode('utf-8')
        self.assertIn('<a href="komentarze"><button class="large-button"> Komentarze</button></a>', decoded_response)
        # Testowanie linku do zdjęć
        self.assertIn('<a href="zdjecia"><button class="large-button">Zdjęcia</button></a>', decoded_response)
        # Testowanie linku do albumów
        self.assertIn('<a href="albumy"><button class="large-button">Albumy</button></a>', decoded_response)
        # Testowanie linku do postów
        self.assertIn('<a href="posty"><button class="large-button">Posty</button></a>', decoded_response)

    # Test dla wyglądu tabeli w albumach()
    def test_albumy_tabela(self):
        with app.test_client() as client:
            response = client.get('/albumy')
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
        <tbody>
    
            <tr>
                <td>user1</td>
                <td>user1@example.com</td>
                <td>comment1</td>
            </tr>
        
        </tbody>
    </table>

            """
            self.assertEqual(html_table.strip(), expected_table.strip())

    # Test dla funkcji zdjecia() o tabeli
    def test_zdjecia(self):
        with app.test_client() as client:
            response = client.get('/zdjecia')
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
        <tbody>
    
            <tr>
                <td>user1</td>
                <td>user1@example.com</td>
                <td>comment1</td>
            </tr>
        
        </tbody>
    </table>

                """
            self.assertEqual(html_table.strip(), expected_table.strip())

    # Test dla funkcji posty() czy się otwiera
    def test_posty(self):
        with app.test_client() as client:
            response = client.get('/posty')
            self.assertEqual(response.status_code, 200)
            self.assertIn(b'<title>Posty</title>', response.data)


    #Test dla wyglądu tabeli w komentarzach
    def test_komentarze_tabela(self):
        with app.test_client() as client:
            response = client.get('/komentarze')
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
        <tbody>
    
            <tr>
                <td>user1</td>
                <td>user1@example.com</td>
                <td>comment1</td>
            </tr>
        
        </tbody>
    </table>

            """
            self.assertEqual(html_table.strip(), expected_table.strip())






    if __name__ == '__main__':
        unittest.main()
